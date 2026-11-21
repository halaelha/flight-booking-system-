
from datetime import date

import pytest

from flight_booking.domain.flight import Flight
from flight_booking.domain.pricing_strategy import EconomyPricing
from flight_booking.application.booking_service import BookingService
from flight_booking.infrastructure.in_memory_booking_repository import (
    InMemoryBookingRepository,
)


def make_service():
    return BookingService(InMemoryBookingRepository())


def make_flight(seats=10, price=200.0):
    return Flight(
        "TK101",
        "Istanbul",
        "London",
        date(2026, 12, 15),
        price,
        seats,
    )


def test_booking_with_no_available_seats():
    flight = make_flight(seats=0)
    service = make_service()

    with pytest.raises(ValueError, match="No available seats"):
        service.create_booking(
            "Sara", flight, EconomyPricing(), "Economy"
        )


def test_booking_with_empty_passenger_name():
    flight = make_flight()
    service = make_service()

    with pytest.raises(ValueError, match="Passenger name is required"):
        service.create_booking(
            "", flight, EconomyPricing(), "Economy"
        )


def test_booking_with_negative_price():
    flight = make_flight(price=-100)
    service = make_service()

    with pytest.raises(ValueError, match="cannot be negative"):
        service.create_booking(
            "Sara", flight, EconomyPricing(), "Economy"
        )


def test_cancelling_nonexistent_booking():
    flight = make_flight()
    service = make_service()

    with pytest.raises(ValueError, match="Booking not found"):
        service.cancel_booking("INVALID-ID", flight)


def test_cancelling_booking_with_wrong_flight():
    flight = make_flight()
    wrong_flight = Flight(
        "TK999",
        "Paris",
        "Rome",
        date(2026, 12, 20),
        150.0,
        5,
    )

    service = make_service()
    booking = service.create_booking(
        "Sara", flight, EconomyPricing(), "Economy"
    )

    with pytest.raises(ValueError, match="Flight does not match"):
        service.cancel_booking(
            booking.booking_id, wrong_flight
        )

    assert booking.status == "CONFIRMED"
    assert flight.available_seats == 9
    assert wrong_flight.available_seats == 5

