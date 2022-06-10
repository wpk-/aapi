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


class AfvalLoopafstandAdres(NamedTuple):
    id: str                                 # "0363010000543293~036...06111~1"
    adresseerbaarobjectId: str              # "0363010000543293"
    adresseerbaarobjectType: str            # "Verblijfsobject"
    nummeraanduidingId: str                 # "0363200000006111"
    gebruiksdoel: str                       # "woonfunctie"
    clusterId: str                          # "120268.662|487891.656"
    fractie: str                            # "1"
    fractieOmschrijving: str                # "Rest"
    loopafstandCategorieId: str             # "1~10"
    loopafstand: float                      # 584.59
    geometrie: Point                        # {...}
    wijzigingsdatumDp: datetime             # "2021-08-14T19:24:44.989071"
    verwijderdDp: bool                      # false


class AfvalLoopafstandBag(NamedTuple):
    id: str                                 # "0363020000676358~5"
    bagObjectId: str                        # "0363020000676358"
    bagObjectType: str                      # "ligplaats"
    clusterId: str                          # "118811.815|484374.131"
    fractie: str                            # "5"
    fractieOmschrijving: str                # "Textiel"
    loopafstandCategorieId: str             # "5~10"
    loopafstand: float                      # 1315.43
    geometrie: Multipolygon                 # {...}
    wijzigingsdatumDp: datetime             # "2021-03-13T19:33:23.809982"
    verwijderdDp: bool                      # false


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


class Ligplaats(NamedTuple):
    registratiedatum: datetime              # "2022-06-08T13:18:54",
    geconstateerd: bool                     # false,
    statusCode: int                         # 1,
    statusOmschrijving: str                 # "Plaats aangewezen",
    heeftHoofdadresId: str                  # "0363200013028201",
    geometrie: Multipolygon                 # {"type": "Polygon", ...},
    beginGeldigheid: datetime               # "2022-06-08T00:00:00",
    eindGeldigheid: datetime                # null,
    documentdatum: date                     # "2022-06-08",
    documentnummer: str                     # "SM00001773",
    ligtInBuurtId: str                      # "03630980000356",
    heeftDossierId: str                     # null,
    bagprocesCode: int                      # 118,
    bagprocesOmschrijving: str              # "Benoemen ligplaats",
    id: str                                 # "0363020012500205.3",
    gebruiksdoel: str                       # [{"omschrijving": "woonfunctie"}, ...]


class MeldingMijnAmsterdam(NamedTuple):
    id: int                                 # 34054
    categorie: str                          # "overlast-bedrijven-en-horeca"
    subcategorie: str                       # "overig-horecabedrijven"
    status: str                             # "In behandeling"
    datumCreatie: datetime                  # "2018-09-30T15:00:22.814031"
    datumWijziging: datetime                # "2021-03-24T10:38:45.977122"
    geometrie: Point                        # {}
    geometrieVisualisatie: Point            # {}


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


class Nummeraanduiding(NamedTuple):
    registratiedatum: datetime              # "2010-10-26T06:19:08"
    huisnummer: int                         # 20
    geconstateerd: bool                     # false
    huisletter: str                         # null
    huisnummertoevoeging: str               # null
    postcode: str                           # "1067TK"
    ligtInWoonplaatsId: str                 # "3594"
    beginGeldigheid: datetime               # "2006-01-03T00:00:00"
    eindGeldigheid: datetime                # null
    ligtAanOpenbareruimteId: str            # "0363300000004610"
    typeAdresseerbaarObjectCode: int        # 1
    typeAdresseerbaarObjectOmschrijving: str   # "Verblijfsobject"
    documentdatum: date                     # "2006-01-03"
    documentnummer: str                     # "GV00000403"
    statusCode: int                         # 1
    statusOmschrijving: str                 # "Naamgeving uitgegeven"
    typeAdres: str                          # "Hoofdadres"
    adresseertVerblijfsobjectId: str        # "0363010001036106"
    adresseertLigplaatsId: str              # null
    adresseertStandplaatsId: str            # null
    heeftDossierId: str                     # "GV00000403"
    bagprocesCode: int                      # 143
    bagprocesOmschrijving: str              # "Splitsen verblijfsobject"
    id: str                                 # "0363200000520747.3"


