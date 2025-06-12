import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model(r'C:\AdoptHouse_ImageModel\model_klasifikasi_hewan.h5')
img_path = r'C:\AdoptHouse_ImageModel\dog1.jpg'

img = image.load_img(img_path, target_size=(128, 128))  # Sesuaikan dengan input model
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

predictions = model.predict(img_array)
class_names = ['Anjing', 'Kelinci', 'Kucing']  # Ganti sesuai urutan kelasmu
predicted_class = class_names[np.argmax(predictions)]
confidence = round(100 * np.max(predictions), 2)

print(f"Predicted: {predicted_class} with confidence {confidence}%")
