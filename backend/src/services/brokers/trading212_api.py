from backend.src.services.brokers.broker_api import AbstractBrokerAPI

class Trading212(AbstractBrokerAPI):
    base_domain = "https://live.trading212.com"

    @staticmethod
    def verify_api_key(api_key: str):
        # fetch_account_data has the lowest rate limit at 1/2s
        try:
            Trading212(api_key=api_key).fetch_account_data()
        except Exception as e:
            return e
        return True

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
