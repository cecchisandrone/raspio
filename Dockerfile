FROM hypriot/rpi-python

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]

EXPOSE 6000
