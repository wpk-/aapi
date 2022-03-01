from datetime import date, datetime, time
from typing import Optional, Type, TypeVar

from aapi.models import JSON, Model, Multipolygon, Point, Polygon

G = TypeVar('G', Point, Polygon, Multipolygon)


def properties(feature: JSON, geometry_field: Optional[str] = None) -> JSON:
    """Extracts the properties from a feature and attaches the geometry.

    :param feature: JSON object with field 'type': 'feature'. It has
        'properties' and possibly a 'crs' and 'geometry'.
    :param geometry_field: The fieldname under which to store the
        geometry in the returned object.
    :return: A JSON object with all extracted properties and geometry.
        Note: It is still raw JSON. No values are parsed.
    """
    props = feature['properties']
    if geometry_field and 'geometry' in feature:
        props[geometry_field] = feature['geometry']
    return props


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

    def geom(val: JSON, typ: Type[G]) -> G:
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

    for fld, typ in model.__annotations__.items():
        if props.get(fld, None):
            if typ in (date, datetime, time):
                props[fld] = typ.fromisoformat(props[fld])
            elif typ in (Point, Polygon, Multipolygon):
                props[fld] = geom(props[fld], typ)

    return model(**props)
