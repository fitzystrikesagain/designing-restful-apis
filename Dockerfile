FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./create_endpoints/serializing/ .
COPY ./utils/ ./utils

CMD [ "python", "./app.py" ]