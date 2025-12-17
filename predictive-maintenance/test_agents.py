from ai_engine.health_score import calculate_health
from ai_engine.failure_prediction import predict_failure
from agents.master_agent import evaluate_and_act

sensor_data = {
    "engine_temp": 99,
    "battery_voltage": 11.2,
    "vibration": 0.85
}

vehicle_id = "AP09AB1234"

health = calculate_health(sensor_data)
prediction = predict_failure(sensor_data, health)

result = evaluate_and_act(vehicle_id, prediction)
print("FINAL RESULT:", result)
