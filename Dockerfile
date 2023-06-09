FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the script and dependencies files
COPY updater_price.py requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Run the script
CMD ["python", "updater_price.py"]
