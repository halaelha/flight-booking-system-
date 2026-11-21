
import pytest

from flight_booking.domain.notification_service import (
    NotificationService,
)
from flight_booking.infrastructure.retry_notification import (
    RetryNotification,
)


class FakeNotificationService(NotificationService):

    def __init__(self, failures_before_success=0):
        self.attempts = 0
        self.failures_before_success = failures_before_success

    def send_confirmation(self, recipient, message):
        self.attempts += 1

        if self.attempts <= self.failures_before_success:
            raise ConnectionError("Temporary email failure")


def test_retry_succeeds_after_failure():
    fake = FakeNotificationService(
        failures_before_success=2
    )

    retry = RetryNotification(
        fake, max_attempts=3, delay=0
    )

    retry.send_confirmation("sara@example.com", "Confirmed")

    assert fake.attempts == 3


def test_retry_stops_after_max_attempts():
    fake = FakeNotificationService(
        failures_before_success=10
    )

    retry = RetryNotification(
        fake, max_attempts=3, delay=0
    )

    with pytest.raises(ConnectionError):
        retry.send_confirmation(
            "sara@example.com", "Confirmed"
        )

    assert fake.attempts == 3
