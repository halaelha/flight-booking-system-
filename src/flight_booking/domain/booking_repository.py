
from abc import ABC, abstractmethod

from flight_booking.domain.booking import Booking


class BookingRepository(ABC):

    @abstractmethod
    def save(self, booking: Booking) -> None:
        pass

    @abstractmethod
    def find_by_id(self, booking_id: str) -> Booking | None:
        pass

    @abstractmethod
    def find_by_passenger(
        self, passenger_name: str
    ) -> list[Booking]:
        pass
