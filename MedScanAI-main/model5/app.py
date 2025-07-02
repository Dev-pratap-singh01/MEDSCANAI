import pickle
import numpy as np
from app import Flask, request, jsonify, render_template


app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["answers"]
        mapping = {
            "Not At All": 0,
            "Several Days": 1,
            "More Than Half The Days": 2,
            "Very Difficult": 3,
            "Somewhat Difficult": 2,
            "Not Difficult At All": 1
        }
        numerical_input = [mapping.get(answer, 0) for answer in data]
        input_array = np.array(numerical_input).reshape(1, -1)
        prediction = model.predict(input_array)[0]

        return jsonify({"prediction": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(port=5004, debug=True)
