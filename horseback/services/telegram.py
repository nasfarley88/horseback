from telepot import Bot


class Telegram:
    def __init__(self, key, *args, **kwargs):
        "Basic bot for Telegram sending messages"
        self._bot = Bot(key)
        self.service_type = "telegram"

    async def send_text_message(self, chat_id, text, **kwargs):
        # TODO figure out how to make this async
        self._bot.sendMessage(chat_id, text, **kwargs)
