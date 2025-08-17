from starlette.exceptions import HTTPException

from backend.src.core.services.brokers.AbstractBrokerClient import BrokerClient


class Kraken(BrokerClient):

    @staticmethod
    def validate_api_key(api_key: str, private_key: str) -> HTTPException | bool:
        return HTTPException(status_code=401, detail="Invalid API key")