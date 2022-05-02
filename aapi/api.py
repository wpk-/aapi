import logging
from collections.abc import Iterator
from typing import Any, Optional, Generic, Type
from urllib.parse import urlencode

import orjson as orjson
import requests as requests

from aapi.geojson import model_parser, model_parser_v0
from aapi.models import (
    Model,
    Afvalbijplaatsing, Afvalcluster, Afvalclusterfractie, Afvalcontainer,
    Afvalcontainerlocatie, Afvalcontainertype, AfvalLoopafstandAdres,
    AfvalLoopafstandBag, AfvalvulgraadSidcon, Afvalweging,
    MeldingMijnAmsterdam, MeldingOpenbareRuimte,
    Buurt, Stadsdeel, Wijk, Winkelgebied, OpenbareRuimte, Nummeraanduiding,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 Chrome/92.0 Safari/537.36',
    'Accept-CRS': 'EPSG:28992',
}


def make_session(headers: Optional[dict[str, str]] = None) -> requests.Session:
    session = requests.Session()
    session.headers.update(headers or DEFAULT_HEADERS)
    return session


class API:
    def __init__(self, session: Optional[requests.Session] = None) -> None:
        def endpoint(path: str, model: Type[Model]) -> Endpoint[Model]:
            return Endpoint(f'{root}{path}', model, session)

        self.session = session = session or make_session()

        root = 'https://api.data.amsterdam.nl/v1'

        # Huishoudelijk afval
        # -------------------
        self.afval_bijplaatsingen = endpoint(
            '/huishoudelijkafval/bijplaatsingen/',
            Afvalbijplaatsing
        )
        self.afval_clusters = endpoint(
            '/huishoudelijkafval/cluster/',
            Afvalcluster
        )
        self.afval_clusterfracties = endpoint(
            '/huishoudelijkafval/clusterfractie/',
            Afvalclusterfractie
        )
        self.afval_containerlocaties = endpoint(
            '/huishoudelijkafval/containerlocatie/',
            Afvalcontainerlocatie
        )
        self.afval_containers = endpoint(
            '/huishoudelijkafval/container/',
            Afvalcontainer
        )
        self.afval_containertypes = endpoint(
            '/huishoudelijkafval/containertype/',
            Afvalcontainertype
        )
        self.afval_vulgraad_sidcon = EndpointV0(
            'https://api.data.amsterdam.nl/afval/suppliers/sidcon/filllevels/',
            AfvalvulgraadSidcon,
            session
        )
        self.afval_wegingen = endpoint(
            '/huishoudelijkafval/weging/',
            Afvalweging
        )

        # Loopafstanden
        self.afval_loopafstanden_adres = endpoint(
            '/huishoudelijkafval/adres_loopafstand/',
            AfvalLoopafstandAdres
        )
        self.afval_loopafstanden_bag = endpoint(
            '/huishoudelijkafval/bag_object_loopafstand/',
            AfvalLoopafstandBag
        )

        # BAG
        self.nummeraanduidingen = endpoint(
            '/bag/nummeraanduidingen/',
            Nummeraanduiding
        )
        self.openbare_ruimtes = endpoint(
            '/bag/openbareruimtes/',
            OpenbareRuimte
        )

        # Meldingen
        # ---------
        self.meldingen = endpoint(
            '/meldingen/meldingen/',
            MeldingOpenbareRuimte
        )
        self.meldingen_buurt = endpoint(
            '/meldingen/meldingen_buurt/',
            MeldingMijnAmsterdam
        )

        # Gebieden
        # --------
        self.buurten = endpoint(
            '/gebieden/buurten/',
            Buurt
        )
        self.stadsdelen = endpoint(
            '/gebieden/stadsdelen/',
            Stadsdeel
        )
        self.wijken = endpoint(
            '/gebieden/wijken/',
            Wijk
        )

        # Winkelgebieden
        # --------------
        self.winkelgebieden = endpoint(
            '/winkelgebieden/winkelgebieden/',
            Winkelgebied
        )


