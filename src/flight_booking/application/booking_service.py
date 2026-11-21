
from uuid import uuid4

from flight_booking.domain.booking import Booking
from flight_booking.domain.flight import Flight
from flight_booking.domain.pricing_strategy import PricingStrategy
from flight_booking.domain.booking_repository import BookingRepository


class BookingService:

    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def create_booking(
        self,
        passenger_name: str,
        flight: Flight,
        pricing_strategy: PricingStrategy,
        ticket_class: str,
    ) -> Booking:

        if not passenger_name.strip():
            raise ValueError("Passenger name is required")

        if not flight.is_available():
            raise ValueError("No available seats")

        if flight.price < 0:
            raise ValueError("Flight price cannot be negative")

        total_price = pricing_strategy.calculate_price(
            flight.price
        )

        booking = Booking(
            booking_id=str(uuid4()),
            passenger_name=passenger_name,
            flight_number=flight.flight_number,
            ticket_class=ticket_class,
            total_price=total_price,
        )

        flight.available_seats -= 1
        self.repository.save(booking)

        return booking

    def cancel_booking(
        self,
        booking_id: str,
        flight: Flight,
    ) -> None:

        booking = self.repository.find_by_id(booking_id)

        if booking is None:
            raise ValueError("Booking not found")

        if booking.status == "CANCELLED":
            raise ValueError("Booking already cancelled")

        if booking.flight_number != flight.flight_number:
            raise ValueError("Flight does not match booking")

        booking.status = "CANCELLED"
        flight.available_seats += 1
        self.repository.save(booking)

