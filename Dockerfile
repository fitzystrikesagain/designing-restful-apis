FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./create_endpoints/serializing/ .

CMD [ "python", "./app.py" ]