from telegram import Bot
from telegram.error import TelegramError
import os
import logging

class TelegramManager:
    def __init__(self):
        self.bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
        self.channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
        self.logger = logging.getLogger(__name__)

    async def post_video(self, video_path):
        try:
            with open(video_path, 'rb') as video_file:
                await self.bot.send_video(chat_id=self.channel_id, video=video_file, caption="\U0001F525 ¡Reacciona! \U0001F4E2 ¡Comparte!")
                return True

        except TelegramError as e:
            self.logger.error(f"Couldn't send the video! {e}")