import pandas as pd
import redis
from datetime import datetime
import json
import updater
import asyncio


def convert_time_string(time_string):
    time_format = "%H %M %S"
    time_obj = datetime.strptime(time_string, time_format).time()
    return time_obj


def convert_time_format(time_str):
    hours = int(time_str[:-4])
    minutes = int(time_str[-4:-2])
    seconds = int(time_str[-2:])
    formatted_time = f"{hours} {minutes:02d} {seconds:02d}"

    return formatted_time


url = (
    "https://raw.githubusercontent.com/amogadasi/python_django_test/main/price_data.csv"
)
r = redis.Redis(host="localhost", port=6379)

for key in r.scan_iter():
    value = r.get(key)
    print(value)
    print(key)


casts = pd.read_csv(url)


def loop_stocks(stock):
    for index, row in filtered.iterrows():
        filtered = casts[casts["Stock"] == stock]

        date = row["Time"]
        price = row["Price"]

        existing_row = r.get("stock1")
        existing_value = json.loads(existing_row)
        price_list = existing_value["price"]
        price_list.append(price)
        time_list = existing_value["time"]
        time_list.append(convert_time_format(str(date)))

        asyncio.run(updater.start_task(date, existing_value, stock))


column_stock = ["stock1", "stock2", "stock3"]
for i in column_stock:
    loop_stocks(i)
