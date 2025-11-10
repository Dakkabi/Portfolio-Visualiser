from backend.src.services.api.abstract_broker_client import AbstractBrokerClient


class Trading212Client(AbstractBrokerClient):
    """Client class for the Trading212 API Endpoints"""
    BASE_URL = "https://live.trading212.com"

    def get_account_cash_balance(self) -> dict:
        """Provides a detailed breakdown of your account's cash and investment metrics, including available funds, invested capital, and total account value.

        Rate Limit: 1 request per 2 seconds
        """
        return super().send_request("GET", "/api/v0/equity/account/cash")