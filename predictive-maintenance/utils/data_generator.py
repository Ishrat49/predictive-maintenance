import csv
import os
import random
import time
from datetime import datetime

DATA_FOLDER = "data"
FILE_PATH = os.path.join(DATA_FOLDER, "sensor_data.csv")

VEHICLE_ID = "AP09AB1234"

def generate_sensor_data(previous_mileage):
    """Generate realistic vehicle sensor values"""
    engine_temp = round(random.uniform(75, 110), 2)
    battery_voltage = round(random.uniform(10.5, 14.5), 2)
    vibration = round(random.uniform(0.2, 1.0), 2)
    mileage = previous_mileage + random.randint(1, 5)

    return {
        "vehicle_id": VEHICLE_ID,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "engine_temp": engine_temp,
        "battery_voltage": battery_voltage,
        "vibration": vibration,
        "mileage": mileage
    }

def write_to_csv(data):
    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Always enforce correct header
        if not file_exists:
            writer.writerow([
                "vehicle_id",
                "timestamp",
                "engine_temp",
                "battery_voltage",
                "vibration",
                "mileage"
            ])

        writer.writerow([
            data["vehicle_id"],
            data["timestamp"],
            data["engine_temp"],
            data["battery_voltage"],
            data["vibration"],
            data["mileage"]
        ])

def start_simulation():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    mileage = 40000  # starting mileage

    print("Starting vehicle sensor simulation...")
    while True:
        sensor_data = generate_sensor_data(mileage)
        mileage = sensor_data["mileage"]

        write_to_csv(sensor_data)
        print("Generated:", sensor_data)

        time.sleep(3)  # simulate data every 3 seconds

if __name__ == "__main__":
    start_simulation()