class Endpoint(Generic[Model]):
    def __init__(self, url: str, item_type: Type[Model],
                 session: requests.Session) -> None:
        """Creates the endpoint interface fetching item_types from url.

        :param url: The endpoint URL. It is a full URL.
        :param item_type: The type of items this endpoint returns.
        :param session: The session to use for communication.
        """
        self.url = url
        self.model = item_type
        self.parse_feature = model_parser(item_type)
        self.session = session

    def __call__(self, **params) -> Iterator[Model]:
        """Convenient shorthand for `.all(...)`.
        """
        return self.all(**params)

    def all(self, **params) -> Iterator[Model]:
        """Iterates over all records in the endpoint.

        :param params: Keyword arguments to refine your query.
        :return: Iterator over all records in the endpoint.
        """
        session = self.session
        parse_feature = self.parse_feature

        params['_format'] = 'geojson'
        url = f'{self.url}?{urlencode(params)}'

        while url:
            logger.info(url)

            # May raise requests.HTTPError
            with session.get(url) as res:
                res.raise_for_status()
                json = orjson.loads(res.content)

            url = next((x['href'] for x in json['_links']
                        if x['rel'] == 'next'), None)

            if 'crs' in json:
                logger.debug(json['crs'])

            for feature in json['features']:
                yield parse_feature(feature)

    def count(self, **params) -> int:
        """Returns the number of records that match the query.

        :param params: Keyword arguments to refine the query.
        :return: The total number of matching records.
        """
        params['_count'] = 'true'
        params['_format'] = 'json'  # geojson heeft geen count.
        params['_pageSize'] = '1'
        url = f'{self.url}?{urlencode(params)}'
        session = self.session

        logger.info(url)

        with session.get(url) as res:
            res.raise_for_status()
            json = orjson.loads(res.content)

        return json['page']['totalElements']

    def one(self, id: Any, **params) -> Model:
        """Fetches a single record from the endpoint.

        :param id: The resource ID.
        :return: The resource.
        """
        session = self.session
        parse_feature = self.parse_feature

        params['_format'] = 'geojson'
        url = f'{self.url}{id}/?{urlencode(params)}'

        logger.info(url)

        with session.get(url) as res:
            res.raise_for_status()
            json = orjson.loads(res.content)

        if 'crs' in json:
            logger.debug(json['crs'])

        return parse_feature(json)


class EndpointV0(Endpoint):
    """Verouderd endpoint. Ondersteuning voor waar de nieuwe API nog niet
    beschikbaar is.
    """
    def __init__(self, url: str, item_type: Type[Model],
                 *args, **kwargs) -> None:
        super().__init__(url, item_type, *args, **kwargs)
        self.parse_feature = model_parser_v0(item_type)

    def all(self, **params) -> Iterator[Model]:
        """Iterates over all records in the endpoint.

        :param params: Keyword arguments to refine your query.
        :return: Iterator over all records in the endpoint.
        """
        session = self.session
        parse_feature = self.parse_feature

        params['format'] = 'json'
        url = f'{self.url}?{urlencode(params)}'

        while url:
            logger.info(url)

            # May raise requests.HTTPError
            with session.get(url) as res:
                res.raise_for_status()
                json = orjson.loads(res.content)

            url = json['_links']['next']['href']

            for feature in json['results']:
                yield parse_feature(feature)

    def count(self, **params) -> int:
        """Returns the number of records that match the query.

        :param params: Keyword arguments to refine the query.
        :return: The total number of matching records.
        """
        raise NotImplementedError('API v0 does not support count.')

    def one(self, id: Any, **params) -> Model:
        """Fetches a single record from the endpoint.

        :param id: The resource ID.
        :return: The resource.
        """
        session = self.session
        parse_feature = self.parse_feature

        params['format'] = 'json'
        url = f'{self.url}{id}/?{urlencode(params)}'

        logger.info(url)

        with session.get(url) as res:
            res.raise_for_status()
            json = orjson.loads(res.content)

        return parse_feature(json)
