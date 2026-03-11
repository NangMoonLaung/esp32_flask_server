from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Render HTTPS endpoint
RENDER_URL = "https://yourapp.onrender.com/sensor-data"

@app.route("/sensor-data", methods=['GET', 'POST'])
def sensor_data():
    data = request.args  # SIM800 GET parameters

    # Optional: print to console
    print(f"Received data: {data}")

    # Forward data to Render HTTPS server
    response = requests.get(RENDER_URL, params=data)

    return jsonify({"status": "forwarded", "response_code": response.status_code})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
