aapi
----

Een typed interface voor de data API van de Gemeente Amsterdam.


## Install

Installeer de dependencies ([orjson][orjson] en [requests][requests]):
```sh
pip install -r requirements.txt
```


## Gebruik

```python
from aapi import API

api = API()

# Een iterator over alle winkelgebieden.
wg = next(api.winkelgebieden.all())
print(wg)
# Winkelgebied(id=1, geometry=[[...]], gebiedscode='A2', gebiedsnaam='Haarlemmerstraat/Haarlemmerdijk', code='A2', ...)

# Met `.all()` is het vaak veiliger om een `_pageSize` op te geven.
aw = next(api.afval_wegingen.all(_pageSize=10, _sort='-datumWeging'))
print(aw)
# Afvalweging(id='10000~2017-02-17~09:12:03~26', clusterId='128920.051|484940.826', clusterSubclusterIndicatie=False, ...)

# Er is ook `.one()`.
ac = api.afval_containers.one('102125')
print(ac)
# Afvalcontainer(id='102125', idNummer='GLA00034', serienummer='HBD2.0161574', clusterId='123143.185|487652.743', ...)

# Gebruik try/catch om HTTP fouten op te vangen.
from requests.exceptions import HTTPError
try:
    api.afval_containers.one('$$$')
except HTTPError as err:
    print('Container niet gevonden.')
    print(err)
# Container niet gevonden.
# 404 Client Error: Not Found for url: https://api.data.amsterdam.nl/v1/huishoudelijkafval/container/$$$/?_format=geojson
```

Het kan ook gebeuren dat een call `api.all()` netjes itereert maar op een keer
toch een `HTTPError` geeft. Bijvoorbeeld als de volgende pagina een time-out
geeft. Houd hier rekening mee.

Voor een overzicht van alle ondersteunde endpoints zie
[models.py](aapi/models.py). Pull requests zijn welkom!


## Licentie

[MIT](LICENSE)


[orjson]: https://github.com/ijl/orjson
[requests]: https://docs.python-requests.org/
