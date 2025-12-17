import pandas as pd
import matplotlib.pyplot as plt
from health_score import calculate_health

DATA_PATH = "data/sensor_data.csv"

def generate_analytics():
    df = pd.read_csv(DATA_PATH)

    if df.empty:
        print("No data available")
        return

    # Compute health score for each row
    health_scores = []
    for _, row in df.iterrows():
        sensor_data = {
            "engine_temp": row.iloc[2],
            "battery_voltage": row.iloc[3],
            "vibration": row.iloc[4],
            "mileage": row.iloc[5]
        }
        health_scores.append(calculate_health(sensor_data))

    df["health_score"] = health_scores

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df.iloc[:, 1])

    # ---------- PLOTS ----------
    plt.figure()
    plt.plot(df["timestamp"], df.iloc[:, 2])
    plt.title("Engine Temperature Over Time")
    plt.xlabel("Time")
    plt.ylabel("Engine Temperature")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/engine_temp.png")

    plt.figure()
    plt.plot(df["timestamp"], df.iloc[:, 3])
    plt.title("Battery Voltage Over Time")
    plt.xlabel("Time")
    plt.ylabel("Battery Voltage")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/battery_voltage.png")

    plt.figure()
    plt.plot(df["timestamp"], df.iloc[:, 4])
    plt.title("Vibration Level Over Time")
    plt.xlabel("Time")
    plt.ylabel("Vibration")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/vibration.png")

    plt.figure()
    plt.plot(df["timestamp"], df["health_score"])
    plt.title("Vehicle Health Score Trend")
    plt.xlabel("Time")
    plt.ylabel("Health Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/health_score.png")

    print("Analytics graphs generated successfully")
