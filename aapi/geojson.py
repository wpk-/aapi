from collections.abc import Callable, Sequence
from datetime import date, datetime, time
from typing import Optional, Type, TypeVar

from aapi.models import JSON, Model, Multipolygon, Point, Polygon

Geom = TypeVar('Geom', Point, Polygon, Multipolygon)
T = TypeVar('T')


def _identity(v: T) -> T:
    return v


def parse_point(xy: tuple[float, float]) -> Point:
    x, y = xy
    return round(float(x), 8), round(float(y), 8)


def parse_polygon(coords: Sequence[tuple[float, float]]) -> Polygon:
    return [parse_point(xy) for xy in coords]


def parse_multipolygon(coords: Sequence[Sequence[tuple[float, float]]]
                       ) -> Multipolygon:
    try:
        return [[parse_point(xy) for xy in poly] for poly in coords]
    except ValueError:
        # Workaround bug in API data.
        assert all(len(poly) == 1 for poly in coords)
        return [[parse_point(xy) for xy in poly[0]] for poly in coords]


def from_field(fld: str, constructor: Callable[..., Geom]
               ) -> Callable[[JSON], Geom]:
    """Returns a function `f(obj) -> constructor(obj[fld])`.

    Because the API sometimes returns very unexpected results, the method
    first checks that the incoming value is actually a dict. If so, it
    applies the constructor. Otherwise it returns the incoming value
    directly.

    :param fld: Name of the field in the JSON object to which apply the
        constructor.
    :param constructor: The constructor to be applied to the field value.
    :return: A function that computes `constructor(obj[fld])`.
    """
    def parse(value: JSON) -> Geom:
        try:
            value = value[fld]
        except TypeError:
            # The value is probably a str.
            return value
        return constructor(value)
    return parse


def model_parser(model: Type[Model], geometry_field: Optional[str] = None
                 ) -> Callable[[JSON], Model]:
    """Returns a function that parses GeoJSON features to model instances.

    :param model: The model type.
    :param geometry_field: If the GeoJSON feature contains geometry, use
        `geometry_field` to specify the name of the field (in the model)
        to store the geometry under. If the GeoJSON has no geometry then
        leave this field empty (None).
        Defaults to the first field in `model` of type Point, Polygon or
        Multipolygon.
    :return: A function `f(feature) -> model(**feature)`.
    """
    def parse(feature: JSON) -> Model:
        """Parses a GeoJSON feature object. Returns a model instance.

        :param feature: A JSON object with 'type': 'feature'. It has
            'properties' and possibly a 'crs' and 'geometry'.
        :return: The model instance.
        """
        props = feature['properties']
        if geometry_field and 'geometry' in feature:
            props[geometry_field] = feature['geometry']
        return model(**{fld: parser(props[fld])
                        if props.get(fld, None) else None
                        for fld, parser in field_methods})

    type_methods = {
        date: date.fromisoformat,
        datetime: datetime.fromisoformat,
        time: time.fromisoformat,
        Point: from_field('coordinates', parse_point),
        Polygon: from_field('coordinates', parse_polygon),
        Multipolygon: from_field('coordinates', parse_multipolygon),
    }

    field_methods = [
        (fld, type_methods.get(typ, _identity))
        for fld, typ in model.__annotations__.items()
    ]

    if geometry_field is None:
        geometry_field = next((
            fld for fld, typ in model.__annotations__.items()
            if typ in (Point, Polygon, Multipolygon)
        ), None)

    return parse


def parse_feature(feature: JSON, model: Type[Model],
                  geometry_field: Optional[str] = None) -> Model:
    """Parses a GeoJSON feature object. Returns a model instance.

    :param feature: A JSON object with 'type': 'feature'. It has
        'properties' and possibly a 'crs' and 'geometry'.
    :param model: The model class which to parse the feature into.
    :param geometry_field: The name of the geometry field in the model.
    :return: The model instance.
    """
    def coord(xy: tuple[float, float]) -> Point:
        x, y = xy
        return round(float(x), 8), round(float(y), 8)

    def geom(val: JSON, typ: Type[Geom]) -> Geom:
        try:
            val = val['coordinates']
        except TypeError:
            # The value is probably a str.
            return val

        if typ == Point:
            return coord(val)
        elif typ == Polygon:
            return [coord(xy) for xy in val]
        elif typ == Multipolygon:
            try:
                return [[coord(xy) for xy in poly] for poly in val]
            except ValueError:
                # Workaround bug in API data.
                assert all(len(poly) == 1 for poly in val)
                return [[coord(xy) for xy in poly[0]] for poly in val]

        return val

    props = properties(feature, geometry_field)

    return model(**{
        fld: None if fld not in props
        else typ.fromisoformat(props[fld]) if typ in (date, datetime, time)
        else geom(props[fld], typ) if typ in (Point, Polygon, Multipolygon)
        else props[fld]
        for fld, typ in model.__annotations__.items()
    })
