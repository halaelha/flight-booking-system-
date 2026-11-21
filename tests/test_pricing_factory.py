
import pytest

from flight_booking.domain.pricing_factory import PricingStrategyFactory
from flight_booking.domain.pricing_strategy import (
    EconomyPricing,
    BusinessPricing,
    FirstClassPricing,
)


def test_economy_factory():
    strategy = PricingStrategyFactory.create("Economy")
    assert isinstance(strategy, EconomyPricing)


def test_business_factory():
    strategy = PricingStrategyFactory.create("Business")
    assert isinstance(strategy, BusinessPricing)


def test_first_class_factory():
    strategy = PricingStrategyFactory.create("First Class")
    assert isinstance(strategy, FirstClassPricing)


def test_invalid_ticket_class():
    with pytest.raises(ValueError, match="Invalid ticket class"):
        PricingStrategyFactory.create("VIP")

