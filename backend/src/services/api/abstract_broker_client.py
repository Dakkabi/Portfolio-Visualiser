from abc import ABC, abstractmethod
from typing import Optional
import requests
from fastapi import HTTPException


class AbstractBrokerClient(ABC):
    """Abstract class to represent a broker / exchange client."""
    API_KEY = None
    PRIVATE_KEY = None

    BASE_URL = None

    def __init__(self, api_key: str, private_key: Optional[str] = None):
        self.API_KEY = api_key
        self.PRIVATE_KEY = private_key

    @staticmethod
    @abstractmethod
    def verify_api_keys(**kwargs): # Allow subclasses to determine the amount of api keys required.
        """Verify that the API key is valid by sending a request to the server and expecting no error status codes."""
        return NotImplementedError("verify_api_keys method not implemented")

    def send_request(self, method: str, path: str, params: Optional[dict] = None) -> dict:
        """Send a request to the broker's server."""
        if self.BASE_URL is None:
            raise NotImplementedError(f"Base URL not set for {self.__class__.__name__}")

        url = self.BASE_URL + path

        method = method.upper()
        response = {}

        try:
            if method == "GET":
                response = requests.get(url, params=params, auth=(self.API_KEY, self.PRIVATE_KEY))

            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as requests_HTTPError:
            raise HTTPException(status_code=requests_HTTPError.response.status_code, detail=str(requests_HTTPError.response))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unknown error: {e}")
