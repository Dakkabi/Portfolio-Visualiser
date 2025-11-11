from backend.src.services.api.abstract_broker_client import AbstractBrokerClient


class Trading212Client(AbstractBrokerClient):
    """Client class for the Trading212 API Endpoints"""
    BASE_URL = "https://live.trading212.com"

    # Account Data
    def get_account_cash_balance(self) -> dict:
        """Provides a detailed breakdown of your account's cash and investment metrics, including available funds, invested capital, and total account value.

        Rate Limit: 1 request per 2 seconds
        """
        return super().send_request("GET", "/api/v0/equity/account/cash")

    def get_account_information(self) -> dict:
        """Retrieves fundamental information about your trading account, such as your primary account number and its base currency.

        Rate Limit: 1 request per 30 seconds
        """
        return super().send_request("GET", "/api/v0/equity/account/info")