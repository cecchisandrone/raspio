FROM python:3.5-alpine
RUN apk add --no-cache build-base
WORKDIR /app
COPY *.py *.pyc config.ini requirements.txt ./
RUN ls -al
RUN python --version
RUN pip --version
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 6000
CMD [ "python", "/app/main.py" ]
