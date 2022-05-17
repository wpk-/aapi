import logging
from typing import Optional, Type

import requests as requests

from aapi.geojson.base import Endpoint, EndpointV0
from aapi.models import (
    Model, Afvalbijplaatsing, Afvalcluster, Afvalclusterfractie,
    Afvalcontainerlocatie, Afvalcontainer, Afvalcontainertype,
    AfvalvulgraadSidcon, Afvalweging, AfvalLoopafstandAdres,
    AfvalLoopafstandBag, Nummeraanduiding, OpenbareRuimte, Verblijfsobject,
    MeldingOpenbareRuimte, MeldingMijnAmsterdam, Buurt, Stadsdeel, Wijk,
    Winkelgebied
)
from aapi.session import make_session

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

__all__ = ['API']


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
        self.verblijfsobjecten = endpoint(
            '/bag/verblijfsobjecten/',
            Verblijfsobject
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
