import psycopg2
import subprocess
import os
from datetime import date
from common.utils import debug_mode
import logging

SQL_GET_ALL_VIDEOS = "SELECT * FROM videos"
SQL_INSERT_VIDEO = "INSERT INTO videos (file_id, filename, date) VALUES (%s, %s, %s)"

class DBManager():
    def __init__(self):
        self.connection = psycopg2.connect(
                        database = os.getenv('DB_NAME'),
                        host = os.getenv('DB_HOST'),
                        user = os.getenv('DB_USER'),
                        password = os.getenv('PGPASSWORD'),
                        port = os.getenv('DB_PORT'))
        self.cursor = self.connection.cursor()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Database connection successful")

    def get_all_videos(self):
        self.cursor.execute(SQL_GET_ALL_VIDEOS)
        rows = self.cursor.fetchall()
        filenames = []
        for row in rows:
            filenames.append(row[0:2])

        return filenames

    def insert_video(self, file_id, filename, timestamp): 
        tuple = (file_id, filename, timestamp)
        self.cursor.execute(SQL_INSERT_VIDEO, tuple)
        self.connection.commit()


    def generate_sql_backup(self):
        filename = f"tgautosender_{date.today()}.sql"
        command = ["pg_dump", "-h", os.getenv('DB_HOST'), "-p", os.getenv('DB_PORT'),
                   "-Fc", "-b", "-U", os.getenv('DB_USER'), "-d", os.getenv('DB_NAME'),
                   "-f", filename]
        
        subprocess.run(command)   
         
        return filename

