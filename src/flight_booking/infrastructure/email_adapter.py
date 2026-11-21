
from flight_booking.domain.notification_service import (
    NotificationService,
)
from flight_booking.infrastructure.external_email_service import (
    ExternalEmailService,
)


class EmailAdapter(NotificationService):

    def __init__(self, email_service: ExternalEmailService):
        self.email_service = email_service

    def send_confirmation(
        self, recipient: str, message: str
    ) -> None:
        self.email_service.send_email(recipient, message)
