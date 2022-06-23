import logging
from collections.abc import Callable, Iterable, Iterator, Sequence
from csv import reader as csv_reader
from datetime import date, datetime, time
from os.path import isfile
from tempfile import mkstemp
from typing import Optional, Type, TypeVar

from requests import Session

from aapi.csv.parse import parse_bool, parse_float, parse_int, parse_point, \
    parse_multipolygon
from aapi.models import Model, Multipolygon, Point
from aapi.session import make_session

T = TypeVar('T')    # Value/type

logger = logging.getLogger(__name__)


class CsvEndpoint(Iterable[Model]):
    """Model voor toegang tot CSV-bestanden met lokale caching naar disk.

    Subclasses definieren de URL en het data model voor de rijen in het
    CSV-bestand. In speciale gevallen kan ook de row_parser overschreven
    worden.

    Het object is iterable. Elke keer dat over het object geïtereerd
    wordt, wordt het bestand van disk opnieuw gelezen.

    Mocht het bestand op dat moment niet bestaan dan wordt het eerst
    gedownload van de URL en met de parameters opgegeven in de
    constructor en opgeslagen.
    """
    delimiter: str = ','
    quotechar: str = '"'
    url: str
    model: Type[Model]
    header: tuple[str] = None

    def __init__(self, cache_filename: str, params: dict[str, str],
                 session: Optional[Session] = None) -> None:
        params['_format'] = 'csv'
        self.cache_filename = cache_filename or mkstemp()
        self.params = params
        self.session = session or make_session()

    def check_header(self, header: Sequence[str]) -> None:
        """Raises an error if the header is not as expected.
        """
        self_header = self.header or self.model.__annotations__
        expected = tuple(f.lower() for f in self_header)
        observed = tuple(f.lower() for f in header[:len(expected)])
        assert observed == expected, f'{observed!r} != {expected!r}'

    def fetch(self) -> None:
        """Downloads the CSV file in full.
        """
        logger.info(f'Fetch {self.url!r} met params {self.params!r}.')
        res = self.session.get(self.url, params=self.params)

        with open(self.cache_filename, 'wb') as fd:
            for chunk in res.iter_content():
                fd.write(chunk)

    def row_parser(self) -> Callable[[Sequence[str]], Model]:
        """Returns a function that parses string tuples to model instances.
        """
        def parse_row(row: Sequence[str]) -> Model:
            return model(*(parse(v) for parse, v in zip(funcs, row)))

        type_parser = {
            bool: optional(parse_bool),
            date: optional(date.fromisoformat),
            datetime: optional(datetime.fromisoformat),
            int: optional(parse_int),
            float: optional(parse_float),
            str: str,
            time: optional(time.fromisoformat),
            Point: optional(parse_point),
            Multipolygon: optional(parse_multipolygon),
        }

        model = self.model
        funcs = [type_parser[typ] for typ in model.__annotations__.values()]
        return parse_row

    def __iter__(self) -> Iterator[Model]:
        """Returns an iterator over all rows.
        """
        parse_row = self.row_parser()
        if not isfile(self.cache_filename):
            self.fetch()
        with open(self.cache_filename, encoding='utf-8', newline='') as f:
            reader = csv_reader(
                f, delimiter=self.delimiter, quotechar=self.quotechar)
            self.check_header(next(reader))
            for row in reader:
                yield parse_row(row)


def optional(func: Callable[[str], T]) -> Callable[[str], Optional[T]]:
    def parse(s: str) -> Optional[T]:
        try:
            return func(s)
        except (ValueError, KeyError, IndexError, TypeError):
            return None
    return parse
