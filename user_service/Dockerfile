FROM python:3.10-bullseye
RUN python -m pip install --upgrade pip
WORKDIR /app

# Copy the top-level files in your service's directory
# Modify these instructions to do that
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY queries queries
COPY routers routers
COPY model.py model.py

# Copy all of the subdirectories in your service's directory
# Modify these instructions to do that
# COPY routers routers

RUN python -m pip install -r requirements.txt
CMD uvicorn main:app --host 0.0.0.0 --port $PORT