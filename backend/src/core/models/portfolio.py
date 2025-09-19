from dataclasses import dataclass, field

import pandas
from pandas import DataFrame

from backend.src.core.services.brokers import BROKER_REGISTRY


@dataclass
class Cash:
    free: float = 0                 # Liquid cash held
    total: float = 0                # Total Portfolio Value after realised gains/losses
    total_dividends: float = 0      # Total gain from Dividends
    unrealised_gain_loss: float = 0 # Potential Gain or Loss on assets unsold
    invested: float = 0             # Total invested before gains/losses

    def __add__(self, other):
        if not isinstance(other, Cash):
            raise NotImplemented

        return Cash(
            self.free + other.free,
            self.total + other.total,
            self.total_dividends + other.total_dividends,
            self.unrealised_gain_loss + other.unrealised_gain_loss,
            self.invested + other.invested,
        )

@dataclass
class Stock:
    assets: DataFrame = field(default_factory=lambda: DataFrame(columns=["ticker", "average_price", "quantity"]))

    def __add__(self, other):
        if not isinstance(other, Stock):
            raise NotImplemented

        # TODO: Handle collision between duplicated ticker names
        return Stock(pandas.concat([self.assets, other.assets], ignore_index=True))

class Portfolio:
    def __init__(self, cash_cls: Cash, stock_cls: Stock):
        self.Cash = cash_cls
        self.Stock = stock_cls

    def __add__(self, other):
        if not isinstance(other, Portfolio):
            raise NotImplemented

        new_portfolio = Portfolio(
            self.Cash + other.Cash,
            self.Stock + other.Stock,
        )
        return new_portfolio

    @classmethod
    def empty(cls):
        return Portfolio(Cash(), Stock())

    def to_dict(self):
        """Return a dict representation of the portfolio."""
        return {
            "Cash": {
                "free": self.Cash.free,
                "total": self.Cash.total,
                "total_dividends": self.Cash.total_dividends,
                "unrealised_gain_loss": self.Cash.unrealised_gain_loss,
                "invested": self.Cash.invested,
            },
            "Stock": {
                "assets": self.Stock.assets.to_dict(orient="records")
            }
        }

    @staticmethod
    def from_dict(data: dict):
        """Return a Portfolio object from a dict."""
        cash_cls = Cash(**data["Cash"])
        stock_cls = Stock(assets=DataFrame.from_dict(data["Stock"]["assets"]))

        return Portfolio(cash_cls, stock_cls)

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

    stock_data = broker_cls.build_stock()
    stock_cls = Stock(stock_data)

    return Portfolio(cash_cls, stock_cls)