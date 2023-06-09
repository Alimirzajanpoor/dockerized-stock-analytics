import pandas as pd
import redis
from datetime import datetime
import json


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
filtered = casts[casts["Stock"] == "stock1"]

# print(time_stock1)
# updater.start_task(time_stock1)
# print(df)

print(filtered)

for index, row in filtered.iterrows():
    # Access the values of each column in the current row
    date = row["Time"]
    stock = row["Stock"]
    price = row["Price"]

    # Perform further operations or analysis on the row data
    # For example, print the values of each column
    print(f"Date: {date}, Stock: {stock}, Price: {price}")

    existing_row = r.get("stock1")
    existing_value = json.loads(existing_row)
    price_list = existing_value["price"]
    price_list.append(price)
    time_list = existing_value["time"]
    time_list.append(convert_time_format(str(date)))

    data = existing_value
    # print(type(stock_data_json))
    # Process the time value
    # asyncio.run(updater.start_task(str(date), data, "stock1"))
# celery -A myapp.celeryapp worker --loglevel=info -P eventlet
