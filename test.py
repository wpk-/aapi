import logging

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
