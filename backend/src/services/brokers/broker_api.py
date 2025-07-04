import warnings
from typing import Optional

import requests

from backend.src.core.config import settings


class AbstractBrokerAPI:
    base_domain = ""

    is_private_key_required = False

    def __init__(self, api_key: str = None, private_key: Optional[str] = None ):
        broker_name = self.get_broker_name()

        if api_key is None:
            api_key = getattr(settings, f"{broker_name}_API_KEY")
        self.api_key = api_key

        if private_key is None and self.is_private_key_required:
            private_key = getattr(settings, f"{broker_name}_PRIVATE_KEY")
        self.private_key = private_key


    @staticmethod
    def verify_api_key(**kwargs):
        """
        Ensure that the entered API key and optional Private Key are valid for the broker.

        :param api_key: The API key to verify.
        :param private_key: The Private key to verify.
        :return: True if the API key is valid, False otherwise.
        """
        raise NotImplementedError()

    def get_broker_name(self):
        """
        Return an all-capital name of the broker, by removing the '_api' suffix from the class name.

        :return: Return the name of the broker.
        """
        class_name = self.__class__.__name__
        return class_name[:-3].upper()

    def requests(self, method: str, path: str, params: Optional[dict] = None) -> dict:
        """
        Send a request to the API endpoint.

        :param method: The HTTP method to use.
        :param path: The API endpoint path.
        :param params: Additional query/body parameters.
        :return: Response from the API endpoint.

        :raises ValueError: Unknown method name.
        :raises HTTPError: An HTTP error occurred.
        """

        url = self.base_domain + path

        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_key
        }

        if method == "GET":
            response = requests.get(url, headers=headers, params=params)

        elif method == "POST":
            response = requests.post(url, headers=headers, json=params)

        else:
            raise ValueError(f"Unknown method name: {method}")

        response.raise_for_status()
        return response.json()