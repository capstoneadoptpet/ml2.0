# Gunakan image Python yang sesuai sebagai base image
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Upgrade pip terlebih dahulu
RUN pip install --upgrade pip

# Hapus cache pip
RUN pip cache purge

# Copy requirements.txt ke dalam container
COPY requirements.txt /app/

# Install dependensi yang ada di requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh kode aplikasi ke dalam container
COPY . /app/

# Tentukan port yang digunakan oleh aplikasi
EXPOSE 5000

# Jalankan aplikasi Flask menggunakan Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
