from datetime import datetime, timedelta

def schedule_service(vehicle_id, issue):
    service_date = datetime.now() + timedelta(days=1)

    booking = {
        "vehicle_id": vehicle_id,
        "issue": issue,
        "service_center": "Nearest Authorized Service Center",
        "scheduled_date": service_date.strftime("%Y-%m-%d %H:%M"),
        "status": "Scheduled"
    }

    print("SERVICE SCHEDULED ✅:", booking)
    return booking
