from collections.abc import Callable, Sequence

from aapi.csv.base import CsvEndpoint
from aapi.models import (
    Model, Afvalbijplaatsing, Afvalcontainer,
    Afvalcontainertype, AfvalLoopafstandAdres, Nummeraanduiding,
    OpenbareRuimte, Verblijfsobject, Afvalweging
)

__all__ = ['BijplaatsingenCsv', 'ContainersCsv', 'ContainertypesCsv',
           'LoopafstandenCsv', 'NummeraanduidingenCsv', 'OpenbareRuimtesCsv',
           'VerblijfsobjectenCsv', 'WegingenCsv']


class BijplaatsingenCsv(CsvEndpoint[Afvalbijplaatsing]):
    url = f'https://api.data.amsterdam.nl/v1/huishoudelijkafval/bijplaatsingen/'
    model = Afvalbijplaatsing


class ContainersCsv(CsvEndpoint[Afvalcontainer]):
    url = f'https://api.data.amsterdam.nl/v1/huishoudelijkafval/container/'
    model = Afvalcontainer


class ContainertypesCsv(CsvEndpoint[Afvalcontainertype]):
    url = f'https://api.data.amsterdam.nl/v1/huishoudelijkafval/containertype/'
    model = Afvalcontainertype


# class FractiebestandenCsv(CsvEndpoint[Fractiebestand]):
#     url = None
#     model = Fractiebestand
#     delimiter = ';'
#     header = (
#         'Chauffeursomschrijving', 'Buurt', 'Aantal', 'Container1',
#         'Container2', 'FreqWeek', 'ClusterId', 'Stadsdeel', 'Adres CMS',
#         'Type Inzameling', 'wpo', 'wpe', 'Oneven', 'Maandag.1', 'Dinsdag.2',
#         'Woensdag.3', 'Donderdag.4', 'Vrijdag.5', 'Zaterdag.6', 'Zondag.7',
#         'Even', 'Maandag.8', 'Dinsdag.9', 'Woensdag.10', 'Donderdag.11',
#         'Vrijdag.12', 'Zaterdag.13', 'Zondag.14', 'ExtraInfo', 'LocCode',
#         'LocCapaciteit', 'Lat', 'Long', 'Wijk', 'Gebied', 'Fractie',
#         'Zondag DuBez', 'Zondag EnkBez', 'RouteNr.dub', 'RouteNr.eb', 'Volume',
#         'CapaciteitStats', 'FreqWeek afgeleid', 'LedigingenWeek',
#     )


class LoopafstandenCsv(CsvEndpoint[AfvalLoopafstandAdres]):
    url = (f'https://api.data.amsterdam.nl/v1/'
           f'huishoudelijkafval/adres_loopafstand/')
    model = AfvalLoopafstandAdres


class NummeraanduidingenCsv(CsvEndpoint[Nummeraanduiding]):
    url = f'https://api.data.amsterdam.nl/v1/bag/nummeraanduidingen/'
    model = Nummeraanduiding

    def row_parser(self) -> Callable[[Sequence[str]], Model]:
        def with_adjusted_id(row: Sequence[str]) -> Model:
            model = parse(row)
            return model._replace(id=model.id.split('.')[0])

        parse = super().row_parser()
        return with_adjusted_id


class OpenbareRuimtesCsv(CsvEndpoint[OpenbareRuimte]):
    url = f'https://api.data.amsterdam.nl/v1/bag/openbareruimtes/'
    model = OpenbareRuimte

    def row_parser(self) -> Callable[[Sequence[str]], Model]:
        def with_adjusted_id(row: Sequence[str]) -> Model:
            model = parse(row)
            return model._replace(id=model.id.split('.')[0])

        parse = super().row_parser()
        return with_adjusted_id


# class ReinigingsrechtCsv(CsvEndpoint[Reinigingsrecht]):
#     url = None
#     model = Reinigingsrecht
#     delimiter = ';'
#     header = (
#         'Postk N', 'Postk A', 'Naam', 'Subjectnr', 'BELOBJNR', 'Straat',
#         'Huisnr', 'Toev', 'Stadsdeel', 'Reintarcode', 'DDINGANG_OBJ',
#         'DDINGANG_REL', 'Count of JJHEFFING',
#     )


class VerblijfsobjectenCsv(CsvEndpoint[Verblijfsobject]):
    url = 'https://api.data.amsterdam.nl/v1/bag/verblijfsobjecten/'
    model = Verblijfsobject
    header = tuple(Verblijfsobject.__annotations__)[:-2]
    # gebruiksdoel en toegang vallen eraf in het CSV formaat. (Waarom?)

    def row_parser(self) -> Callable[[list[str]], Model]:
        """Returns a function that parses string tuples to model instances.
        """
        def parse_row(row: list[str]) -> Model:
            # Lege velden voor gebruiksdoel en toegang.
            return parse(row + ['', ''])

        parse = super().row_parser()
        return parse_row


class WegingenCsv(CsvEndpoint[Afvalweging]):
    url = 'https://api.data.amsterdam.nl/v1/huishoudelijkafval/weging/'
    model = Afvalweging
