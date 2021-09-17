import csv
import datetime
import os
import time

import dotenv
import requests

dotenv.load_dotenv(".env")

WEATHER_STATION_API_URL = os.environ.get("WEATHER_STATION_API_URL")
WEATHER_STATION_API_ENDPOINT = os.environ.get("WEATHER_STATION_API_ENDPOINT")
CSV_SAVE_LOCATION = os.environ.get("CSV_SAVE_LOCATION")
POLLING_TIME = int(os.environ.get("POLLING_TIME"))


def create_data_save_location():
    if not os.path.exists(CSV_SAVE_LOCATION):
        os.makedirs(CSV_SAVE_LOCATION)


def request_data():
    headers = {"Content-Type": "application/json; charset=utf-8"}

    req = requests.get(
        WEATHER_STATION_API_URL + WEATHER_STATION_API_ENDPOINT, headers=headers
    )

    results = req.json()

    weather_station_header = ["date", "time"] + [
        f"{result['type']} ({result['unit']})" for result in results
    ]
    weather_station_data = [
        datetime.date.today(),
        datetime.datetime.now().strftime("%H:%M:%S"),
    ] + [result["value"] for result in results]

    return weather_station_header, weather_station_data


def does_file_exist(file):
    return os.path.exists(file)


def data_writer(header, data):
    create_data_save_location()
    data_file_name = f"{CSV_SAVE_LOCATION}data_{datetime.date.today()}.csv"
    should_add_header = not does_file_exist(data_file_name)

    with open(data_file_name, "a") as data_file:
        writer = csv.writer(data_file)

        if should_add_header:
            print(f"Writing header {header} to CSV {data_file_name}")
            writer.writerow(header)

        print(f"Writing data {data} to CSV {data_file_name}")
        writer.writerow(data)


if __name__ == "__main__":
    while True:
        header, data = request_data()
        data_writer(header, data)

        print("Sleeping for 30 seconds")
        time.sleep(POLLING_TIME)
