FROM python:3.9-alpine

RUN apk add --update build-base linux-headers bash gcc musl-dev

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80/tcp
ENTRYPOINT ["/usr/local/bin/uwsgi", "--http", ":80", "--module", "app:app"]
