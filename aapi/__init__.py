"""
aapi.

Een typed interface voor de data API van de Gemeente Amsterdam.
"""
import logging
from typing import Any, Generic, Iterator, Optional, Type
from urllib.parse import urlencode

import orjson as orjson
import requests as requests

from aapi.geojson import parse_feature
from aapi.models import (
    JSON, Point, Polygon, Multipolygon, Model,
    Afvalbijplaatsing, Afvalcluster, Afvalclusterfractie, Afvalcontainer,
    Afvalcontainerlocatie, Afvalcontainertype, Afvalweging,
    Winkelgebied,
)

__version__ = '0.1.0'
__author__ = 'Paul Koppen'
__credits__ = 'Gemeente Amsterdam'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36'
                  ' Chrome/92.0 Safari/537.36',
    'Accept-CRS': 'EPSG:28992',
}


class Endpoint(Generic[Model]):
    def __init__(self, url: str, item_type: Type[Model],
                 session: requests.Session) -> None:
        """Creates the endpoint interface fetching item_types from url.

        :param url: The endpoint URL. It is a full URL.
        :param item_type: The type of items this endpoint returns.
        :param session: The session to use for communication.
        """
        self.url = url
        self.item_type = item_type
        self.session = session

        self.item_geometry_field = next(
            (f for f, t in item_type.__annotations__.items()
             if t in (Point, Polygon, Multipolygon)), None)

    def all(self, **params) -> Iterator[Model]:
        """Iterates over all records in the endpoint.

        :param params: Keyword arguments to refine your query.
        :return: Iterator over all records in the endpoint.
        """
        params['_format'] = 'geojson'
        url = f'{self.url}?{urlencode(params)}'
        session = self.session
        model = self.item_type
        geom_field = self.item_geometry_field

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
                yield parse_feature(feature, model, geom_field)

    def one(self, id: Any) -> Model:
        """Fetches a single record from the endpoint.

        :param id: The resource ID.
        :return: The resource.
        """
        params = {'_format': 'geojson'}
        url = f'{self.url}{id}/?{urlencode(params)}'
        session = self.session
        model = self.item_type
        geom_field = self.item_geometry_field

        logger.info(url)

        with session.get(url) as res:
            res.raise_for_status()
            json = orjson.loads(res.content)

            if 'crs' in json:
                logger.debug(json['crs'])

            return parse_feature(json, model, geom_field)


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

        self.winkelgebieden = Endpoint(
            f'{root}/winkelgebieden/winkelgebieden/', Winkelgebied, session)
