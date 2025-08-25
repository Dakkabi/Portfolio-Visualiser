from backend.src.core.services.brokers.KrakenClient import Kraken
from backend.src.core.services.brokers.Trading212Client import Trading212

BROKER_REGISTRY = {
    "Trading212": Trading212,
    "Kraken": Kraken,
}