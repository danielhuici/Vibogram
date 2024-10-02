from managers.db_manager import DBManager
from managers.google_drive_manager import GoogleDriveManager
from managers.telegram_manager import TelegramManager
from datetime import datetime
import logging
import random
import asyncio
import os

class SenderBot():
    def __init__(self):
        self.db_manager = DBManager()
        self.gdrive_manager = GoogleDriveManager()
        self.telegram_manager = TelegramManager()
        self.loop = asyncio.get_event_loop()
        self.logger = logging.getLogger(__name__)

    def send_periodical_video(self):
        gdrive_video_files = self.gdrive_manager.get_all_video_files()
        already_sended_videos = self.db_manager.get_all_videos()

        pending_videos = set(gdrive_video_files).difference(already_sended_videos)
        video_id, filename = random.choice(list(pending_videos))
        self.logger.info(f"Posting video {filename}")
        video_path = self.gdrive_manager.download_file(video_id)
        success = self.loop.run_until_complete(self.telegram_manager.post_video(video_path))
        if success:
            self.db_manager.insert_video(video_id, filename, datetime.now())
            os.remove(video_path)

    def backup_db(self):
        filename = self.db_manager.generate_sql_backup()
        self.gdrive_manager.upload_backup(filename)
        os.remove(filename)
