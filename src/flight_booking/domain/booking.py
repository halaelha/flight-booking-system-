
from dataclasses import dataclass


@dataclass
class Booking:
    booking_id: str
    passenger_name: str
    flight_number: str
    status: str = "CONFIRMED"
