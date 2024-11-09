FROM python:latest

# Copy requirements.txt and install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy the entire project into the root directory
COPY . /

# Expose the port that Flask will run on
EXPOSE 5000

# Run the Flask application
CMD ["python", "Receipt_processor.py"]