from __future__ import unicode_literals

from dotenv import load_dotenv
import schedule
import time
import logging

from common.utils import configure_logger
from sender_bot import SenderBot


if __name__ == "__main__":
    load_dotenv()
    configure_logger()
    logger = logging.getLogger(__name__)

    logger.info("Telegram Autosender BOT is starting up!")

    sender_bot = SenderBot()

    schedule.every().day.at("15:00").do(sender_bot.send_periodical_video)
    schedule.every().day.at("22:00").do(sender_bot.send_periodical_video)
    schedule.every().day.at("23:00").do(sender_bot.backup_db)
    
    schedule.run_all() # Run everything on the beginning
    while True:
        schedule.run_pending()
        time.sleep(1)