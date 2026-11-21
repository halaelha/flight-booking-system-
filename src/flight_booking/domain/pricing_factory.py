
from flight_booking.domain.pricing_strategy import (
    PricingStrategy,
    EconomyPricing,
    BusinessPricing,
    FirstClassPricing,
)


class PricingStrategyFactory:

    @staticmethod
    def create(ticket_class: str) -> PricingStrategy:
        strategies = {
            "economy": EconomyPricing,
            "business": BusinessPricing,
            "first class": FirstClassPricing,
        }

        strategy_class = strategies.get(ticket_class.strip().lower())

        if strategy_class is None:
            raise ValueError(f"Invalid ticket class: {ticket_class}")

        return strategy_class()
