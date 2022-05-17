from typing import Optional

import requests as requests

DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 Chrome/92.0 Safari/537.36',
    'Accept-CRS': 'EPSG:28992',
}


def make_session(headers: Optional[dict[str, str]] = None) -> requests.Session:
    session = requests.Session()
    session.headers.update(headers or DEFAULT_HEADERS)
    return session
