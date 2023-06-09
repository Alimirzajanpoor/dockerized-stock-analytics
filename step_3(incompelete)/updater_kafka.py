from kafka import KafkaProducer, KafkaConsumer
import csv
import requests


bootstrap_servers = ["kafka:9092"]
topic_name = "main_topic"


github_csv_url = (
    "https://raw.githubusercontent.com/amogadasi/python_django_test/main/price_data.csv"
)
delimiter = ","


def produce_csv_data():
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    response = requests.get(github_csv_url)
    response.raise_for_status()

    csv_data = response.text.splitlines()

    reader = csv.reader(csv_data, delimiter=delimiter)
    headers = next(reader)

    for row in reader:
        timestamp = row[0]
        price = row[1]

        kafka_message = f"{timestamp},{price}".encode("utf-8")

        producer.send(topic_name, value=kafka_message)

        print(f"Produced message: {kafka_message}")

    producer.flush()
    producer.close()


if __name__ == "__main__":
    produce_csv_data()
