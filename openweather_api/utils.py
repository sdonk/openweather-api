import functools
import gzip
import json
from io import BytesIO
from typing import List
from urllib.parse import urljoin

import requests

from openweather_api.settings import CITY_ID_LIST_URL


def build_full_url(base_url: str, endpoint: str) -> str:
    if not base_url.endswith('/'):
        base_url += '/'
    if endpoint.startswith('/'):
        endpoint = endpoint[1:]

    return urljoin(base_url, endpoint)


@functools.lru_cache()
def load_cities() -> List:
    response = requests.get(CITY_ID_LIST_URL)
    with gzip.open(BytesIO(response.content), 'rb') as f:
        cities = json.loads(f.read())
    return cities
