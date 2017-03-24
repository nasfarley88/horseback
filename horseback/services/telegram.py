from ..chatobjects.textmessage import TextMessage


class Telegram:
    def __init__(self, session, key, *args, **kwargs):
        "Basic bot for Telegram sending messages"
        self.session = session
        self.key = key

        self.service_type = "telegram"

    async def send_text_message(self, chat_id, text, **kwargs) -> TextMessage:
        payload = {
            'chat_id': chat_id,
            'text': text,
            **kwargs
        }
        async with self.session.post(
                "https://api.telegram.org/bot{}/sendMessage".format(
                    self.key), data=payload) as resp:
            json = await resp.json()

        return TextMessage(
            json,
            json['result']['chat']['id'],
            json['result']['message_id'],
            json['result']['text'],
        )
