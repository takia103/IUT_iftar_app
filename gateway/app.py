gateway/app.py:

from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Service URLs
IDENTITY = "http://127.0.0.1:5001"
ORDER    = "http://127.0.0.1:5002"
STOCK    = "http://127.0.0.1:5004"
KITCHEN  = "http://127.0.0.1:5003"


# -----------------------
# PAGE ROUTES (UI LOAD)
# -----------------------

@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/menu")
def menu_page():
    return render_template("menu.html")


@app.route("/status/<int:oid>")
def status_page(oid):
    return render_template("status.html", oid=oid)


@app.route("/ready/<int:oid>")
def ready_page(oid):
    return render_template("ready.html", oid=oid)


@app.route("/admin")
def admin_page():
    return render_template("admin.html")


# -----------------------
# API ROUTES (BACKEND CALLS)
# -----------------------

@app.route("/api/login", methods=["POST"])
def api_login():
    try:
        r = requests.post(f"{IDENTITY}/login", json=request.json)
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": "Identity Service Down", "details": str(e)}), 500


@app.route("/api/order", methods=["POST"])
def api_order():
    data = request.json

    try:
        # Deduct budget first
        requests.post(f"{IDENTITY}/deduct", json=data)

        # Create order
        r = requests.post(f"{ORDER}/order", json={})
        return jsonify(r.json())

    except Exception as e:
        return jsonify({"error": "Order Flow Failed", "details": str(e)}), 500


@app.route("/api/status/<int:oid>")
def api_status(oid):
    try:
        r = requests.get(f"{ORDER}/status/{oid}")
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": "Order Service Down", "details": str(e)}), 500


@app.route("/api/plates")
def api_plates():
    try:
        r = requests.get(f"{STOCK}/plates")
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": "Stock Service Down", "details": str(e)}), 500


# -----------------------
# HEALTH DASHBOARD (ADMIN)
# -----------------------

@app.route("/api/health")
def health():
    services = {
        "identity": f"{IDENTITY}/health",
        "order": f"{ORDER}/health",
        "stock": f"{STOCK}/health",
        "kitchen": f"{KITCHEN}/health"
    }

    result = {}

    for name, url in services.items():
        try:
            r = requests.get(url, timeout=2)
            result[name] = r.json()
        except Exception as e:
            result[name] = {
                "service": name,
                "status": "DOWN",
                "error": str(e)
            }

    return jsonify(result)


# -----------------------
# START GATEWAY
# -----------------------

if __name__ == "__main__":
    print("Gateway running on http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
