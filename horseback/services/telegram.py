from telepot import Bot

from ..chatobjects import TextMessage


class Telegram:
    def __init__(self, key, *args, **kwargs):
        "Basic bot for Telegram sending messages"
        self._bot = Bot(key)
        self.service_type = "telegram"

    async def send_text_message(self, chat_id, text, **kwargs) -> TextMessage:
        # TODO figure out how to make this async
        json = self._bot.sendMessage(chat_id, text, **kwargs)
        return TextMessage(
            json,
            json['chat_id'],
            json['message_id'],
            json['text'],
        )
