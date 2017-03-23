import unittest
import asyncio
import yaml

from horseback.services.telegram import Telegram
from horseback import Horseback


class TestTelegramBot(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        self.config = yaml.load(open("test_config.yml"))
        self.bot = Telegram(self.config['telegram_key'])
        self.hb = Horseback([self.bot])

    def test_send_text_message(self):
        async def foo():
            await self.hb.send_text_message(
                "telegram",
                self.config['telegram_chat_id'],
                self.config['sample_text'])

        self.loop.run_until_complete(foo())
