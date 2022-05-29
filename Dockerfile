FROM python:3.7-slim-buster
add ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
add steam.py /app/steam.py
CMD [ "python3", "/app/steam.py"]