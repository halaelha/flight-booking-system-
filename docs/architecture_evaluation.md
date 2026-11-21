
# Flight Booking System — Architecture Evaluation

## Architecture

The project uses a layered modular-monolith
architecture.

## Quality Attributes

### Maintainability

Business logic is separated from the
presentation and infrastructure layers.

The Repository Pattern allows persistence
implementations to change independently
of booking operations.

### Extensibility

The Strategy Pattern allows new pricing
algorithms to be introduced.

The Adapter Pattern supports integration
with external notification providers.

### Testability

Automated tests verify flight search,
pricing, booking creation, cancellation,
repository operations, and failure handling.

### Reliability

The system validates important booking rules,
including seat availability and passenger names.

Notification retries handle temporary
connection failures.

## Architecture Trade-offs

### Advantages

- Simple deployment.
- Clear separation of responsibilities.
- Easier testing.
- Lower complexity than microservices.
- Supports adding new pricing strategies.

### Disadvantages

- No persistent database.
- No authentication.
- No atomic transactions for seat inventory.
- Application components deploy together.
- In-memory data is lost after restart.

## Future Improvements

1. Add persistent database storage.
2. Introduce authenticated passenger accounts.
3. Add concurrency-safe seat reservation.
4. Add notification delivery tracking.
5. Introduce structured logging.

## Conclusion

The modular-monolith architecture is appropriate
for the current scope of the Flight Booking System.

It balances simplicity with separation of
responsibilities and provides a foundation for
future extensions.
