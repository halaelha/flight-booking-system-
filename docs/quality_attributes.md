
# Quality Attributes and Resilience

## Reliability

The Flight Booking System should remain functional
when the notification service experiences a
temporary failure.

### Quality Attribute Scenario

- Source: External email notification provider
- Stimulus: Temporary connection failure
- Environment: After a successful flight booking
- Artifact: Notification component
- Response: Retry sending the confirmation
- Response Measure: At most three attempts

## Architectural Solution

We introduced RetryNotification, which wraps the
EmailAdapter and retries transient failures.

The retry mechanism handles ConnectionError and
TimeoutError.

If all attempts fail, the application informs the
user that the booking is confirmed but notification
delivery was unsuccessful.

## Benefits

- Improves tolerance of temporary service failures.
- Prevents unlimited retry attempts.
- Separates resilience behavior from the email adapter.
- Allows retry behavior to be tested independently.

## Limitations

- Notifications are simulated rather than sent.
- Failed notifications are not stored for later delivery.
- No exponential backoff is implemented.
- Retry attempts may cause duplicate notifications
  if the provider completes a request but the
  response is lost.

## Verification

Automated tests simulate temporary notification
failures and verify that retries stop after the
configured maximum number of attempts.
