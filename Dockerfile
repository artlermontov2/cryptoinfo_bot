FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt

ENV BOT_TOKEN=5717241467:AAHYLKwOGnDY7Dghb5B7bmu2V81QteLIhnc

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]