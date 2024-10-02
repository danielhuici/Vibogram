FROM  ubuntu:latest

WORKDIR /root/telegram-autosender-bot

COPY . .
RUN apt update -y
RUN apt install -y python3 python3-pip libpq-dev postgresql-client
RUN pip install --break-system-packages -r requirements.txt

CMD ["python3", "main.py"]
