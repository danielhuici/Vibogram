import schedule
import time
import logging


from sender_bot import SenderBot


if __name__ == "__main__":
    print("Telegram Autosender BOT is starting up!")

    sender_bot = SenderBot()
    sender_bot.send_periodical_video()
    schedule.every().day.at("18:00").do(sender_bot.send_periodical_video)
    schedule.every().day.at("22:00").do(sender_bot.send_periodical_video)
    schedule.every().day.at("00:00").do(sender_bot.send_periodical_video)
    schedule.every().day.at("02:00").do(sender_bot.send_periodical_video)

    schedule.every().day.at("05:00").do(sender_bot.backup_db)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
