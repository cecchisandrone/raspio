FROM resin/rpi-raspbian:stretch

# Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python \
    python-dev \
    python-pip \
    python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN python --version

RUN pip --version

RUN pip install setuptools

RUN pip install -r requirements.txt

CMD [ "python", "/app/main.py" ]

EXPOSE 6000
