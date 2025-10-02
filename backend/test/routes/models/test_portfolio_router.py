from starlette.testclient import TestClient

from backend.src.core.models.portfolio import Portfolio, Cash, Stock
from backend.src.core.services.models import portfolio_service
from backend.src.database.models.api_key_model import ApiKey
from backend.src.main import app

client = TestClient(app)

def _mock_build_portfolio(broker_name, db_api_key, private_key):
    cash_cls = Cash(
        total=10,
    )
    stock_cls = Stock()

    return Portfolio(cash_cls, stock_cls)

def _mock_build_portfolio_update(broker_name, db_api_key, private_key):
    cash_cls = Cash(
        total=20,
    )
    stock_cls = Stock()

    return Portfolio(cash_cls, stock_cls)

def _mock_get_db_api_key(db, user_id, broker_name):
    return ApiKey(
        user_id=1,
        broker_name="Trading212",
        api_key="test",
        private_key="test"
    )

def _is_portfolio_outdated(portfolio, broker_rate_limit):
    return False

def test_portfolio_get_broker_failure(monkeypatch):
    response = client.get("/api/portfolio/unknown_broker")
    assert response.status_code == 404

    response = client.get("/api/portfolio/Kraken")
    assert response.status_code == 409

def test_portfolio_get_broker_success(monkeypatch):
    monkeypatch.setattr(portfolio_service, "get_db_api_key", _mock_get_db_api_key)
    monkeypatch.setattr(portfolio_service, "build_portfolio", _mock_build_portfolio)
    monkeypatch.setattr(portfolio_service, "is_portfolio_outdated", _is_portfolio_outdated)

    response = client.get("/api/portfolio/Trading212")
    assert response.status_code == 200

    data = response.json()
    assert data["portfolio"]["Cash"]["total"] == 10

    monkeypatch.setattr(portfolio_service, "build_portfolio", _mock_build_portfolio_update)
    response = client.get("/api/portfolio/Trading212")
    assert response.status_code == 200

    data = response.json()
    assert data["portfolio"]["Cash"]["total"] == 20

def test_portfolio_get_total():
    response = client.get("/api/portfolio/total")
    assert response.status_code == 200