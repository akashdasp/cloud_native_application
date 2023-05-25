# Use the base Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app files to the working directory
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Flask app will listen
EXPOSE 5000

# Set the entry point command to run the Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]
