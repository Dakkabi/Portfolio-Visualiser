from backend.src.core.services.brokers import Trading212Client, KrakenClient

BROKER_REGISTRY = {
    "Trading212": Trading212Client,
    "Kraken": KrakenClient,
}