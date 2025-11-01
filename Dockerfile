# Use lightweight official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first (for Docker layer caching)
COPY requirements.txt /app/

# Install system dependencies (optional: needed for some Python libs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN  pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . /app

# Expose Flask default port
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run your Flask app
CMD ["python", "app.py"]
