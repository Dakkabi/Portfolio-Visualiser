from starlette.exceptions import HTTPException

from backend.src.core.services.brokers.AbstractBrokerClient import BrokerClient


class Trading212(BrokerClient):
    BASE_URL = "https://live.trading212.com"

    @staticmethod
    def validate_api_key(api_key: str, private_key: str) -> bool:
        try:
            # Use fetch_a_specific_position as it has the lowest rate limits: 1/1s
            # Doesn't matter what ticker, use AAPL as placeholder.
            client = Trading212(api_key)
            response = client.fetch_a_specific_position("AAPL_US_EQ")
            return response is not None

        except HTTPException as e:
            if e.status_code == 404:
                # No open position with that ticker
                # API Key is valid, the user just doesn't own any AAPL.
                return True
            elif e.status_code == 401:
                raise HTTPException(status_code=401, detail="Invalid API key")

            elif e.status_code == 403:
                raise HTTPException(status_code=403, detail="Invalid API key scope, valid key but insufficient permissions.")

            raise HTTPException(status_code=e.status_code, detail=f"Unable to verify API keys, client returned: '{e.status_code}: {e.detail}'")


    # Personal Portfolio
    def fetch_a_specific_position(self, ticker: str) -> dict:
        """Fetch an open position by ticker"""
        return super().send_request("GET", "/api/v0/equity/portfolio/" + ticker)