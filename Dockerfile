FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt

ENV BOT_TOKEN=YOUR_BOT_TOKEN

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]
