import abc

from .chatobjects.textmessage import TextMessage


class ChatService(metaclass=abc.ABCMeta):
    def __init__(self, service_type):
        self.service_type = service_type

    @abc.abstractmethod
    async def send_text_message(self,
                                chat_id,
                                text: str,
                                **kwargs) -> TextMessage:
        """Should send a text message via this service.

        kwargs should be passed to the function sending the text message.

        """

    @abc.abstractmethod
    async def json2textmessage(self, json: dict) -> TextMessage:
        """Should take a JSON object and create a TextMessage object."""

    @abc.abstractmethod
    async def get_updates(self, **kwargs):
        """Should get updates from the service."""
