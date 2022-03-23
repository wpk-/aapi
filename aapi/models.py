from datetime import date, datetime, time
from typing import Any, NamedTuple, TypeVar

JSON = dict[str, Any]

Point = tuple[float, float]
Polygon = list[Point]
Multipolygon = list[Polygon]

# Model = TypeVar('Model', ...) is defined at the end of this file.


class Afvalbijplaatsing(NamedTuple):
    id: str                                 # "000G65rgtyhFoTOgL0R3"
    datumTijdWaarneming: datetime           # "2021-07-15T13:28:38"
    clusterId: str                          # "123526.357|489156.517"
    gbdBuurtId: str                         # "03630000000645"
    bagOpenbareruimteId: str                # "0363300000004297"
    bagNummeraanduidingId: str              # "0363200000201634"
    bagVerblijfsobjectId: str               # "0363010000741030"
    geometrie: Point                        # {...}
    bruingoed: bool                         # false
    containervies: bool                     # false
    crowScore: str                          # "A"
    glas: bool                              # false
    glasgestremd: bool                      # false
    glastoegankelijk: bool                  # false
    glasvol: bool                           # false
    grof: bool                              # false
    handhaving: bool                        # false
    waardeHandhaving: str                   # "0"
    huisvuil: bool                          # false
    karton: bool                            # false
    overig: bool                            # false
    papiervol: bool                         # false
    papiergestremd: bool                    # false
    papiertoegankelijk: bool                # false
    restgestremd: bool                      # false
    resttoegankelijk: bool                  # true
    restvol: bool                           # false
    veegvuil: bool                          # false
    zwerfafval: bool                        # false
    waarnemerRol: str                       # "Werkbrigade"


class Afvalcluster(NamedTuple):
    id: str                                 # "112739.485|487842.301"
    subclusterIndicatie: bool               # false
    geometrie: Point                        # {...}
    datumOpvoer: datetime                   # "2021-12-20T19:24:10.125375"
    datumOntstaan: date                     # "2019-08-22"
    datumEinde: date                        # "2021-05-26"
    wijzigingsdatumDp: datetime             # "2021-12-20T19:25:23.623280"
    verwijderdDp: bool                      # false
    status: int                             # 1
    bagHoofdadresVerblijfsobjectId: str     # "0363010001036106"
    gbdBuurtId: str                         # "3630000000441"
    bagOpenbareruimteId: str                # "0363300000002365"
    bagNummeraanduidingId: str              # "0363200000520747"


class Afvalclusterfractie(NamedTuple):
    id: str                                 # "[112740.024|487843.078][1]"
    clusterId: str                          # "112740.024|487843.078"
    aantalContainers: int                   # 0
    volumeM3: float                         # 3.5
    code: str                               # "1"
    omschrijving: str                       # "Rest"
    datumOpvoer: datetime                   # "2020-01-28T15:15:20.500395"
    datumEinde: date                        # "2021-12-20"
    wijzigingsdatumDp: datetime             # "2021-12-21T20:51:57.731003"
    verwijderdDp: bool                      # true


class Afvalcontainer(NamedTuple):
    id: str                                 # "10000"
    idNummer: str                           # "PA 6225"
    serienummer: str                        # "BAO01402"
    clusterId: str                          # "123645.153|485465.699"
    eigenaarId: str                         # "184"
    eigenaarNaam: str                       # "Amsterdam Dump Locatie"
    status: int                             # 0
    fractieCode: str                        # "3"
    fractieOmschrijving: str                # "Papier"
    datumCreatie: date                      # "2012-03-29"
    datumPlaatsing: date                    # "2012-03-28"
    datumOperationeel: date                 # "2012-03-28"
    datumAflopenGarantie: date              # "2013-03-28"
    datumOplevering: date                   # "2012-03-28"
    wijzigingsdatumDp: datetime             # "2021-05-05T19:46:35.035150"
    verwijderdDp: bool                      # false
    geadopteerdInd: bool                    # false
    locatieId: str                          # "9999"
    geometrie: Point                        # {...}
    typeId: str                             # "3137"
    bagHoofdadresVerblijfsobjectId: str     # "0363010000946581"
    gbdBuurtId: str                         # "03630000000756"
    bagOpenbareruimteId: str                # "0363300000004575"
    bagNummeraanduidingId: str              # "0363200000439941"
    containerRalKleurNaam: str              # "Fir green",
    containerRalKleurCode: str              # "6009"
    containerRalKleurHexcode: str           # "31372B"
    containerChipNummber: str               # null
    containerUnitCardLezerId: str           # "Proefsensor geplaatst . Abel..."
    containerKleur: str                     # "Dennengroen (RAL 6009)"
    containerMark: int                      # 10
    containerDatumVervanging: date          # "2022-03-29"
    containerDatumWijziging: datetime       # "2018-07-01T00:00:00"
    containerEndOfLife: date                # "2021-04-13"
    containerEigenaarschap: str             # "Eigendom"
    containerEigenaarschapOpmerking: str    # "Container is in ..."
    containerOpmerking: str                 # "komt van Krugerplein ..."


