
# 🐾 Pet Adoption - Klasifikasi Gambar Hewan

Aplikasi ini merupakan bagian dari sistem **Adopsi Hewan Online (Pet Adoption Web App)**. Modul klasifikasi ini bertugas mengenali jenis hewan dari gambar yang diunggah pengguna, menggunakan model deep learning berbasis **MobileNetV2**.

---

## 🌐 Use Case

Ketika pengguna mengunggah gambar hewan, sistem secara otomatis mengklasifikasikan hewan tersebut (misalnya: kucing, anjing, kelinci) untuk membantu proses kategorisasi dalam sistem adopsi.

---

## 🧠 Model

Model klasifikasi dibangun menggunakan:

- ✅ Arsitektur: **MobileNetV2**
- ✅ Pre-trained weights dari ImageNet
- ✅ Head kustom: GlobalAveragePooling → Dropout → Dense Softmax
- ✅ Fine-tuning sebagian layer MobileNetV2

Model akhir disimpan sebagai file: `model_klasifikasi_hewan.h5`

---

## 📦 Struktur Proyek

```
.
├── app.py                      # Endpoint deployment (misalnya Flask / FastAPI)
├── model_klasifikasi_hewan.h5 # Model klasifikasi hewan
├── render.yaml                # Konfigurasi deployment di Render.com
├── requirements.txt           # Dependency Python
```

---

## 🚀 Deployment

Proyek ini dideploy ke platform **Render** menggunakan `render.yaml`. Anda dapat menjalankan aplikasi ini secara lokal atau langsung deploy:

### ▶️ Jalankan Lokal

```bash
pip install -r requirements.txt
python app.py
```

### 🌍 Deployment di Render

Pastikan file `render.yaml` sudah dikonfigurasi dengan:

- Type: Web Service
- Start command: `python app.py`

---

## 🧾 Dokumentasi Model

Model dilatih dengan dataset gambar hewan yang sudah di-augmentasi dan dibagi menjadi data pelatihan dan validasi. Pelatihan terdiri dari dua tahap:

1. **Initial Training** – hanya head dilatih (base dibekukan)
2. **Fine-tuning** – unfreeze sebagian layer MobileNetV2

Model akhir memiliki akurasi validasi yang memadai untuk klasifikasi dasar dalam aplikasi web adopsi hewan.

---

## 📊 Visualisasi Hasil Pelatihan

![Training Accuracy & Loss](https://drive.google.com/uc?export=view&id=1MzzfqUx2tj5QHgbqajMosxMkj9ZySScy)

- **Akurasi Pelatihan (accuracy)** pada Epoch 19 adalah 82.46%.
- **Akurasi Validasi (val_accuracy)** pada Epoch 19 adalah 82.77%.
---

## 🔁 Replikasi Proyek

Untuk menggunakan proyek ini:

1. Pastikan file `model_klasifikasi_hewan.h5` tersedia.
2. Jalankan `app.py` untuk inference berbasis gambar.
3. Upload gambar melalui form web atau API endpoint (tergantung implementasi `app.py`).

---

## 👤 Kontributor

1. [Rizqi Maulidi (MC224D5Y1546)](https://github.com/rizqi-maulidi) - Machine Learning as a Team Lead
2. [Bagas Rizky Ramadhan (MC001D5Y1201)](https://github.com/Bagas30-mm) - Machine Learning
3. [Deffin Purnama Noer (MC224D5Y0523)](https://github.com/deffinpurnama) - Machine Learning
4. [Agung Maulana Saputra (FC193D5Y1198)](https://github.com/agung7703) - Front End Back End as a UI/UX Designer & Front-End Developer
5. [Jason Chainara Putra (FC325D5Y0822)](https://github.com/JasonFTI45) - Front End Back End as a Full-Stack Developer
6. [Samuel Maruba Manik (FC406D5Y1918)](https://github.com/Redfly54) - Front End Back End as a Back-End Developer
