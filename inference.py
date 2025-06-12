import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load model
model = tf.keras.models.load_model('model_klasifikasi_hewan.h5')

# Ganti dengan nama file gambar Anda sendiri
img_path = 'your_image.jpg'  # Contoh: 'kelinci1.jpg'

# Load dan proses gambar
img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# Prediksi
predictions = model.predict(img_array)
class_names = ['Anjing', 'Kelinci', 'Kucing']
predicted_class = class_names[np.argmax(predictions)]
confidence = round(100 * np.max(predictions), 2)

print(f"Predicted: {predicted_class} with confidence {confidence}%")
