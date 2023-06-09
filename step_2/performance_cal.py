import pandas as pd
import redis
import json
import concurrent.futures
import time

url = (
    "https://raw.githubusercontent.com/amogadasi/python_django_test/main/price_data.csv"
)
casts = pd.read_csv(url)
redis_client = redis.Redis(host="redis-1", port=6379)


def calculate_performance(stock_price):
    time.sleep(3)
    return 0


def update_performance(stock, performance):
    current_row = json.loads(redis_client.get(stock))
    current_row["performance"] = performance

    redis_client.set(stock, json.dumps(current_row))


def compare_and_update_performance(stock):
    loaded_row = json.loads(redis_client.get(stock))["price"]

    current_price_index = len(loaded_row) - 1

    current_price = loaded_row[current_price_index]

    previous_performance = json.loads(redis_client.get(stock))["performance"]

    if current_price == previous_performance:
        return

    new_performance = calculate_performance(current_price)

    update_performance(stock, new_performance)


def process_stock(stock):
    compare_and_update_performance(stock)


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/amogadasi/python_django_test/main/price_data.csv"
    price_data = pd.read_csv(url)
    redis_client = redis.Redis(host="localhost", port=6379)

    stocks = ["stock1", "stock2", "stock3"]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_stock, stocks)
