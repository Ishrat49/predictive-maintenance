def predict_failure(sensor_data, health_score):
    """
    Predict failure risk and probable issue.
    Returns risk level and issue description.
    """

    risk_level = "Low"
    issue = "No immediate issues"

    if sensor_data["engine_temp"] > 95:
        risk_level = "High"
        issue = "Engine Overheating"

    elif sensor_data["battery_voltage"] < 11.5:
        risk_level = "High"
        issue = "Battery Failure Risk"

    elif sensor_data["vibration"] > 0.8:
        risk_level = "High"
        issue = "Mechanical Vibration Issue"

    elif health_score < 70:
        risk_level = "Medium"
        issue = "General Wear and Tear"

    return {
        "health_score": health_score,
        "risk_level": risk_level,
        "predicted_issue": issue
    }
if __name__ == "__main__":
    sample_data = {
        "engine_temp": 99,
        "battery_voltage": 11.3,
        "vibration": 0.82
    }

    from health_score import calculate_health
    health = calculate_health(sample_data)

    result = predict_failure(sample_data, health)
    print(result)
