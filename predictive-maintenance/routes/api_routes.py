from flask import Blueprint, jsonify
import pandas as pd

from ai_engine.health_score import calculate_health
from ai_engine.failure_prediction import predict_failure
from agents.master_agent import evaluate_and_act

api_bp = Blueprint("api", __name__)

DATA_PATH = "data/sensor_data.csv"
@api_bp.route("/api/latest-status", methods=["GET"])
def latest_status():
    try:
        df = pd.read_csv(DATA_PATH)

        if df.empty:
            return jsonify({"error": "No sensor data found"})

        latest = df.iloc[-1]

        # Map by index to avoid header issues
        sensor_data = {
            "vehicle_id": str(latest.iloc[0]),
            "engine_temp": float(latest.iloc[2]),
            "battery_voltage": float(latest.iloc[3]),
            "vibration": float(latest.iloc[4]),
            "mileage": int(latest.iloc[5])
        }

        health = calculate_health(sensor_data)
        prediction = predict_failure(sensor_data, health)
        agent_result = evaluate_and_act(sensor_data["vehicle_id"], prediction)

        return jsonify({
            "sensor_data": sensor_data,
            "prediction": prediction,
            "agent_action": agent_result
        })

    except Exception as e:
        return jsonify({"error": str(e)})
