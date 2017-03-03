import unittest
import asyncio
import yaml

from horseback.telegrambot import TelegramBot


class TestTelegramBot(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        self.config = yaml.load(open("test_config.yml"))
        self.bot = TelegramBot(self.config['telegram_key'])

    def test_send_text_message(self):
        async def foo():
            await self.bot.send_text_message(
                self.config['telegram_chat_id'],
                self.config['sample_text'])

        self.loop.run_until_complete(foo())
