import re

from aapi.models import Point, Polygon, Multipolygon


def parse_bool(s: str) -> bool:
    return {'t': True, 'f': False, '1': True, '0': False, '-': False,
            'j': True, 'n': False}[s[0].lower()]


def parse_float(s: str) -> float:
    return float(s.replace(',', '.'))


def parse_int(s: str) -> int:
    return int(parse_float(s))


def parse_point(s: str) -> Point:
    if s:
        # s = 'SRID=28992;POINT (x y)'
        i = s.index('(') + 1
        j = s.index(')', i)
        x, y = s[i:j].split(',' if ',' in s[i:j] else None)
        return round(float(x), 8), round(float(y), 8)


def parse_multipolygon(s: str) -> Multipolygon:
    # s = 'SRID=28992;POLYGON ((x0 y0, x1 y1, ...), ...)'
    return [
        [
            Point(map(float, pair.split()))
            for pair in poly[1:-1].split(', ')
        ]
        for poly in re.findall(r'\([^(]+\)', s)
    ]
