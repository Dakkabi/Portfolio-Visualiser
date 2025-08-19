from starlette.exceptions import HTTPException

from backend.src.core.services.brokers.AbstractBrokerClient import BrokerClient


class Trading212(BrokerClient):
    BASE_URL = "https://live.trading212.com"

    @staticmethod
    def validate_api_key(api_key: str, private_key: str) -> HTTPException | bool:
        return True

    # Personal Portfolio
    def fetch_a_specific_position(self, ticker: str) -> dict:
        """Fetch an open position by ticker"""
        return super().requests("GET", "/api/v0/equity/portfolio/" + ticker)