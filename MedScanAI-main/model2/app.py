# import requests
# from flask import Flask, render_template, request, jsonify
# from geopy.distance import geodesic

# app = Flask(__name__)

# @app.route('/nearby', methods=['GET'])
# def get_nearby_places():
#     lat = request.args.get('lat')
#     lng = request.args.get('lng')
#     place_type = request.args.get('type')

#     if not lat or not lng:
#         return jsonify({"error": "Latitude and longitude are required"}), 400

#     user_location = (float(lat), float(lng))
    
#     # ✅ Fix category issue (Medical Stores are actually "Pharmacy")
#     category = "pharmacy" if place_type == "medical_store" else "doctor"

#     # ✅ Use Overpass API for better results
#     url = f"https://overpass-api.de/api/interpreter?data=[out:json];node[amenity={category}](around:5000,{lat},{lng});out;"
    
#     headers = {"User-Agent": "MedScanAI/1.0 (ayush@example.com)"}
#     response = requests.get(url, headers=headers)

#     # ✅ Check if API is working
#     if response.status_code != 200:
#         return jsonify({"error": "API request failed", "status": response.status_code, "text": response.text}), 500
    
#     try:
#         data = response.json()
#     except requests.exceptions.JSONDecodeError:
#         return jsonify({"error": "Invalid JSON response from API"}), 500

#     nearby_places = []
#     for element in data.get("elements", []):
#         place_lat = element.get("lat")
#         place_lng = element.get("lon")
#         place_name = element.get("tags", {}).get("name", "Unknown Place")

#         if place_lat and place_lng:
#             distance = geodesic(user_location, (place_lat, place_lng)).km
#             if distance <= 5:
#                 nearby_places.append({
#                     "name": place_name,
#                     "latitude": place_lat,
#                     "longitude": place_lng,
#                     "distance": round(distance, 5)
#                 })

#     if nearby_places:
#         return jsonify(nearby_places)
#     else:
#         return jsonify({"error": "No places found within 5 km."}), 404

# @app.route('/')
# def index():
#     return render_template('index1.html')

# if __name__ == '__main__':
#     app.run(debug=True)
import requests
from flask import Blueprint, Flask, render_template, request, jsonify
from geopy.distance import geodesic
module2_bp = Blueprint('model2_8', __name__) 

app = Flask(__name__)

# Replace with your new Geoapify API key
GEOAPIFY_API_KEY = '19b13fb3d72044bab53370cb9fa462c7'

@app.route('/nearby', methods=['GET'])
def get_nearby_places():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    place_type = request.args.get('type')

    if not lat or not lng:
        return jsonify({"error": "Latitude and longitude are required"}), 400

    user_location = (float(lat), float(lng))

    # Fix categories for Geoapify API
    category = "healthcare.pharmacy" if place_type == "medical_store" else "healthcare.clinic"

    # Geoapify API URL
    url = f"https://api.geoapify.com/v2/places?categories=healthcare.pharmacy&filter=circle:80.3058,26.4792,5000&limit=20&apiKey=19b13fb3d72044bab53370cb9fa462c7"

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "API request failed", "status": response.status_code, "text": response.text}), 500

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        return jsonify({"error": "Invalid JSON response from API"}), 500

    nearby_places = []
    for feature in data.get("features", []):
        properties = feature.get("properties", {})
        place_lat = properties.get("lat")
        place_lng = properties.get("lon")
        place_name = properties.get("name", "Unknown Place")

        if place_lat and place_lng:
            distance = geodesic(user_location, (place_lat, place_lng)).km
            if distance <= 5:
                nearby_places.append({
                    "name": place_name,
                    "latitude": place_lat,
                    "longitude": place_lng,
                    "distance": round(distance, 5)
                })

    if nearby_places:
        return jsonify(nearby_places)
    else:
        return jsonify({"error": "No places found within 5 km."}), 404

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5002, debug=True)
