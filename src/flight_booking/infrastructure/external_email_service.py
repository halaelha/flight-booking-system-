
class ExternalEmailService:

    def send_email(self, address: str, body: str) -> None:
        print(f"Sending email to {address}: {body}")

