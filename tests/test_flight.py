
from datetime import date

from flight_booking.domain.flight import Flight


def test_flight_is_available():
    flight = Flight(
        flight_number="TK101",
        origin="Istanbul",
        destination="London",
        departure_date=date(2026, 12, 15),
        price=250.0,
        available_seats=10,
    )

    assert flight.is_available() is True
