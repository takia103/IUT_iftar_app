kitchen_service/app.py:

from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "service": "kitchen",
        "status": "online",
        "time": time.time()
    })

app.run(port=5003, debug=True)
