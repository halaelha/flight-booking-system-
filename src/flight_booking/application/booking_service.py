
from uuid import uuid4

from flight_booking.domain.booking import Booking
from flight_booking.domain.flight import Flight


class BookingService:
    def __init__(self):
        self.bookings: list[Booking] = []

    def create_booking(
        self, passenger_name: str, flight: Flight
    ) -> Booking:
        if not passenger_name.strip():
            raise ValueError("Passenger name is required")

        if not flight.is_available():
            raise ValueError("No available seats")

        booking = Booking(
            booking_id=str(uuid4()),
            passenger_name=passenger_name,
            flight_number=flight.flight_number,
        )

        flight.available_seats -= 1
        self.bookings.append(booking)

        return booking

    def cancel_booking(self, booking_id: str) -> None:
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                if booking.status == "CANCELLED":
                    raise ValueError("Booking already cancelled")

                booking.status = "CANCELLED"
                return

        raise ValueError("Booking not found")
