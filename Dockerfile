FROM python:3.7-slim-buster
add steam.py /app/steam.py
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD [ "python3", "/app/steam.py"]