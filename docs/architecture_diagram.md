
# Flight Booking System — Architecture Diagram

```mermaid
flowchart TD
    A["Presentation Layer: main.py"]
    B["Application Layer: FlightService and BookingService"]
    C["Domain Layer: Flight, Booking, PricingStrategy"]
    D["Infrastructure: InMemoryBookingRepository"]
    E["Infrastructure: EmailAdapter"]
    F[("In-Memory Booking Data")]
    G["Simulated Email Service"]

    A --> B
    A --> E
    B --> C
    B -->|"Repository Interface"| D
    D -->|"Implements domain interface"| C
    D --> F
    E --> G
```

## Architecture Description

The Flight Booking System uses a layered modular-monolith architecture.

- Presentation Layer: Handles user input through the terminal.
- Application Layer: Manages flight searching and bookings.
- Domain Layer: Defines business models and interfaces.
- Infrastructure Layer: Handles storage and simulated email notifications.

## Architectural Decision

A modular monolith was selected because the system is small
and does not require independently deployed services.

This architecture supports separation of responsibilities,
maintainability, and testability.
