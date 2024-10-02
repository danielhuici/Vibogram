# Vibogram

Vibogram is a Telegram bot that automatically posts videos to a Telegram channel. It connects to your Google Drive folder, downloads a random video, and posts it to the specified. It also keeps track of the downloaded videos using a PostgreSQL database to ensure that videos are not repeated.

## Features

- **Google Drive Integration**: Connects directly to your Google Drive folder to fetch video files.
- **Random Video Selection**: Downloads and posts a random video from your designated folder.
- **Configurable schedule**: Automatically sends the selected video following the specified schedule.
- **Tracking**: Maintains a record of all downloaded videos to avoid repetition.

## Installation

### Prerequisites

- Python 3.6 or higher
- PostgreSQL
- Google Drive API credentials
- Telegram Bot token

### Steps to Deploy

1. **Clone the repository**:
```bash
git clone https://github.com/danielhuici/videobot.git
cd videobot
```

3. **Install the required dependencies**:
```bash
pip install -r requirements.txt
```

5. **Set up your environment variables**:
```env
DB_HOST=YOUR_DB_HOST
DB_PORT=YOUR_DB_PORT
DB_USER=YOUR_DB_USER
DB_NAME=YOUR_DB_NAME
PGPASSWORD=YOUR_DB_PASSWORD

GDRIVE_CLIENT_SECRET_PATH=YOUR_GOOGLEDRIVE_CLIENT_SECRET_FILE_PATH
GDRIVE_CREDENTIALS_PATH=YOUR_GOOGLEDRIVE_CREDENTIALS_FILE_PATH
GDRIVE_VIDEOS_PATH=YOUR_GOOGLEDRIVE_VIDEOS_FOLDER_ID
GDRIVE_DB_BACKUPS_PATH=YOUR_GOOGLEDRIVE_DESTINATON_DB_BACKUPS_FOLDER_ID

TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN_ID
TELEGRAM_CHANNEL_ID=@YOUR_TELEGRAM_CHANNEL_ID
```

6. **Run the bot**:
```bash
   python3 main.py
```

## Docker Deployment

To deploy Vibogram using Docker, run:
````
docker-compose up -d
````
## Usage

Once deployed, the bot will automatically begin fetching random videos from your Google Drive folder and posting them to your Telegram channel according to the configured schedule. The PostgreSQL database will track which videos have already been sent.

## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and submit a pull request. Any enhancements, bug fixes, or suggestions are appreciated.

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details.

## Contact

For inquiries or support, please contact:
- Your Name: danielhuici@hotmail.com
- GitHub: [danielhuici](https://github.com/danielhuici)
