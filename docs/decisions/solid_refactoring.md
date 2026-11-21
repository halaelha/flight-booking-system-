# SOLID Refactoring: Dependency Inversion Principle

## Problem

Initially, the `BookingService` class stored bookings directly in a Python list.

This tightly coupled the booking business logic to its storage implementation.

## Before Refactoring

```python
class BookingService:
    def __init__(self):
        self.bookings = []
```

The service was responsible for both booking operations and managing stored bookings.

## After Refactoring

We introduced a `BookingRepository` abstraction and a separate `InMemoryBookingRepository` implementation.

```python
class BookingService:
    def __init__(self, repository: BookingRepository):
        self.repository = repository
```

The service now interacts with the repository through an abstract interface.

## SOLID Principle Applied

**Dependency Inversion Principle (DIP):** High-level modules should depend on abstractions rather than concrete low-level implementations.

## Benefits

- Reduced coupling between business logic and data storage.
- Improved unit testability.
- Easier replacement of in-memory storage with a database.
- Clearer separation of responsibilities.

## Trade-offs

The new design introduces additional classes and interfaces, but the flexibility is useful for future extensions.

## Verification

Automated tests verify booking creation, retrieval, cancellation, and repository behavior.