class Afvalcontainerlocatie(NamedTuple):
    id: str                                 # "10001"
    serienummer: str                        # "WLBAO01403"
    status: int                             # 0
    geometrie: Point                        # {...}
    eigenaarId: str                         # "184"
    eigenaarNaam: str                       # "Amsterdam Dump Locatie"
    datumCreatie: date                      # "2012-03-29"
    datumPlaatsing: date                    # "2019-04-01"
    datumOperationeel: date                 # "2019-04-01"
    datumOplevering: date                   # "2012-03-28"
    wijzigingsdatumDp: datetime             # "2021-05-05T19:46:25.415126"
    verwijderdDp: bool                      # false
    datumEindeGarantie: date                # "0002-11-29"      !!!
    indBevatContainer: bool                 # true
    bagHoofdadresVerblijfsobjectId: str     # "0363010000946581"
    gbdBuurtId: str                         # "03630000000770"
    bagOpenbareruimteId: str                # "0363300000004575"
    bagNummeraanduidingId: str              # "0363200000439941"
    containerlocatieTypeNaam: str           # "ONBEKEND VOLUME - GEEN"
    containerlocatieIdNummer: str           # "WLP004"
    containerlocatieDatumWijziging: datetime        # "2017-09-28T10:30:08"
    containerlocatieOpmerking: str          # "(Oude opgeslagen adres: ..."
    containerlocatieEndOfLife: date         # "2021-04-20"
    containerlocatieEigenaarschap: str      # "Eigendom"
    containerlocatieEigenaarschapOpmerking: str     # "Container is in ..."
    containerlocatieTypeArtikelcode: str    # "P000022"


class Afvalcontainertype(NamedTuple):
    id: str                                 # "109"
    naam: str                               # "nieuw-West Glas 1 4m3 KH ..."
    volumeM3: float                         # 3.5
    gewichtKg: int                          # 600
    wijzigingsdatumDp: datetime             # "2021-04-07T09:48:28.058193"
    verwijderdDp: bool                      # false
    containertypeArtikelcode: str           # "549598"
    containertypeHijskraantypeNaam: str     # "Kinshofer"
    containertypeHijskraanOpmerking: str    # "KH"
    containertypeContainerType: str         # "UNDERGROUND"
    containertypeCompressieContainerInd: bool   # false
    containertypeCompressiefactor: str      # "2.50"


class AfvalvulgraadSidcon(NamedTuple):
    filling: int                            # 6
    communication_date_time: datetime       # 2022-03-17T15:19:04.960000Z
    id: int                                 # 11026789
    container_id: str                       # "REA00252"
    short_id: str                           # null


class Afvalweging(NamedTuple):
    id: str                                 # "10000~2017-02-17~09:12:03~26"
    clusterId: str                          # "128920.051|484940.826"
    clusterSubclusterIndicatie: bool        # false
    weegsysteemId: int                      # 26
    weegsysteemOmschrijving: str            # "O 26"
    volgnummer: int                         # 10000
    datumWeging: date                       # "2017-02-17"
    tijdstipWeging: time                    # "09:12:03"
    locatienummer: str                      # "0"
    fractieCode: int                        # 1
    fractieOmschrijving: str                # "Rest"
    eersteWeging: int                       # 820
    tweedeWeging: int                       # 745
    nettoGewicht: int                       # 75
    geometrie: Point                        # {...}
    bedieningCode: int                      # 0
    bedieningOmschrijving: str              # "Hand"
    wijzigingsdatumDp: datetime             # "2021-12-20T19:43:39.327944"
    verwijderdDp: bool                      # false
    bagHoofdadresVerblijfsobjectId: str     # "0363010000911073"
    gbdBuurtId: str                         # "03630000000603"
    bagOpenbareruimteId: str                # "0363300000006097"
    bagNummeraanduidingId: str              # "0363200000368382"


