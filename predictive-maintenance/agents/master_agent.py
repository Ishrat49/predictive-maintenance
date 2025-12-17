from agents.alert_agent import send_alert
from agents.scheduler_agent import schedule_service

def evaluate_and_act(vehicle_id, prediction):
    risk = prediction["risk_level"]
    issue = prediction["predicted_issue"]

    print(f"MASTER AGENT 🧠 | Evaluating risk: {risk}")

    if risk == "High":
        alert_msg = send_alert(vehicle_id, issue, risk)
        booking = schedule_service(vehicle_id, issue)
        return {
            "action": "Service Scheduled",
            "alert": alert_msg,
            "booking": booking
        }

    elif risk == "Medium":
        alert_msg = send_alert(vehicle_id, issue, risk)
        return {
            "action": "Alert Sent",
            "alert": alert_msg
        }

    else:
        print("MASTER AGENT 🟢 | No action required")
        return {
            "action": "No Action"
        }
