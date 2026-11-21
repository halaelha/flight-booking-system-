
# ADR 0001: Use a Modular Monolith Architecture

## Status
Accepted

## Context

The Flight Booking System allows passengers to
search flights, create bookings, calculate ticket
prices, and cancel reservations.

The system includes several responsibilities:

- Flight management
- Booking management
- Ticket pricing
- Notification handling

We need an architecture that supports separation
of responsibilities, maintainability, and testing.

Two architectural approaches were considered:

1. Modular Monolith
2. Microservices

## Decision

We have chosen a modular monolith architecture
for the Flight Booking System.

The application is organized into four layers:

- Presentation
- Application
- Domain
- Infrastructure

All components run within one Python application.

## Reasons

1. The project is relatively small.
2. Deployment is simpler than microservices.
3. Separate modules support maintainability.
4. Testing and debugging are easier.
5. We can demonstrate SOLID and design patterns
   without distributed-system complexity.

## Consequences

### Positive

- Clear separation of responsibilities.
- Simple deployment.
- Easier automated testing.
- Lower infrastructure complexity.
- Easier development for a small team.

### Negative

- Components cannot be deployed independently.
- A failure in one process can affect the
  entire application.
- Scaling individual components is more difficult.

## Alternatives Considered

### Microservices

We considered separating flight searching,
booking management, and notifications into
independently deployed services.

This could allow independent deployment and
scaling, but would require additional networking,
service communication, and deployment management.

For the current project scope, this complexity
is not justified.

## Review

The decision may be revisited if the system
grows significantly or requires independent
deployment of its components.
