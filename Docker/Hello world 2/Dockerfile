# Dockerfile (recommended)
FROM python:3.8-slim

WORKDIR /app
COPY . /app

# install system build deps needed by some wheels or packages (kept minimal)
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gfortran libatlas-base-dev && \
    rm -rf /var/lib/apt/lists/*

# upgrade pip/wheel to reduce build-from-source attempts
RUN pip install --upgrade pip wheel setuptools

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
