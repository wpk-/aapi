import logging
from typing import Optional, Generic, Type, Iterator, Any
from urllib.parse import urlencode

import orjson as orjson
import requests as requests

from aapi.geojson import model_parser
from aapi.models import (
    Model,
    Afvalbijplaatsing, Afvalcluster, Afvalclusterfractie, Afvalcontainer,
    Afvalcontainerlocatie, Afvalcontainertype, Afvalweging,
    Buurt, MeldingOpenbareRuimte, Stadsdeel, Wijk, Winkelgebied
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36'
                  ' Chrome/92.0 Safari/537.36',
    'Accept-CRS': 'EPSG:28992',
}


class API:
    def __init__(self, headers: Optional[dict[str, str]] = None) -> None:
        session = requests.Session()
        if not headers:
            headers = DEFAULT_HEADERS
        session.headers.update(headers)
        self.session = session

        root = 'https://api.data.amsterdam.nl/v1'

        self.afval_bijplaatsingen = Endpoint(
            f'{root}/huishoudelijkafval/bijplaatsingen/',
            Afvalbijplaatsing, session)
        self.afval_clusters = Endpoint(
            f'{root}/huishoudelijkafval/cluster/', Afvalcluster, session)
        self.afval_clusterfracties = Endpoint(
            f'{root}/huishoudelijkafval/clusterfractie/',
            Afvalclusterfractie, session)
        self.afval_containerlocaties = Endpoint(
            f'{root}/huishoudelijkafval/containerlocatie/',
            Afvalcontainerlocatie, session)
        self.afval_containers = Endpoint(
            f'{root}/huishoudelijkafval/container/', Afvalcontainer, session)
        self.afval_containerlocaties = Endpoint(
            f'{root}/huishoudelijkafval/containertype/',
            Afvalcontainertype, session)
        self.afval_wegingen = Endpoint(
            f'{root}/huishoudelijkafval/weging/', Afvalweging, session)

        self.meldingen = Endpoint(
            f'{root}/meldingen/meldingen/', MeldingOpenbareRuimte, session)

        self.buurten = Endpoint(f'{root}/gebieden/buurten/', Buurt, session)
        self.stadsdelen = Endpoint(
            f'{root}/gebieden/stadsdelen/', Stadsdeel, session)
        self.wijken = Endpoint(f'{root}/gebieden/wijken/', Wijk, session)
        self.winkelgebieden = Endpoint(
            f'{root}/winkelgebieden/winkelgebieden/', Winkelgebied, session)


class Endpoint(Generic[Model]):
    def __init__(self, url: str, item_type: Type[Model],
                 session: requests.Session) -> None:
        """Creates the endpoint interface fetching item_types from url.

        :param url: The endpoint URL. It is a full URL.
        :param item_type: The type of items this endpoint returns.
        :param session: The session to use for communication.
        """
        self.url = url
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
