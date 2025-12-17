def send_alert(vehicle_id, issue, risk_level):
    message = (
        f"ALERT 🚨 | Vehicle: {vehicle_id} | "
        f"Issue: {issue} | Risk Level: {risk_level}"
    )
    print(message)
    return message
