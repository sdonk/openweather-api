import abc
from typing import Optional

import requests

from openweather_api.settings import API_BASE_URL
from openweather_api.utils import build_full_url


class ClientCore(abc.ABC):

    def __init__(self, api_key: str, base_url: Optional[str] = API_BASE_URL) -> None:
        self.base_url = base_url
        self.api_key = api_key

    def build_params(self, params: Optional[dict] = None):
        params = params if params else {}
        params['appid'] = self.api_key
        return params

    def get(self, endpoint: str, params: Optional[dict] = None) -> requests.Response:
        url = build_full_url(self.base_url, endpoint)
        params = self.build_params(params)
        return requests.get(url, params=params)
