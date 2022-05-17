from aapi.models import Point


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
        x, y = s[i:j].split()
        return round(float(x), 8), round(float(y), 8)
