from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import tensorflow as tf
import os
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

class_names = ['Anjing', 'Kelinci', 'Kucing']
model = None

def load_model():
    global model
    if model is None:
        app.logger.info("Loading model...")
        from tensorflow.keras.models import load_model
        with tf.device('/cpu:0'):  # Force CPU usage
            model = load_model("model_klasifikasi_hewan.h5")
        app.logger.info("Model loaded")
    return model

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def preprocess_image(file_stream):
    img = Image.open(file_stream).convert('RGB').resize((128, 128))
    input_data = np.array(img, dtype=np.float16) / 255.0  # Use float16
    return np.expand_dims(input_data, axis=0)

@app.route("/")
def home():
    return "Image Classification API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    if 'image_file' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
        
    file = request.files['image_file']
    selected_class = request.form.get('animal_class', '')
    
    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400
        
    try:
        model = load_model()
        input_data = preprocess_image(file.stream)
        
        # Gunakan batch prediction untuk efisiensi
        prediction = model.predict(input_data, batch_size=1)
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
        app.logger.error(f"Prediction error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