class Buurt(NamedTuple):
    registratiedatum: datetime              # "2021-05-27T13:15:21"
    naam: str                               # "Dichtersbuurt Weesp"
    code: str                               # "SAC1"
    beginGeldigheid: datetime               # "2021-04-07T00:00:00"
    eindGeldigheid: datetime                # null
    documentdatum: date                     # "2021-05-01"
    documentnummer: str                     # "Tijdelijk besluit Weesp 2021"
    cbsCode: str                            # "BU04570201"
    geometrie: Multipolygon                 # {...}
    id: str                                 # "03630980000006.1"


class MeldingOpenbareRuimte(NamedTuple):
    id: str                                 # "SIA-1000"
    hoofdcategorie: str                     # "Wegen, verkeer, straatmeubilair"
    subcategorie: str                       # "Prullenbak is kapot"
    datumMelding: date                      # "2018-08-09"
    tijdstipMelding: time                   # "09:52:36"
    datumOverlast: date                     # "2018-08-09"
    tijdstipOverlast: time                  # "09:52:36"
    meldingType: str                        # "SIG"
    meldingSoort: str                       # "standaard"
    meldingsnummerBovenliggend: str         # "SIA-999894"
    gbdBuurtCode: str                       # "A04g"
    gbdBuurtNaam: str                       # "Valkenburg"
    gbdWijkCode: str                        # "A04"
    gbdWijkNaam: str                        # "Nieuwmarkt/Lastage"
    gbdGgwgebiedCode: str                   # "DX02"
    gbdGgwgebiedNaam: str                   # "Centrum-Oost"
    gbdStadsdeelCode: str                   # "A"
    gbdStadsdeelNaam: str                   # "Centrum"
    bagWoonplaatsNaam: str                  # "Amsterdam"
    bron: str                               # "SIA"
    laatstGezienBron: datetime              # "2022-03-07T04:21:37"


class Stadsdeel(NamedTuple):
    registratiedatum: datetime              # "2021-05-27T13:15:21"
    naam: str                               # "Weesp"
    code: str                               # "S"
    beginGeldigheid: datetime               # "2021-04-07T00:00:00"
    eindGeldigheid: datetime                # null
    documentdatum: date                     # "2021-05-01"
    documentnummer: str                     # "Tijdelijk besluit Weesp 2021"
    geometrie: Multipolygon                 # {...}
    id: str                                 # "03630930000000.1"


class Wijk(NamedTuple):
    registratiedatum: datetime              # "2021-05-27T13:15:21"
    naam: str                               # "Oostelijke Vechtoever"
    code: str                               # "SAG"
    beginGeldigheid: datetime               # "2021-04-07T00:00:00"
    eindGeldigheid: datetime                # null
    documentdatum: date                     # "2021-05-01"
    documentnummer: str                     # "Tijdelijk besluit Weesp 2021"
    cbsCode: str                            # "WK045708"
    geometrie: Multipolygon                 # {...}
    id: str                                 # "03630970000006.1


class Winkelgebied(NamedTuple):
    id: int                                 # 1
    geometry: Multipolygon                  # {...}
    gebiedscode: str                        # "A2"
    gebiedsnaam: str                        # "Haarlemmerstraat/Haarlemmerdijk"
    code: str                               # "A2"
    oppervlakte: float                      # 3.63
    winkelgebiedcode: str                   # "001"
    concentratiegebiedcode: str             # "X4"
    concentratiegebiednaam: str             # "Haarlemmerstraat/dijk"
    wijk: str                               # "A05"
    gebied: str                             # "DX01"
    categorie: str                          # "K"
    categorienaam: str                      # "Kernwinkelgebied"


Model = TypeVar(
    'Model',
    Afvalbijplaatsing, Afvalcluster, Afvalclusterfractie, Afvalcontainer,
    Afvalcontainerlocatie, Afvalcontainertype, AfvalvulgraadSidcon,
    Afvalweging, Buurt, MeldingOpenbareRuimte, Stadsdeel, Wijk, Winkelgebied,
)
