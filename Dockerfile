# # Stage 1: Install Microsoft ODBC driver on a full Debian image (with root access)
# FROM mcr.microsoft.com/mssql/server:2019-latest as odbc

# USER root

# # Install required packages for ODBC on Debian-based image
# RUN apt-get update && apt-get install -y \
#     curl \
#     gnupg \
#     unixodbc-dev \
#     && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
#     && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/microsoft-prod.list \
#     && apt-get update \
#     && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
#     && rm -rf /var/lib/apt/lists/*

# # Stage 2: Python app with Alpine base image (without root access)
# FROM python:3.11.5-alpine

# # Set the working directory in the container
# WORKDIR /app

# # Install system dependencies required for pyodbc and others
# RUN apk update && apk add --no-cache \
#     build-base \
#     unixodbc-dev \
#     curl \
#     libressl-dev \
#     && rm -rf /var/cache/apk/*

# # Copy the Microsoft ODBC driver libraries from the first stage (Debian image)
# COPY --from=odbc /usr/lib /usr/lib
# COPY --from=odbc /etc/ssl/certs /etc/ssl/certs
# COPY --from=odbc /opt/microsoft/msodbcsql17 /opt/microsoft/msodbcsql17


# # Set the environment variable LD_LIBRARY_PATH to include the ODBC library directory
# ENV LD_LIBRARY_PATH=/opt/microsoft/msodbcsql17/lib64/:$LD_LIBRARY_PATH

# # Copy the requirements.txt file into the container
# COPY requirement.txt /app/

# # Install any needed Python packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirement.txt

# # Copy the rest of your application code into the container
# COPY . /app/

# # Expose port 5000 for the Flask application
# EXPOSE 5000

# # Define environment variable to specify the Flask application entry point
# ENV FLASK_APP=app.py

# # Run the Flask application when the container starts
# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]




# Use a Python base image

FROM python:3.11.5-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies and ODBC driver (to connect to SQL Server)
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/microsoft-prod.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file into the container
COPY requirement.txt /app/

# Install Python dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the Flask app files into the container
COPY . /app/

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define environment variable to specify the Flask application entry point
ENV FLASK_APP=app.py

# Run the Flask application when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]


