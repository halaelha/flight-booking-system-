
# Flight Booking System — Bounded Context Diagram

```mermaid
flowchart TD
    A["Flight Management Context"]
    B["Booking Management Context"]
    C["Pricing Context"]
    D["Notification Integration"]

    A -->|"Flight details and availability"| B
    B -->|"Request price calculation"| C
    B -->|"Request booking confirmation"| D
```

## Description

The system is divided into three conceptual
bounded contexts.

Flight Management provides flight information.

Booking Management manages reservations and
seat availability changes.

Pricing provides interchangeable pricing
strategies.

Notification handling is a supporting
integration rather than a separate deployed
service.
