from backend.src.services.brokers.broker_api import AbstractBrokerAPI

class Trading212(AbstractBrokerAPI):
    base_domain = "https://live.trading212.com"

    @staticmethod
    def verify_api_key(api_key: str):
        # fetch_account_data has the lowest rate limit at 1/2
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