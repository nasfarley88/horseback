import unittest
import asyncio
import aiohttp
import yaml

from horseback.services.telegram import Telegram
from horseback import Horseback


class TestTelegramBot(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        self.config = yaml.load(open("test_config.yml"))

    def test_send_text_message(self) -> None:
        async def foo():
            # Set up the aiohttp session
            async with aiohttp.ClientSession() as session:

                # Set up the telegram service and horseback object
                self.bot = Telegram(session, self.config['telegram_key'])
                self.hb = Horseback([self.bot])

                # Send message
                await self.hb.send_text_message(
                    "telegram",
                    self.config['telegram_chat_id'],
                    self.config['sample_text'])

        self.loop.run_until_complete(foo())

    def test_get_updates(self) -> None:
        async def foo():
            # Set up the aiohttp session
            async with aiohttp.ClientSession() as session:

                # Set up the telegram service and horseback object
                self.bot = Telegram(session, self.config['telegram_key'])
                self.hb = Horseback([self.bot])

                # Get the bot updates
                msgs = await self.hb.get_updates("telegram")

                # Send a message confirming the bot updates.
                await msgs[-1].service.send_text_message(
                    msgs[-1].chat_id,
                    "Last message recieved: {}".format(
                        msgs[-1].text))

        self.loop.run_until_complete(foo())
