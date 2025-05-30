FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Install system dependencies required for TensorFlow
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements.txt to the container
COPY requirements.txt /app/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Disable GPU and enforce CPU usage
RUN echo "import tensorflow as tf; tf.config.set_visible_devices([], 'GPU')" > /app/set_tensorflow_cpu.py

# Disable oneDNN custom operations
ENV TF_ENABLE_ONEDNN_OPTS=0

# Copy the rest of the application code to the container
COPY . /app/

# Expose port 5000
EXPOSE 5000

# Run the Flask app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
