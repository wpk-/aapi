"""
Gebruik als volgt:

    from aapi.csv import ContainersCsv

    containers = ContainersCsv('cache/containers.csv', {
        'verwijderdDp': False, 'status': 1, ...})

    for container in containers:
        ...
    # Volgende keer wordt containers gelezen van disk.
"""
from aapi.csv.endpoints import *
