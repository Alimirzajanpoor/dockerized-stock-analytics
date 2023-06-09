# Stock Performance Update

This repository contains code for updating stock performance using concurrent processing. It includes the following files:

## main.py

This file serves as the entry point of the application. It retrieves stock data from a provided URL and updates the stock performance using concurrent processing.

- The code imports the necessary libraries, including pandas for data manipulation, redis for interacting with a Redis database, json for working with JSON data, concurrent.futures for concurrent processing, and time for simulating performance calculation.

- It defines utility functions `calculate_performance()` and `update_performance()` for calculating and updating the stock performance.

- The script reads stock data from a URL using pandas and initializes a Redis client to interact with a Redis database.

- The `compare_and_update_performance()` function compares the current price with the previous performance and calculates the new performance using the `calculate_performance()` function.

- The `process_stock()` function is responsible for processing each stock by calling `compare_and_update_performance()`.

- The script reads the stock data, initializes the Redis client, and defines a list of stocks.

- It utilizes concurrent processing with a `ProcessPoolExecutor` to map the `process_stock()` function to each stock, allowing for parallel execution.

Please note that this code utilizes concurrent processing to efficiently update stock performance. Ensure that Redis is running on `localhost:6379` before executing the code.

