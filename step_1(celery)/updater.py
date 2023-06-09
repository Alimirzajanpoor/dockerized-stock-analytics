from celery import Celery
from celery import app, chain
import asyncio
import datetime
import redis
import json

app = Celery("updater", backend="rpc://", broker="amqp://localhost:5672")
r = redis.Redis(host="localhost", port=6379)


def convert_time_format(time_str):
    hours = int(time_str[:-4])
    minutes = int(time_str[-4:-2])
    seconds = int(time_str[-2:])
    formatted_time = f"{hours} {minutes:02d} {seconds:02d}"

    return formatted_time


def convert_time_string(time_string):
    time_format = "%H %M %S"
    time_obj = datetime.datetime.strptime(time_string, time_format).time()
    combined_datetime = datetime.datetime.combine(datetime.datetime.today(), time_obj)
    return combined_datetime


@app.task(bind=True)
def celery_schedule_todo(self, stock_value, stock_itself):
    r.set(stock_itself, json.dumps(stock_value))


async def schedule_todo(time_sec, stock_data_json, stock_itself):
    celery_schedule_todo.apply_async(args=(stock_data_json, stock_itself), eta=time_sec)


async def start_task(time_list, stock_data, stock_itself):
    eta = convert_time_string(convert_time_format(str(time_list)))
    print(eta)
    await schedule_todo(eta, stock_data, stock_itself)
