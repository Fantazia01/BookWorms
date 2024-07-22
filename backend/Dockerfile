# backend/Dockerfile
FROM python:3.9-slim

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory
WORKDIR /app

# Clone the latest code from GitHub
RUN git clone https://github.com/Fantazia01/BookWorms.git .

# Set the working directory to the backend folder inside the cloned repo
WORKDIR /app/backend

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create the database
RUN python create_db.py

# Run the backend server
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
