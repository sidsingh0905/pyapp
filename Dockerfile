# Use an official Python runtime as a parent image
FROM python:3.11.5-alpine

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for pyodbc and others
RUN apk update && apk add --no-cache \
    build-base \
    unixodbc-dev \
    && rm -rf /var/cache/apk/*

# Copy the requirements.txt file into the container
COPY requirement.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of your application code into the container
COPY . /app/

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define environment variable to specify the Flask application entry point
ENV FLASK_APP=app.py

# Run the Flask application when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
