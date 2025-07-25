from backend.src.services.brokers.broker_api import AbstractBrokerAPI


class Kraken(AbstractBrokerAPI):
    base_domain = ""

    @staticmethod
    def verify_api_key_response():
        return None