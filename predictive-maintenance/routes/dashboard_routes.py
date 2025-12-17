from flask import Blueprint, render_template

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():
    return render_template("dashboard.html")

@dashboard_bp.route("/customer")
def customer():
    return render_template("customer.html")

@dashboard_bp.route("/manufacturer")
def manufacturer():
    return render_template("manufacturer.html")
