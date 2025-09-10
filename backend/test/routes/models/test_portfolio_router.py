from starlette.testclient import TestClient

from backend.src.core.models.portfolio import Portfolio, Cash
from backend.src.core.models import portfolio
from backend.src.database.models.api_key_model import ApiKey
from backend.src.main import app
from backend.src.routes.models import portfolio_router

client = TestClient(app)

def _mock_build_portfolio(broker_name, db_api_key, private_key):
    cash_cls = Cash(
        10,
    )

    return Portfolio(cash_cls)

def _mock_get_db_api_key(db, user_id, broker_name):
    return ApiKey(
        user_id=1,
        broker_name="Trading212",
        api_key="test",
        private_key="test"
    )

def test_portfolio_get_broker_failure(monkeypatch):
    response = client.get("/api/portfolio/unknown_broker")
    assert response.status_code == 404

    response = client.get("/api/portfolio/Kraken")
    assert response.status_code == 409

def test_portfolio_get_broker_success(monkeypatch):
    monkeypatch.setattr(portfolio_router, "get_db_api_key", _mock_get_db_api_key)
    monkeypatch.setattr(portfolio_router, "build_portfolio", _mock_build_portfolio)

    response = client.get("/api/portfolio/Trading212")
    assert response.status_code == 200

