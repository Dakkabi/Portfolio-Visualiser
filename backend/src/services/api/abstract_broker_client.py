from abc import ABC
from typing import Optional
import requests

class AbstractBrokerClient(ABC):
    """Abstract class to represent a broker / exchange client."""
    API_KEY = None
    PRIVATE_KEY = None

    BASE_URL = None

    def __init__(self, api_key: str, private_key: Optional[str] = None):
        self.API_KEY = api_key
        self.PRIVATE_KEY = private_key

    def send_request(self, method: str, path: str, params: Optional[dict] = None) -> dict:
        """Send a request to the broker's server."""
        if self.BASE_URL is None:
            raise NotImplementedError(f"Base URL not set for {self.__class__.__name__}")

        url = self.BASE_URL + path

        method = method.upper()
        response = {}
        if method == "GET":
            response = requests.get(url, params=params, auth=(self.API_KEY, self.PRIVATE_KEY))

        else:
            raise ValueError(f"Unknown method {method}")

        response.raise_for_status()
        return response.json()
