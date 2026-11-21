
from flight_booking.infrastructure.email_adapter import EmailAdapter
from flight_booking.infrastructure.external_email_service import (
    ExternalEmailService,
)


def test_email_adapter(capsys):
    external_service = ExternalEmailService()
    adapter = EmailAdapter(external_service)

    adapter.send_confirmation(
        "sara@example.com",
        "Your flight booking is confirmed!",
    )

    output = capsys.readouterr().out

    assert "sara@example.com" in output
    assert "Your flight booking is confirmed!" in output

