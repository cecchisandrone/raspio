FROM hypriot/rpi-python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]

EXPOSE 6000
