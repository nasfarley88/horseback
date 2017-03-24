from .chatobject import ChatObject


class TextMessage(ChatObject):
    """Represents a text message recieved from a service.

    TextMessage objects should not be instantiated directly. They should only
    come from services or service member functions.

    """
    def __init__(self, json, chat_id, message_id, text):
        super().__init__(json)
        self.message_id = message_id
        self.chat_id = chat_id
        self.text = text
