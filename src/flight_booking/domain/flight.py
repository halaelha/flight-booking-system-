
from dataclasses import dataclass
from datetime import date


@dataclass
class Flight:
    flight_number: str
    origin: str
    destination: str
    departure_date: date
    price: float
    available_seats: int

    def is_available(self) -> bool:
        return self.available_seats > 0
