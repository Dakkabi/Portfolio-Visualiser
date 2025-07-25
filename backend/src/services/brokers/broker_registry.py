from backend.src.services.brokers.kraken_api import Kraken
from backend.src.services.brokers.trading212_api import Trading212

broker_registry = {
    "Trading212": Trading212,
    "Kraken": Kraken,
}