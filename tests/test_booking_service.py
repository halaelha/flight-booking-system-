
from datetime import date

import pytest

from flight_booking.domain.flight import Flight
from flight_booking.domain.pricing_strategy import (
    EconomyPricing,
    BusinessPricing,
)
from flight_booking.application.booking_service import BookingService
from flight_booking.infrastructure.in_memory_booking_repository import (
    InMemoryBookingRepository,
)


def make_flight():
    return Flight(
        "TK101",
        "Istanbul",
        "London",
        date(2026, 12, 15),
        200.0,
        10,
    )


def make_service():
    repository = InMemoryBookingRepository()
    return BookingService(repository)


def test_create_booking():
    flight = make_flight()
    service = make_service()

    booking = service.create_booking(
        "Sara", flight, EconomyPricing(), "Economy"
    )

    assert booking.passenger_name == "Sara"
    assert booking.status == "CONFIRMED"
    assert booking.total_price == 200.0
    assert flight.available_seats == 9
    assert service.repository.find_by_id(booking.booking_id) == booking


def test_business_booking():
    flight = make_flight()
    service = make_service()

    booking = service.create_booking(
        "Sara", flight, BusinessPricing(), "Business"
    )

    assert booking.total_price == 300.0
    assert booking.ticket_class == "Business"


def test_cancel_booking_restores_seat():
    flight = make_flight()
    service = make_service()

    booking = service.create_booking(
        "Sara", flight, EconomyPricing(), "Economy"
    )

    service.cancel_booking(booking.booking_id, flight)

    assert booking.status == "CANCELLED"
    assert flight.available_seats == 10


def test_cannot_cancel_twice():
    flight = make_flight()
    service = make_service()

    booking = service.create_booking(
        "Sara", flight, EconomyPricing(), "Economy"
    )

    service.cancel_booking(booking.booking_id, flight)

    with pytest.raises(ValueError, match="already cancelled"):
        service.cancel_booking(booking.booking_id, flight)

    assert flight.available_seats == 10


