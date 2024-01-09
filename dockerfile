FROM  python:3.10.5-buster


# copy requirements
COPY  ./requirements.txt /srv/requirements.txt
RUN mkdir /srv/Product
COPY . /srv/Product

RUN pip install --no-cache-dir -U pip setuptools
RUN pip install --no-cache-dir -r /srv/requirements.txt

RUN apt-get update
RUN apt-get -y install cron

# System Packages

