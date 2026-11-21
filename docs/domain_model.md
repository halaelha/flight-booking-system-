
# Flight Booking System — Domain Model

## Overview

The Flight Booking System contains three
conceptual bounded contexts:

1. Flight Management
2. Booking Management
3. Pricing

These contexts separate different business
responsibilities within the application.

## 1. Flight Management

### Responsibilities

- Store flight information.
- Search flights by origin and destination.
- Check departure dates.
- Check seat availability.

### Main Classes

- Flight
- FlightService

### Important Business Rule

A flight is available when its available_seats
value is greater than zero.

## 2. Booking Management

### Responsibilities

- Create reservations.
- Store booking information.
- Cancel reservations.
- Restore seats after cancellation.
- Retrieve bookings.

### Main Classes

- Booking
- BookingService
- BookingRepository

### Important Business Rules

- A passenger name cannot be empty.
- A booking cannot be created if no seats remain.
- Creating a booking reduces available seats by one.
- Cancelling a confirmed booking restores one seat.
- A booking cannot be cancelled twice.

## 3. Pricing

### Responsibilities

- Calculate ticket prices.
- Support different ticket classes.
- Allow pricing algorithms to be replaced.

### Main Classes

- PricingStrategy
- EconomyPricing
- BusinessPricing
- FirstClassPricing
- PricingStrategyFactory

### Pricing Rules

- Economy: Base price
- Business: Base price multiplied by 1.5
- First Class: Base price multiplied by 2

## Context Relationships

Flight Management provides flight information
and seat availability to Booking Management.

Booking Management uses Pricing to calculate
the ticket price during reservation creation.

Notifications are handled by a supporting
infrastructure integration.

## Current Limitations

The bounded contexts are logical design
boundaries rather than fully isolated
software modules.

Booking Management currently modifies the
available_seats attribute of a Flight object
directly.

Future versions could introduce clearer
interfaces between these contexts.
