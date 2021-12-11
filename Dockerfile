FROM python:3.10-alpine
RUN apk add --no-cache build-base
WORKDIR /app
COPY *.py *.pyc config.ini requirements.txt ./
RUN CFLAGS=-fcommon pip install --no-cache-dir -r requirements.txt
EXPOSE 6000
CMD [ "python", "/app/main.py" ]
