from abc import ABC, abstractmethod

import requests
from requests import HTTPError
from fastapi.exceptions import HTTPException


class BrokerClient(ABC):
    BASE_URL = ""

    def __init__(self, api_key: str, private_key: str = None):
        self.api_key = api_key
        self.private_key = private_key

    @staticmethod
    @abstractmethod
    def validate_api_key(api_key: str, private_key: str) -> HTTPException | bool:
        """Using an API endpoint, validate that the API key and optionally a Private key is valid.

        :param api_key: An Api key to validate.
        :param private_key: Optional private key to validate.
        :return: True if the API key is valid, HTTPException otherwise.

        :throws: HTTPException if the API key is invalid.
        """
        pass

    def requests(self, method: str, path: str, params: dict = None) -> dict:
        """Send a request to an api endpoint, return the json response.

        :param method: The HTTP method to use, valid values are GET, POST.
        :param path: The API endpoint path.
        :param params: Optional parameters to pass to the request.
        :return: A json response as a dict.

        :raises HTTPException: If server responded with an error.
        """
        url = self.BASE_URL + path
        headers = {"Authorization": self.api_key}

        response = {}
        try:
            if method == "GET":
                response = requests.get(url, headers=headers, params=params)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=params)
            else:
                raise ValueError("Unknown HTTP method: {}".format(method))

            response.raise_for_status()
        except HTTPError:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        return response.json()

