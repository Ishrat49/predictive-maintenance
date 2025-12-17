def calculate_health(sensor_data):
    """
    Calculate vehicle health score based on sensor values.
    Returns a score between 0 and 100.
    """

    score = 100

    # Engine temperature impact
    if sensor_data["engine_temp"] > 95:
        score -= 25
    elif sensor_data["engine_temp"] > 85:
        score -= 10

    # Battery voltage impact
    if sensor_data["battery_voltage"] < 11.5:
        score -= 25
    elif sensor_data["battery_voltage"] < 12.2:
        score -= 10

    # Vibration impact
    if sensor_data["vibration"] > 0.8:
        score -= 20
    elif sensor_data["vibration"] > 0.6:
        score -= 10

    # Ensure score stays within bounds
    score = max(0, min(score, 100))

    return score
if __name__ == "__main__":
    sample_data = {
        "engine_temp": 98,
        "battery_voltage": 11.2,
        "vibration": 0.85
    }

    score = calculate_health(sample_data)
    print("Health Score:", score)
