from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

TEMP_VIDEO_FILENAME = "video.mp4"

class GoogleDriveManager():
    def __init__(self):
        gauth = GoogleAuth()
        gauth.LoadClientConfigFile(os.getenv('GDRIVE_CLIENT_SECRET_PATH'))
        gauth.LoadCredentialsFile(os.getenv('GDRIVE_CREDENTIALS_PATH'))
        if gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()
        gauth.SaveCredentialsFile(os.getenv('GDRIVE_CREDENTIALS_PATH'))
        
        self.videos_folder_id = os.getenv('GDRIVE_VIDEOS_PATH')
        self.db_backups_folder_id = os.getenv('GDRIVE_DB_BACKUPS_PATH')
        self.drive = GoogleDrive(gauth)

    def get_all_video_files(self):
        files = []
        gdrive_files = self.drive.ListFile({'q': f"'{self.videos_folder_id}' in parents and trashed=false"}).GetList()
        for file in gdrive_files:
            if file['title'].endswith(".mp4"):
                files.append((file['id'], file['title']))
        return files

    def download_file(self, file_id):
        file = self.drive.CreateFile({'id': file_id})
        file.GetContentFile(TEMP_VIDEO_FILENAME)
        return TEMP_VIDEO_FILENAME

    def upload_backup(self, filename):
        file = self.drive.CreateFile({'parents': [{'id': self.db_backups_folder_id}]})
        file.SetContentFile(filename)
        file.Upload()
