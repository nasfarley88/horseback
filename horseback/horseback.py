class Horseback:
    def __init__(self, services):
        self.services = {s.service_type: s for s in services}

    async def send_text_message(self, service_type, chat_id, text, **kwargs):
        service = self.services[service_type]
        # TODO get this to return a TextMessage type (whenever I get round to
        # making that type)
        return await service.send_text_message(chat_id, text, **kwargs)
