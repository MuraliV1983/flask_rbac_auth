from flask import Flask
from routes.auth import auth_bp
from routes.event import event_bp

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Register routes
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(event_bp, url_prefix="/events")

if __name__ == "__main__":
    app.run(debug=True)