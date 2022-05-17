"""
Gebruik als volgt:

    from aapi.geojson import API

    api = API()

    for melding in api.containers.all(status=1, verwijderdDp=False, ...):
        ...
"""
from aapi.geojson.endpoints import *
