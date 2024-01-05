FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3.11 python3.11-dev python3-pip gcc musl-dev libxml2 libxml2-dev git libxslt1-dev libpq-dev gnupg2 wget unzip && mkdir -p /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/

WORKDIR /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

CMD uwsgi --module=whatproducts.wsgi --http=0.0.0.0:80