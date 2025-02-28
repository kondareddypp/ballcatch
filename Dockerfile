# Use the official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Flask
RUN pip install flask

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the application
CMD ["python", "app.py"]
