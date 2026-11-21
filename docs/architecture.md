# Flight Booking System — Architecture Overview

## Architectural Style

The Flight Booking System uses a layered modular-monolith architecture.

## Layers

**Presentation Layer:** Provides a command-line interface for searching flights, creating reservations, viewing bookings, and cancelling reservations.

**Application Layer:** Coordinates the application's use cases through `FlightService` and `BookingService`.

**Domain Layer:** Contains the core business entities, pricing strategies, and repository abstractions.

**Infrastructure Layer:** Implements in-memory persistence and simulated email integration.

## Why a Modular Monolith?

A modular monolith was selected because the project is relatively small and does not require independent deployment of its components.

The approach provides clear separation of responsibilities without the operational complexity of microservices.

## Advantages

- Simple development and deployment.
- Easier testing and debugging.
- Clear separation of responsibilities.
- Reduced infrastructure complexity.
- Supports future replacement of persistence and external integrations.

## Limitations

- Components are deployed together.
- Data is currently stored in memory and does not survive application restarts.
- Seat changes are not protected by transactional concurrency controls.
- The prototype does not include authentication or real payment processing.

## Future Improvements

Potential extensions include persistent database storage, authenticated users, atomic seat inventory updates, and integration with real notification services.
