from abc import ABC, abstractmethod
from starlette.exceptions import HTTPException


class BrokerClient(ABC):
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