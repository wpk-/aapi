"""
aapi.

Een typed interface voor de data API van de Gemeente Amsterdam.

Voor de GeoJSON API:

    from aapi import API
    api = API()
    containers = api.containers(...query kwargs)
    for container in containers:
        ...

Voor de CSV API:

    from aapi.csv import ContainersCsv
    containers = ContainersCsv('cache/containers.csv', {...query args})
    for container in containers:
        ...

"""
__version__ = '0.3.1'
__author__ = 'Paul Koppen'
__credits__ = 'Gemeente Amsterdam'

from aapi.geojson.endpoints import API
