import faust
from config import WORKER_BROKER, TOPIC_ERP, TOPIC_NOTIF
import time

app = faust.App(
    'appERP',
    broker=WORKER_BROKER
)


@app.agent(TOPIC_NOTIF)
async def test(messages):
    async for data in messages:
        # if PROD:
        print('Receiving data')
        send_email(data)
        send_sms(data)


def send_email(data):
    print('Sending email to ', data['company'])


def send_sms(data):
    print('Sending sms to ', data['company'])
