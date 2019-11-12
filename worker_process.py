import faust
from faust.web import Request, Response, View
from config import WORKER_BROKER, TOPIC_ERP
import time

app = faust.App(
    'appProcess',
    broker=WORKER_BROKER
)
# python worker.py worker -l info --web-port=6067

@app.page('/data')
class SendData(View):
    async def put(self, request: Request) -> Response:
        new_res = Response()
        new_res.json = await request.json()
        print(new_res.json)
        time.sleep(5)

        data = self.process_data(new_res.json)

        await TOPIC_ERP.send(value=data)

        return self.json({'response': 200})

    def process_data(self, data):

        values = [
            {'name_one': 24578},
            {'name_two': 24578},
            {'name_third': 24578},
            {'name_four': 24578},
        ]

        data['values'] = values

        return data



if __name__ == '__main__':
    app.main()
