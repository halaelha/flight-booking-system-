
from flight_booking.domain.booking import Booking
from flight_booking.infrastructure.in_memory_booking_repository import (
    InMemoryBookingRepository,
)


def test_save_booking():
    repository = InMemoryBookingRepository()

    booking = Booking(
        booking_id="B001",
        passenger_name="Sara",
        flight_number="TK101",
        ticket_class="Economy",
        total_price=200.0,
    )

    repository.save(booking)

    result = repository.find_by_id("B001")

    assert result == booking


def test_booking_not_found():
    repository = InMemoryBookingRepository()

    result = repository.find_by_id("INVALID")

    assert result is None
