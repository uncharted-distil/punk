FROM python:3.6-slim

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN tar -xzf metadata.tar.gz \
    && pip install ./metadata-master-92ca72247c4e676ebf74b6bdd8b0f9492588db8c/

RUN tar -xzf primitive_interfaces.tar.gz \
    && pip install ./primitive-interfaces-8ad39963b5076cb8565b941cf339f86d8cfd9f0d-8ad39963b5076cb8565b941cf339f86d8cfd9f0d/

RUN pip install -r requirements.txt

CMD ./run.sh