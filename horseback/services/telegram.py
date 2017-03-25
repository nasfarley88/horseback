from ..chatobjects.textmessage import TextMessage


class Telegram:
    def __init__(self, session, key, *args, **kwargs):
        """Basic ChatService for Telegram."""
        self.session = session
        self.key = key

        self.service_type = "telegram"

    # Helper funtions
    async def _get(self, endpoint, **kwargs):
        """Use GET with telegram bot api and return json."""
        async with self.session.get(
                "https://api.telegram.org/bot{}/{}".format(
                    self.key, endpoint), **kwargs) as resp:
            return await resp.json()

    async def _post(self, endpoint, payload, **kwargs):
        """Use POST with telegram bot api and return json."""
        async with self.session.post(
                "https://api.telegram.org/bot{}/{}".format(
                    self.key, endpoint), data=payload, **kwargs) as resp:
            return await resp.json()

    # Methods that are needed
    async def json2textmessage(self, json: dict) -> TextMessage:
        """Takes JSON from telegram and creates a TextMessage object."""
        return TextMessage(
            self, 
            json,
            json['chat']['id'],
            json['message_id'],
            json['text'],
        )

    async def send_text_message(self,
                                chat_id,
                                text: str,
                                **kwargs) -> TextMessage:
        """Send a text message using the telegram bot API."""
        payload = {
            'chat_id': chat_id,
            'text': text,
            **kwargs
        }
        json = await self._post("sendMessage", payload)

        return await self.json2textmessage(json['result'])

    async def get_updates(self,
                          *,
                          timeout: int=10,
                          allowed_updates=('message',),
                          **kwargs) -> list:
        """Gets updates from telegram bot API.

        Keyword arguments are passed as data with the GET request.

        See https://core.telegram.org/bots/api#getupdates for more details.

        """

        json = await self._get("getUpdates",
                               data={
                                   'allowed_updates': allowed_updates,
                                   'timeout': timeout,
                                   **kwargs,
                               })

        msgs = json['result']
        return [await self.json2textmessage(m['message']) for m in msgs]
