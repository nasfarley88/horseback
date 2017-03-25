from .chatobjects.textmessage import TextMessage
from .utils import ServicesDict


class Horseback:
    """Class used to interact with `ChatService`s.

    Horseback takes a list of `ChatService`s and uses them to interact with the
    service. If a service is not found, a ServiceNotFound exception is raised.

    """
    def __init__(self, services):
        self.services = ServicesDict({s.service_type: s for s in services})

    async def send_text_message(self,
                                service_type: str,
                                chat_id,
                                text: str,
                                **kwargs) -> TextMessage:
        """Send text message with named service."""

        service = self.services[service_type]
        return await service.send_text_message(chat_id, text, **kwargs)

    async def get_updates(self,
                          service_type: str,
                          **kwargs) -> list:

        """Get updates from named service.

        TODO make this function so that it acts like a single service. E.g. it
        will 'long poll' by long polling all the services and then as soon at
        it recieves udpates from one of them, it returns (cancelling the long
        polling of the other services).
        """

        service = self.services[service_type]
        return await service.get_updates(**kwargs)
