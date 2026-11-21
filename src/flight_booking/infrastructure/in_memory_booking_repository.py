
from flight_booking.domain.booking import Booking
from flight_booking.domain.booking_repository import BookingRepository


class InMemoryBookingRepository(BookingRepository):

    def __init__(self):
        self.bookings: dict[str, Booking] = {}

    def save(self, booking: Booking) -> None:
        self.bookings[booking.booking_id] = booking

    def find_by_id(self, booking_id: str) -> Booking | None:
        return self.bookings.get(booking_id)
