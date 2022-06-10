import logging
from datetime import date

from aapi import API

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('aapi').setLevel(logging.DEBUG)

    api = API()

    wg = next(api.winkelgebieden.all())
    print(wg)

    aw = next(api.afval_wegingen.all(_pageSize=10))
    print(aw)

    ac = api.afval_containers.one('102125')
    print(ac)

    from requests.exceptions import HTTPError
    try:
        api.afval_containers.one('$$$')
    except HTTPError as err:
        print('Container niet gevonden.')
        print(err)

    b = next(api.buurten())
    print(b)
    assert api.buurten.one(b.id) == b

    nc = api.afval_containers.count(fractieOmschrijving='Rest')
    print(f'Aantal containers voor restafval: {nc}')

    assert api.meldingen.one('SIA-1000097').datumMelding == date(2021, 7, 27)

    av = api.afval_vulgraad_sidcon.all(page_size=1)
    print(next(av))
    print(next(av))

    print(next(api.afval_loopafstanden_bag.all(_pageSize=1)))
    print(api.afval_loopafstanden_adres.count(
        clusterId='123645.153|485465.699', fractieOmschrijving='Rest'))

    print(api.meldingen_buurt.one(34054))

    print(next(api.openbare_ruimtes.all(_pageSize=1)))
    print(next(api.nummeraanduidingen.all(_pageSize=1)))
    print(next(api.verblijfsobjecten.all(_pageSize=1)))
    print(next(api.ligplaatsen.all(_pageSize=1)))
    print(next(api.standplaatsen.all(_pageSize=1)))
