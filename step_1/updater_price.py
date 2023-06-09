import pandas as pd
import redis
import json

from datetime import datetime

url = (
    "https://raw.githubusercontent.com/amogadasi/python_django_test/main/price_data.csv"
)
casts = pd.read_csv(url)
r = redis.Redis(host="redis-1", port=6379)


def convert_time_string(time_string):
    time_format = "%H %M %S"
    time_obj = datetime.strptime(time_string, time_format).time()
    return time_obj


def convert_time_format(time_str):
    hours = int(time_str[:-4])
    minutes = int(time_str[-4:-2])
    formatted_time = f"{hours}:{minutes:02d}"

    return formatted_time


def main_func(stock):
    filtered = casts[casts["Stock"] == stock]

    for index, row in filtered.iterrows():
        date = row["Time"]
        stock = row["Stock"]
        price = row["Price"]

        print(f"Date: {date}, Stock: {stock}, Price: {price}")

        existing_row = r.get(stock)
        existing_value = json.loads(existing_row)
        price_list = existing_value["price"]
        price_list.append(price)
        time_list = existing_value["time"]
        time_list.append(convert_time_format(str(date)))

        data = existing_value
        r.set(stock, json.dumps(data))


column_stock = ["stock1", "stock2", "stock3"]
for i in column_stock:
    main_func(i)
