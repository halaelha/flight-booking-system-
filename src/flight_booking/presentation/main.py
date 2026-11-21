
from datetime import date

from flight_booking.infrastructure.email_adapter import EmailAdapter
from flight_booking.infrastructure.external_email_service import ExternalEmailService

from flight_booking.domain.flight import Flight
from flight_booking.domain.pricing_factory import PricingStrategyFactory
from flight_booking.application.flight_service import FlightService
from flight_booking.application.booking_service import BookingService
from flight_booking.infrastructure.in_memory_booking_repository import (
    InMemoryBookingRepository,
)


def main():
    flights = [
        Flight("TK101", "Istanbul", "London",
               date(2026, 12, 15), 200.0, 10),
        Flight("TK102", "Istanbul", "Paris",
               date(2026, 12, 16), 150.0, 8),
        Flight("TK103", "London", "Istanbul",
               date(2026, 12, 20), 220.0, 12),
    ]

    flight_service = FlightService(flights)
    booking_service = BookingService(
        InMemoryBookingRepository()
    )

    email_adapter = EmailAdapter(ExternalEmailService())


    while True:
       
        print("1. View all flights")
        print("2. Search flights")
        print("3. Book a flight")
        print("4. View my bookings")
        print("5. Cancel a booking")
        print("6. Exit")


        choice = input("Choose an option: ").strip()

        if choice == "1":
            for flight in flights:
                print(
                    f"{flight.flight_number}: "
                    f"{flight.origin} -> {flight.destination} | "
                    f"{flight.departure_date} | "
                    f"${flight.price:.2f} | "
                    f"Seats: {flight.available_seats}"
                )

        elif choice == "2":
            origin = input("From: ").strip()
            destination = input("To: ").strip()

            try:
                travel_date = date.fromisoformat(
                    input("Date (YYYY-MM-DD): ").strip()
                )
            except ValueError:
                print("Invalid date. Use YYYY-MM-DD.")
                continue

            results = flight_service.search_flights(
                origin, destination, travel_date
            )

            if not results:
                print("No available flights found.")
            else:
                for flight in results:
                    print(
                        f"{flight.flight_number}: "
                        f"{flight.origin} -> {flight.destination} | "
                        f"${flight.price:.2f}"
                    )

        elif choice == "3":
            flight_number = input(
                "Enter flight number: "
            ).strip().upper()

            flight = next(
                (f for f in flights
                 if f.flight_number == flight_number),
                None,
            )

            if flight is None:
                print("Flight not found.")
                continue

            passenger = input("Passenger name: ").strip()
            ticket_class = input(
                "Ticket class (Economy/Business/First Class): "
            ).strip()

            try:
                strategy = PricingStrategyFactory.create(
                    ticket_class
                )

                booking = booking_service.create_booking(
                    passenger,
                    flight,
                    strategy,
                    ticket_class,
                )

                print("\nBooking confirmed!")
                print(f"Booking ID: {booking.booking_id}")
                print(f"Passenger: {booking.passenger_name}")
                print(f"Class: {booking.ticket_class}")
                print(f"Total: ${booking.total_price:.2f}")

                email_adapter.send_confirmation(
                    "passenger@example.com",
                    f"Booking {booking.booking_id} confirmed "
                    f"for flight {booking.flight_number}. "
                    f"Total: ${booking.total_price:.2f}"
                )

            except ValueError as error:
                print(f"Booking failed: {error}")

      
        elif choice == "4":
            passenger = input(
                "Enter passenger name: "
            ).strip()

           
            try:
                bookings = booking_service.get_passenger_bookings(
                    passenger
                )
            except ValueError as error:
                print(f"Search failed: {error}")
                continue


            if not bookings:
                print("No bookings found.")
            else:
                for booking in bookings:
                    print(
                        f"\nBooking ID: {booking.booking_id}\n"
                        f"Flight: {booking.flight_number}\n"
                        f"Class: {booking.ticket_class}\n"
                        f"Price: ${booking.total_price:.2f}\n"
                        f"Status: {booking.status}"
                    )

        elif choice == "5":
            booking_id = input(
                "Enter booking ID: "
            ).strip()

            booking = booking_service.repository.find_by_id(
                booking_id
            )

            if booking is None:
                print("Booking not found.")
                continue

            flight = next(
                (
                    f for f in flights
                    if f.flight_number == booking.flight_number
                ),
                None,
            )

            if flight is None:
                print("Associated flight not found.")
                continue

            try:
                booking_service.cancel_booking(
                    booking_id, flight
                )
                print("Booking cancelled successfully!")
                print("One seat has been restored.")
            except ValueError as error:
                print(f"Cancellation failed: {error}")

        elif choice == "6":
            print("Goodbye!")
            break


        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

from datetime import date

from flight_booking.domain.flight import Flight
from flight_booking.domain.pricing_factory import PricingStrategyFactory
from flight_booking.application.flight_service import FlightService
from flight_booking.application.booking_service import BookingService
from flight_booking.infrastructure.in_memory_booking_repository import (
    InMemoryBookingRepository,
)


def main():
    flights = [
        Flight("TK101", "Istanbul", "London",
               date(2026, 12, 15), 200.0, 10),
        Flight("TK102", "Istanbul", "Paris",
               date(2026, 12, 16), 150.0, 8),
        Flight("TK103", "London", "Istanbul",
               date(2026, 12, 20), 220.0, 12),
    ]

    flight_service = FlightService(flights)
    booking_service = BookingService(
        InMemoryBookingRepository()
    )

    while True:
        print("\n=== FLIGHT BOOKING SYSTEM ===")
        print("1. View all flights")
        print("2. Search flights")
        print("3. Book a flight")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            for flight in flights:
                print(
                    f"{flight.flight_number}: "
                    f"{flight.origin} -> {flight.destination} | "
                    f"{flight.departure_date} | "
                    f"${flight.price:.2f} | "
                    f"Seats: {flight.available_seats}"
                )

        elif choice == "2":
            origin = input("From: ").strip()
            destination = input("To: ").strip()

            try:
                travel_date = date.fromisoformat(
                    input("Date (YYYY-MM-DD): ").strip()
                )
            except ValueError:
                print("Invalid date. Use YYYY-MM-DD.")
                continue

            results = flight_service.search_flights(
                origin, destination, travel_date
            )

            if not results:
                print("No available flights found.")
            else:
                for flight in results:
                    print(
                        f"{flight.flight_number}: "
                        f"{flight.origin} -> {flight.destination} | "
                        f"${flight.price:.2f}"
                    )

        elif choice == "3":
            flight_number = input(
                "Enter flight number: "
            ).strip().upper()

            flight = next(
                (f for f in flights
                 if f.flight_number == flight_number),
                None,
            )

            if flight is None:
                print("Flight not found.")
                continue

            passenger = input("Passenger name: ").strip()
            ticket_class = input(
                "Ticket class (Economy/Business/First Class): "
            ).strip()

            try:
                strategy = PricingStrategyFactory.create(
                    ticket_class
                )

                booking = booking_service.create_booking(
                    passenger,
                    flight,
                    strategy,
                    ticket_class,
                )

                print("\nBooking confirmed!")
                print(f"Booking ID: {booking.booking_id}")
                print(f"Passenger: {booking.passenger_name}")
                print(f"Class: {booking.ticket_class}")
                print(f"Total: ${booking.total_price:.2f}")

            except ValueError as error:
                print(f"Booking failed: {error}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

