from starlette.exceptions import HTTPException

from backend.src.core.services.brokers.AbstractBrokerClient import BrokerClient


class Trading212(BrokerClient):

    @staticmethod
    def validate_api_key(api_key: str) -> HTTPException | bool:
        return True