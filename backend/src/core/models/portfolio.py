from dataclasses import dataclass

from backend.src.core.services.brokers import BROKER_REGISTRY


@dataclass
class Cash:
    total: float = 0                # Total Portfolio Value after realised gains/losses
    total_dividends: float = 0      # Total gain from Dividends
    unrealised_gain_loss: float = 0 # Potential Gain or Loss on assets unsold
    invested: float = 0             # Total invested before gains/losses

    def __add__(self, other):
        if not isinstance(other, Cash):
            raise NotImplemented

        return Cash(
            self.total + other.total,
            self.total_dividends + other.total_dividends,
            self.unrealised_gain_loss + other.unrealised_gain_loss,
            self.invested + other.invested,
        )

class Portfolio:
    def __init__(self, cash_cls: Cash):
        self.Cash = cash_cls

    def __add__(self, other):
        if not isinstance(other, Portfolio):
            raise NotImplemented

        new_portfolio = Portfolio(
            self.Cash + other.Cash,
        )
        return new_portfolio

    @classmethod
    def empty(cls):
        return Portfolio(Cash())

    def to_dict(self):
        """Return a dict representation of the portfolio."""
        return {
            "Cash": {
                "total": self.Cash.total,
                "total_dividends": self.Cash.total_dividends,
                "unrealised_gain_loss": self.Cash.unrealised_gain_loss,
                "invested": self.Cash.invested,
            }
        }

    @staticmethod
    def from_dict(data: dict):
        """Return a Portfolio object from a dict."""
        cash_cls = Cash(**data["Cash"])

        return Portfolio(cash_cls)

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