class OpenbareRuimte(NamedTuple):
    registratiedatum: datetime              # "2019-06-28T19:28:27"
    straatcode: str                         # "31496"
    straatnaamPtt: str                      # "RUBENSSTR"
    statusCode: int                         # 1
    statusOmschrijving: str                 # "Naamgeving uitgegeven"
    beginGeldigheid: datetime               # "2014-01-10T00:00:00"
    eindGeldigheid: datetime                # null
    geconstateerd: bool                     # false
    typeCode: int                           # 1
    typeOmschrijving: str                   # "Weg"
    documentdatum: date                     # "2014-01-10"
    documentnummer: str                     # "GV00001729_AC00AC"
    naam: str                               # "Rubensstraat"
    naamNen: str                            # "Rubensstraat"
    ligtInWoonplaatsId: str                 # "3594"
    beschrijvingNaam: str                   # "Petrus Paulus Rubens ..."
    heeftDossierId: str                     # "GV00001729"
    bagprocesCode: int                      # 122
    bagprocesOmschrijving: str              # "Benoemen openbare ruimte"
    geometrie: Multipolygon                 # {"type": "MultiPolygon", ...}
    id: str                                 # "0363300000004427.8"


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


class Standplaats(NamedTuple):
    registratiedatum: datetime              # "2022-04-01T14:14:09"
    geconstateerd: bool                     # true
    statusCode: int                         # 1
    statusOmschrijving: str                 # "Plaats aangewezen"
    heeftHoofdadresId: str                  # "0363200013025651"
    geometrie: Multipolygon                 # {"type": "Polygon", ...}
    beginGeldigheid: datetime               # "2022-04-01T00:00:00"
    eindGeldigheid: datetime                # null
    documentdatum: date                     # "2022-04-01"
    documentnummer: str                     # "TM22030911_TM00TM"
    ligtInBuurtId: str                      # "03630980000173"
    heeftDossierId: str                     # "TM22030911"
    bagprocesCode: int                      # 130
    bagprocesOmschrijving: str              # "Constatering nieuw object"
    id: str                                 # "0363030012500050.3"
    gebruiksdoel: str                       # [{"omschrijving": "Woonfunctie"}, ...]


class Verblijfsobject(NamedTuple):
    id: str                                 # "0363010000749418.9"
    registratiedatum: datetime              # "2022-04-26T15:57:06"
    cbsNummer: str                          # "302570"
    indicatieWoningvoorraad: str            # "N"
    financieringscodeCode: int              # 500
    financieringscodeOmschrijving: str      # "Ongesubsidieerde bouw (500)"
    geconstateerd: bool                     # false
    heeftHoofdadresId: str                  # "0363200000210020"
    geometrie: Point                        # {"type": "Point", ...}
    oppervlakte: int                        # 70
    statusCode: int                         # 7
    statusOmschrijving: str                 # "Verbouwing verblijfsobject"
    beginGeldigheid: datetime               # "2022-04-26T00:00:00"
    eindGeldigheid: datetime                # "2047-08-03T00:00:00"
    documentdatum: date                     # "2022-04-26"
    documentnummer: str                     # "SA06302917"
    gebruiksdoelWoonfunctieCode: int        # 2085
    gebruiksdoelWoonfunctieOmschrijving: str                # "Complex, ..."
    gebruiksdoelGezondheidszorgfunctieCode: int             # 2330
    gebruiksdoelGezondheidszorgfunctieOmschrijving: str     # "Complex, ..."
    aantalEenhedenComplex: int              # 4
    verdiepingToegang: int                  # 3
    aantalBouwlagen: int                    # 2
    hoogsteBouwlaag: int                    # 4
    laagsteBouwlaag: int                    # 3
    aantalKamers: int                       # 5
    eigendomsverhoudingCode: int            # 1
    eigendomsverhoudingOmschrijving: str    # "Huur"
    feitelijkGebruikCode: int               # 3113
    feitelijkGebruikOmschrijving: str       # "toonzaal"
    redenopvoerCode: int                    # 27
    redenopvoerOmschrijving: str            # "Verbouw in vergunningsfase"
    redenafvoerCode: int                    # 49
    redenafvoerOmschrijving: str            # "Correctie afvoer"
    ligtInBuurtId: str                      # "03630980000051"
    heeftDossierId: str                     # "SA06302917"
    bagprocesCode: int                      # 111
    bagprocesOmschrijving: str              # "Kleine verbouwing object"
    gebruiksdoel: str                       # [{"code": "5", "omschrijving": "industriefunctie"}, ...]
    toegang: str                            # [{"code": "8", "omschrijving": "Begane grond"}, ...]
    # @TODO: lijst van dicts als type.


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
    Afvalcontainerlocatie, Afvalcontainertype, AfvalLoopafstandAdres,
    AfvalLoopafstandBag, AfvalvulgraadSidcon, Afvalweging, Buurt, Ligplaats,
    MeldingMijnAmsterdam, MeldingOpenbareRuimte, Nummeraanduiding,
    OpenbareRuimte, Stadsdeel, Standplaats, Verblijfsobject, Wijk,
    Winkelgebied,
)
