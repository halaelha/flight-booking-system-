
from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def send_confirmation(
        self, recipient: str, message: str
    ) -> None:
        pass
