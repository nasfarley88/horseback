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
                                **kwargs):
        service = self.services[service_type]
        # TODO get this to return a TextMessage type (whenever I get round to
        # making that type)
        return await service.send_text_message(chat_id, text, **kwargs)
