from typing import Optional

import requests

class AbstractBrokerAPI:
    base_domain = ""

    def __init__(self, api_key: str, private_key: Optional[str]):
        self.api_key = api_key
        self.private_key = private_key

    @staticmethod
    def verify_api_key(api_key: str, private_key: Optional[str] = None):
        """
        Ensure that the entered API key and optional Private Key are valid for the broker.

        :param api_key: The API key to verify.
        :param private_key: The Private key to verify.
        :return: True if the API key is valid, False otherwise.
        """
        raise NotImplementedError()

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
            "Authorization": {self.api_key}
        }

        if method == "GET":
            response = requests.get(url, headers=headers, params=params)

        elif method == "POST":
            response = requests.post(url, headers=headers, json=params)

        else:
            raise ValueError(f"Unknown method name: {method}")

        response.raise_for_status()
        return response.json()