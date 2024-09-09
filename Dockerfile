# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Execute post-install script to download the SpaCy model
# RUN python post_install.py

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable to prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Run app.py when the container launches
CMD ["python", "main.py"]