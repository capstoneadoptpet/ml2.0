from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
class_names = ['Anjing', 'Kelinci', 'Kucing']
model = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.before_first_request
def load_model_once():
    global model
    model = load_model("model_klasifikasi_hewan.h5")

def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB').resize((128, 128))
    input_data = np.array(image, dtype=np.float32) / 255.0
    input_data = np.expand_dims(input_data, axis=0)
    return input_data

@app.route("/predict", methods=["POST"])
def predict():
    if 'image_file' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image_file']
    selected_class = request.form.get('animal_class', '')

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        input_data = preprocess_image(filepath)
        prediction = model.predict(input_data)
        predicted_index = np.argmax(prediction)
        predicted_label = class_names[predicted_index]
        confidence = float(np.max(prediction)) * 100

        is_match = (predicted_label.lower() == selected_class.lower()) if selected_class else None

        result = {
            "predicted_label": predicted_label,
            "confidence": round(confidence, 2),
            "selected_class": selected_class if selected_class else None,
            "is_match": is_match
        }
        return jsonify(result)

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
        except Exception as cleanup_error:
            print(f"Cleanup error: {cleanup_error}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
