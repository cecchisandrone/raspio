FROM hypriot/rpi-python

COPY . /data

RUN pip install -r requirements.txt

CMD [ "python", "./data/main.py" ]

EXPOSE 6000
