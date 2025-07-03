from typing import Optional

import requests

class AbstractBroker:
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

    def requests(self):
        pass