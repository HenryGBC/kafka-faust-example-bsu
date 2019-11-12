import faust
from faust.web import Request, Response, View
from config import WORKER_BROKER, TOPIC_ERP, TOPIC_NOTIF
import time

app = faust.App(
    'appERP',
    broker=WORKER_BROKER
)


@app.agent(TOPIC_ERP)
async def test(messages):
    async for data in messages:
        # if PROD:
        print('Processing data')

        for value in data['values']:
            print('Saving ', value)

        notification = {
            'company': data['company'],
            'value': 'Procesado'
        }
        await TOPIC_NOTIF.send(value=notification)
