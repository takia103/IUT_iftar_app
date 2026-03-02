stock_service/app.py:

from flask import Flask, jsonify
import time

app = Flask(__name__)

plates = 120

@app.route("/plates")
def get_plates():
    return jsonify({"plates": plates})

@app.route("/health")
def health():
    return jsonify({
        "service": "stock",
        "status": "online",
        "time": time.time(),
        "plates_left": plates
    })

app.run(port=5004, debug=True)
