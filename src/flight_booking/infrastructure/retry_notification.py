
import time

from flight_booking.domain.notification_service import (
    NotificationService,
)


class RetryNotification(NotificationService):

    def __init__(
        self,
        notification_service: NotificationService,
        max_attempts: int = 3,
        delay: float = 0.1,
    ):
        if max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")

        self.notification_service = notification_service
        self.max_attempts = max_attempts
        self.delay = delay

    def send_confirmation(
        self, recipient: str, message: str
    ) -> None:

        for attempt in range(1, self.max_attempts + 1):
            try:
                self.notification_service.send_confirmation(
                    recipient, message
                )
                return

            except (ConnectionError, TimeoutError):
                if attempt == self.max_attempts:
                    raise

                time.sleep(self.delay)
