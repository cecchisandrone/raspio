FROM arm32v6/python:2.7.14-alpine3.6

RUN apk update && apk add build-base

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "/app/main.py" ]

EXPOSE 6000
