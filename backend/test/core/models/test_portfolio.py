import pytest

from backend.src.core.models.portfolio import Stock, Portfolio, Cash


def test_class_not_implemented():
    stock_cls = Stock()
    cash_cls = Cash()
    portfolio_cls = Portfolio.empty()

    with pytest.raises(TypeError):
        stock_cls + "string"

    with pytest.raises(TypeError):
        portfolio_cls + 400

    with pytest.raises(TypeError):
        cash_cls + "string"
