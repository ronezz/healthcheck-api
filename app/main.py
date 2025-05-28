from flask import Flask, jsonify
from utils import get_system_status

app = Flask(__name__)

@app.route("/health", methods=["GET"])


def health_check():
    status= get_system_status()
    return jsonify(status), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  