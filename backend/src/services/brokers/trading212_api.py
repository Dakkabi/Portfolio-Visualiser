from datetime import datetime

import requests.exceptions

from backend.src.services.brokers.broker_api import AbstractBrokerAPI

class Trading212(AbstractBrokerAPI):
    base_domain = "https://live.trading212.com"

    @staticmethod
    def verify_api_key_response(api_key: str) -> None | requests.exceptions.HTTPError:
        # fetch_account_data has the lowest rate limit at 1/2s
        try:
            Trading212(api_key=api_key).fetch_account_data()
        except requests.exceptions.HTTPError as e:
            return e
        return None

    # Account Data
    def fetch_account_data(self):
        return super().requests(method="GET", path="/api/v0/equity/account/cash")

    def fetch_account_metadata(self):
        return super().requests(method="GET", path="/api/v0/equity/account/info")

    # Personal Portfolio
    def fetch_all_open_positions(self):
        return super().requests(method="GET", path="/api/v0/equity/portfolio")

    def search_for_a_specific_position_by_ticker(self, ticker: str):
        payload = {
            "ticker": ticker
        }
        return super().requests(method="POST", path="/api/v0/equity/portfolio/ticker", params=payload)

    def fetch_a_specific_position(self, ticker: str):
        return super().requests(method="GET", path=f"/api/v0/equity/portfolio/{ticker}")

    # Historical Items
    def historical_order_data(self, cursor: int, ticker: str, limit: int):
        if (limit > 50) and (limit < 0):
            raise ValueError("Limit must be between 0 and 50 inclusive.")

        payload = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit
        }
        return super().requests("GET", "/api/v0/equity/history/orders", payload)

    def paid_out_dividends(self, cursor: int, ticker: str, limit: int):
        if (limit > 50) and (limit < 0):
            raise ValueError("Limit must be between 0 and 50 inclusive.")

        payload = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit
        }
        return super().requests("GET", "/api/v0/history/dividends", payload)

    def exports_list(self):
        return super().requests("GET", "/api/v0/history/exports")

    def export_csv(self):
        """Intentionally left unimplemented due to responsibility boundaries with users' broker accounts."""
        raise NotImplementedError("Export CSV is too invasive, won't be supported.")

    def transaction_list(self, cursor: str, time: datetime, limit: int):
        if (limit > 50) and (limit < 0):
            raise ValueError("Limit must be between 0 and 50 inclusive.")

        payload = {
            "cursor": cursor,
            "time": time,
            "limit": limit
        }
        return super().requests("GET", "/api/v0/history/transactions", payload)

print(Trading212().verify_api_key_response("tet").response.reason)