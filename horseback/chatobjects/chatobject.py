class ChatObject:
    def __init__(self, service, json):
        """Base class for objects emmitted from chat services."""
        self.json = json
        self.service = service
