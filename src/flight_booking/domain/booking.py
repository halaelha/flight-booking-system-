

from dataclasses import dataclass


@dataclass
class Booking:
    booking_id: str
    passenger_name: str
    flight_number: str
    ticket_class: str
    total_price: float
    status: str = "CONFIRMED"
