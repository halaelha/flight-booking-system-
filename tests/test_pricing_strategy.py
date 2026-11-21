
from flight_booking.domain.pricing_strategy import (
    EconomyPricing,
    BusinessPricing,
    FirstClassPricing,
)


def test_economy_pricing():
    strategy = EconomyPricing()
    assert strategy.calculate_price(200) == 200


def test_business_pricing():
    strategy = BusinessPricing()
    assert strategy.calculate_price(200) == 300


def test_first_class_pricing():
    strategy = FirstClassPricing()
    assert strategy.calculate_price(200) == 400
