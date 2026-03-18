from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

AZURE_MAPS_KEY = "73cx8nVOkRIoUoy0SSjmWeDRNzDB0PdsiVbdsAfOxVEJihrsvNOWJQQJ99CCACYeBjFVCOd4AAAgAZMPNQyd"

@app.route('/get-route', methods=['GET'])
def get_route():
    try:
        origin = request.args.get('origin')
        dest = request.args.get('dest')

        print(f"DEBUG: Route from {origin} ➔ {dest}")

        endpoint = "https://atlas.microsoft.com/route/directions/json"
        params = {
            "api-version": "1.0",
            "subscription-key": AZURE_MAPS_KEY,
            "query": f"{origin}:{dest}",
            "traffic": "true"
        }

        response = requests.get(endpoint, params=params)

        if response.status_code != 200:
            print("AZURE ERROR:", response.text)
            return jsonify({"error": "Azure API failed"}), 500

        data = response.json()
        summary = data['routes'][0]['summary']

        # 🔹 Basic values
        distance_km = summary['lengthInMeters'] / 1000
        time_min = summary['travelTimeInSeconds'] / 60
        azure_delay = summary['trafficDelayInSeconds'] / 60

        # 🔥 SMART AI TRAFFIC DELAY (METHOD 2)
        current_hour = datetime.now().hour

        # Peak hours (Bangalore logic)
        if 8 <= current_hour <= 11 or 17 <= current_hour <= 21:
            peak_factor = random.uniform(1.3, 2.0)
        else:
            peak_factor = random.uniform(0.5, 1.2)

        # Simulated delay based on distance + peak factor
        simulated_delay = distance_km * peak_factor

        # Final delay (take higher of Azure or AI simulation)
        delay_minutes = max(azure_delay, simulated_delay)

        # Add slight randomness for realism
        delay_minutes += random.uniform(1, 3)

        return jsonify({
            "distance": round(distance_km, 2),
            "time": round(time_min),
            "delay": round(delay_minutes),
            "source": "Current Location",
            "dest": "Target Destination"
        })

    except Exception as e:
        print("SERVER ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=8080)
