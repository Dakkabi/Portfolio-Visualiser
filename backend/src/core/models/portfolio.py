from dataclasses import dataclass

from backend.src.core.services.brokers import BROKER_REGISTRY


@dataclass
class Cash:
    total: float

class Portfolio:
    def __init__(self, cash_cls: Cash):
        self.Cash = cash_cls

    def to_dict(self):
        """Return a dict representation of the portfolio."""
        return {
            "Cash": {
                "total": self.Cash.total,
            }
        }

def build_portfolio(broker_name: str, api_key: str, private_key: str = None):
    """Build and populate a portfolio class using the broker's client services.

    :param broker_name: The name of the broker to populate the class with.
    :param api_key: The API key of the broker.
    :param private_key: An optional private key of the broker.

    :return: A Portfolio class.
    """
    broker_cls = BROKER_REGISTRY[broker_name]
    broker_cls = broker_cls(api_key=api_key, private_key=private_key)

    cash_data = broker_cls.build_cash()
    cash_cls = Cash(**cash_data)

    return Portfolio(cash_cls)