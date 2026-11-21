
# Flight Booking System

## Software Design and Architecture Project

A Python-based flight booking application developed
to demonstrate software architecture principles,
SOLID principles, design patterns, and automated
testing.

## Features

- View available flights
- Search flights by route and departure date
- Create flight reservations
- Choose Economy, Business, or First Class
- Calculate ticket prices
- View passenger bookings
- Cancel reservations
- Restore seat availability after cancellation
- Generate simulated email confirmations
- Retry temporary notification failures

## Technology Stack

- Python
- uv (Python package manager)
- pytest (Automated testing)
- Git and GitHub
- Mermaid (UML and architecture diagrams)

## Project Architecture

The application uses a layered modular-monolith
architecture.

### Layers

1. Presentation — Command-line interface
2. Application — Business use cases
3. Domain — Business entities and interfaces
4. Infrastructure — Data storage and notifications

## Design Patterns

### Strategy Pattern
Used to implement interchangeable ticket pricing
algorithms for Economy, Business, and First Class.

### Simple Factory
Centralizes the creation of pricing strategies.

### Repository Pattern
Separates booking business logic from persistence.

### Adapter Pattern
Adapts the simulated external email provider
to the application's notification interface.

### Decorator Pattern
Adds retry behavior to notification delivery
without changing the email adapter.

## SOLID Principles

The system demonstrates separation of
responsibilities and dependency inversion.

BookingService depends on the abstract
BookingRepository interface rather than
a concrete storage implementation.

See docs/solid_refactoring.md for details.

## Installation

Clone the repository and navigate into
the project folder.

Install dependencies:

```bash
uv sync
```

## Run the Application

```bash
uv run python -m flight_booking.presentation.main
```

## Run Tests

```bash
uv run pytest -v
```

## Documentation

- docs/class_diagram.md
- docs/architecture_diagram.md
- docs/architecture.md
- docs/domain_model.md
- docs/bounded_context_diagram.md
- docs/quality_attributes.md
- docs/architecture_evaluation.md
- docs/solid_refactoring.md
- docs/decisions/0001-use-modular-monolith.md

## Architectural Decisions

The modular-monolith architecture was selected
to balance maintainability, simplicity,
and testability.

See the Architecture Decision Record in
docs/decisions/.

## Limitations

- Flights are stored in memory.
- Reservations are not persistent.
- Notifications are simulated.
- No real payment processing.
- No passenger authentication.
- Seat updates are not concurrency-safe.

## Future Improvements

- Database integration
- User authentication
- Web-based interface
- Real airline API integration
- Payment processing
- Concurrency-safe seat reservations

## Authors

Software Design and Architecture Project Team
