from backend.src.services.brokers.trading212_api import Trading212

registry = {
    "Trading212": Trading212.verify_api_key_response
}