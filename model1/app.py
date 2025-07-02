import os
import cv2
import pandas as pd
import easyocr
import pickle
from fuzzywuzzy import process
from flask import Blueprint, Flask, request, jsonify, render_template
from PIL import Image
import pyheif

module1_bp = Blueprint('model1_8', __name__)  # use a unique name like 'module1'

app = Flask(__name__)

# Load your model (if needed)
model_path = "model.pkl"
if os.path.exists(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
else:
    model = None  # If your processing doesn't need a model, you can skip this

# Convert HEIC to JPEG
def convert_heic_to_supported_format(image_path):
    heif_file = pyheif.read(image_path)
    image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, heif_file.stride)
    output_path = image_path.replace(".heic", ".jpg")
    image.save(output_path, format="JPEG")
    return output_path

# Preprocess Image
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresholded

# Recognize Text
def recognize_text(image_path):
    reader = easyocr.Reader(["en"], gpu=False)
    results = reader.readtext(image_path)
    return " ".join([result[1] for result in results])

# Lookup Molecule
def lookup_molecule(extracted_text, dataset_path):
    df = pd.read_csv(dataset_path)
    df.columns = df.columns.str.strip()
    if "Molecule Name" not in df.columns:
        return {"error": "Dataset is missing 'Molecule Name' column"}
    
    best_match = process.extractOne(extracted_text, df["Molecule Name"])
    if best_match:
        matched_row = df[df["Molecule Name"] == best_match[0]].to_dict("records")[0]
        return {"match": best_match[0], "score": best_match[1], "details": matched_row}
    return {"error": "Molecule not found"}

# Process Image
def process_medicine_image(image_path, dataset_path):
    if image_path.lower().endswith(".heic"):
        image_path = convert_heic_to_supported_format(image_path)
    
    extracted_text = recognize_text(image_path)
    return lookup_molecule(extracted_text, dataset_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"})

    # Save uploaded file
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    dataset_path = "Molecule_Dataset2.csv"
    result = process_medicine_image(file_path, dataset_path)

    return jsonify(result)

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(port=5000, debug=True)

