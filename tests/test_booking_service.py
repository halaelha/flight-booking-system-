
from datetime import date

from flight_booking.domain.flight import Flight
from flight_booking.application.booking_service import BookingService


def test_create_booking():
    flight = Flight(
        "TK101", "Istanbul", "London",
        date(2026, 12, 15), 250.0, 10
    )

    service = BookingService()
    booking = service.create_booking("Sara", flight)

    assert booking.passenger_name == "Sara"
    assert booking.status == "CONFIRMED"
    assert flight.available_seats == 9
    assert len(service.bookings) == 1
