from flask import Flask
from routes.api_routes import api_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(api_bp)
app.register_blueprint(dashboard_bp)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=False)
