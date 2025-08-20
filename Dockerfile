# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Nginx and other dependencies
RUN apt-get update && apt-get install -y nginx cron && apt-get clean

# Set work directory
WORKDIR /app

# create directory for socket
RUN mkdir -p /app/run

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

# Copy Nginx and Gunicorn configurations
COPY nginx.conf /etc/nginx/nginx.conf
COPY gunicorn.conf.py /app/gunicorn.conf.py

# Expose port 80
EXPOSE 80

# Run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]