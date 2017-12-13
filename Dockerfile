FROM arm32v6/python:3.7.0a3-alpine3.6

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]

EXPOSE 6000