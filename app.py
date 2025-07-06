# app/app.py
from flask import Flask
from controllers.mutuals_controller import bp as mutuals_bp

app = Flask(__name__)
app.register_blueprint(mutuals_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
