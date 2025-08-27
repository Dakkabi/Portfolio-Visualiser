from starlette.exceptions import HTTPException

from backend.src.core.services.brokers.AbstractBrokerClient import BrokerClient

class Trading212(BrokerClient):
    BASE_URL = "https://live.trading212.com"

    def build_cash(self) -> dict:
        data = {}

        fetch_account_cash = self.fetch_account_cash()
        data["total"] = fetch_account_cash["total"]

        return data

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

    # Account Data
    def fetch_account_cash(self):
        """Fetch cash information

        :raises HTTPException: If request fails, possible responses include:

            - 200 OK
            - 401 Bad API key
            - 403 Scope (account) missing for API key
            - 408 Timed-out
            - 429 Limited: 1 / 2s
        """
        return super().send_request("GET", "/api/v0/equity/account/cash")

    def fetch_account_metadata(self):
        """Fetch account information.

        :raises HTTPException: If request fails, possible responses include:

            - 200 OK
            - 401 Bad API key
            - 403 Scope (account) missing for API key
            - 408 Timed-out
            - 429 Limited: 1 / 30s
        """
        return super().send_request("GET", "/api/v0/equity/account/info")

    # Personal Portfolio
    def fetch_all_open_positions(self):
        """Fetch all open positions.

        :raises HTTPException: If request fails, possible responses include:

            - 200 OK
            - 401 Bad API key
            - 403 Scope (portfolio) missing for API key
            - 408 Timed-out
            - 429 Limited: 1 / 5s
        """
        return super().send_request("GET", "/api/v0/equity/portfolio")

    def search_for_a_specific_position_by_ticker(self, ticker: str):
        """Fetch an open position by ticker, using POST method.

        :param ticker: Ticker to search for.

        :raises HTTPException: If request fails, possible responses include:

            - 200 OK
            - 400 Invalid ticker supplied
            - 401 Bad API key
            - 403 Scope (portfolio) missing for API key
            - 404 No open position with ticker supplied
            - 408 Timed-out
            - 429 Limited: 1 / 1s
        """

    def fetch_a_specific_position(self, ticker: str):
        """Fetch an open position by ticker, using GET method.

        :param ticker: Ticker to search for.

        :raises HTTPException: If request fails, possible responses include:

            - 200 OK
            - 400 Invalid ticker supplied
            - 401 Bad API key
            - 403 Scope (portfolio) missing for API key
            - 404 No open position with ticker supplied
            - 408 Timed-out
            - 429 Limited: 1 / 1s
        """
        return super().send_request("GET", "/api/v0/equity/portfolio/" + ticker)

    # Historical Items
    def historical_order_data(self, cursor: int, ticker: str = None, limit: int = 50):
        """Fetch historical asset order data.

        :param cursor: Pagination cursor.
        :param ticker: Optional ticker filter, defaults to None.
        :param limit: Max items per page, defaults to 50, must be lower than or equal to 50.

        :raises HTTPException: If request fails, possible responses include:

            - 200 OK
            - 400 Bad filtering arguments
            - 401 Bad API key
            - 403 Scope (history:orders) missing for API key
            - 408 Timed-out
            - 429 Limited: 1 / 1m
        """
        if limit > 50: raise ValueError("Limit cannot be greater than 50")

        params = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit,
        }

        return super().send_request("GET", "/api/v0/equity/history/orders", params)

    def paid_out_dividends(self, cursor: int, ticker: str = None, limit: int = 50):
        """Fetch all historical dividend payment.

        :param cursor: Pagination cursor.
        :param ticker: Optional ticker filter, defaults to None.
        :param limit: Max items per page, defaults to 50, must be lower than or equal to 50.

        :raises HTTPException: If request fails, possible responses include:

            - 200 OK
            - 400 Bad filtering arguments
            - 401 Bad API key
            - 403 Scope (history:dividends) missing for API key
            - 408 Timed-out
            - 429 Limited: 6 / 1m
        """
        if limit > 50: raise ValueError("Limit cannot be greater than 50")

        params = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit,
        }

        return super().send_request("GET", "/api/v0/history/dividends", params)
