import faust
from faust.web import Request, Response, View
from config import WORKER_BROKER, TOPIC_ERP
import time

app = faust.App(
    'appERP',
    broker=WORKER_BROKER
)


