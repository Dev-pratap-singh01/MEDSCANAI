from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model_path = "model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError("model.pkl file not found. Ensure it exists in the same directory as this script.")

with open(model_path, "rb") as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')  # Make sure your HTML file is inside the 'templates' folder

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Convert input data to a list of feature values
        features = [
            int(data.get("fever", "no") == "yes"),
            int(data.get("cough", "no") == "yes"),
            int(data.get("fatigue", "no") == "yes"),
            int(data.get("difficulty-breathing", "no") == "yes"),
            int(data.get("blood-pressure", "no") == "yes"),
            int(data.get("cold", "no") == "yes"),
            int(data.get("dizziness", "no") == "yes"),
            int(data.get("body-pain", "no") == "yes"),
            int(data.get("headache", "no") == "yes"),
            int(data.get("days", 0))
        ]
        
        # Convert to NumPy array and reshape for prediction
        input_array = np.array([features])
        prediction = model.predict(input_array)[0]
        
        return jsonify({"prediction": str(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5003, debug=True)