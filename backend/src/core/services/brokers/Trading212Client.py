from starlette.exceptions import HTTPException

from backend.src.core.services.brokers.AbstractBrokerClient import BrokerClient


class Trading212(BrokerClient):
    BASE_URL = "https://live.trading212.com"

    @staticmethod
    def validate_api_key(api_key: str, private_key: str) -> HTTPException | bool:
        try:
            # Use fetch_a_specific_position as it has the lowest rate limits: 1/1s
            # Doesn't matter what ticker, use AAPL as placeholder.
            return Trading212.fetch_a_specific_position(Trading212(api_key), "AAPL_US_EQ") is not None
        except HTTPException as e:
            if e.status_code == 404: # No open position with that ticker
                return True
            raise e

    # Personal Portfolio
    def fetch_a_specific_position(self, ticker: str) -> dict:
        """Fetch an open position by ticker"""
        return super().requests("GET", "/api/v0/equity/portfolio/" + ticker)