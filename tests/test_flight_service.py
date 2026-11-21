
from datetime import date

from flight_booking.domain.flight import Flight
from flight_booking.application.flight_service import FlightService


def test_search_flights():
    flights = [
        Flight("TK101", "Istanbul", "London",
               date(2026, 12, 15), 250.0, 10),
        Flight("TK102", "Istanbul", "Paris",
               date(2026, 12, 15), 200.0, 5),
    ]

    service = FlightService(flights)

    results = service.search_flights(
        "Istanbul", "London", date(2026, 12, 15)
    )

    assert len(results) == 1
    assert results[0].flight_number == "TK101"
