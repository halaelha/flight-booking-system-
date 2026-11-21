
from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, base_price: float) -> float:
        pass


class EconomyPricing(PricingStrategy):
    def calculate_price(self, base_price: float) -> float:
        return base_price


class BusinessPricing(PricingStrategy):
    def calculate_price(self, base_price: float) -> float:
        return base_price * 1.5


class FirstClassPricing(PricingStrategy):
    def calculate_price(self, base_price: float) -> float:
        return base_price * 2
