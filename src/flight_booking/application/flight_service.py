
from datetime import date

from flight_booking.domain.flight import Flight


class FlightService:
    def __init__(self, flights: list[Flight]):
        self.flights = flights

    def search_flights(
        self,
        origin: str,
        destination: str,
        departure_date: date,
    ) -> list[Flight]:

        return [
            flight
            for flight in self.flights
            if flight.origin.lower() == origin.lower()
            and flight.destination.lower() == destination.lower()
            and flight.departure_date == departure_date
            and flight.is_available()
        ]
