FROM registry.datadrivendiscovery.org/jpl/docker_images:python3.6_base

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip3.6 install -r requirements.txt

CMD ./run.sh