# Dockerized Stock Analytics

This repository contains code for performing stock analytics tasks using Docker. It includes the following files:

## main.py

This file is the entry point of the application. It performs stock analytics on the provided data.

- The code imports the necessary libraries, including pandas for data manipulation, redis for interacting with a Redis database, datetime for handling date and time values, and json for working with JSON data.

- It defines utility functions `convert_time_string()` and `convert_time_format()` to manipulate time-related values.

- The script retrieves stock data from a URL and filters it based on a specific condition.

- It then iterates over the filtered data and performs operations on each row, such as printing the values of each column.

- It retrieves existing stock data from a Redis database, updates it with the new price and time values, and stores the updated data back in Redis.

## updater.py

This file provides functionality for updating stock data using Celery for asynchronous task scheduling.

- The code imports the necessary libraries, including Celery for task scheduling, asyncio for asynchronous operations, datetime for working with date and time values, redis for interacting with a Redis database, and json for handling JSON data.

- It defines the `celery_schedule_todo()` function as a Celery task. This function stores stock values in a Redis database.

- The script defines the `schedule_todo()` function to schedule Celery tasks asynchronously.

- It also defines the `start_task()` function, which converts time values, schedules tasks using Celery, and updates stock data in Redis.

Please note that Celery is used in this project to simulate the updating scenario by scheduling tasks asynchronously.
