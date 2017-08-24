#!/bin/bash

export PS4='$(tput setaf 1)$(tput setab 7) + $(tput sgr 0)'
set -x


docker-compose down --remove-orphans --volumes
docker-compose up --build -d

set +x
echo -e "$(tput setaf 1)\tCreate multiple Kafka Topics for Communication between containers...$(tput sgr 0)"
docker-compose exec kafka /bin/bash -c "\
    bin/kafka-topics.sh --list --zookeeper zookeeper:2181 && \
    bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic consumer && \
    bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic producer && \
    bin/kafka-topics.sh --list --zookeeper zookeeper:2181 && \
    exit"
sleep 5
echo -e "$(tput setaf 1)\tMaking sure services were spun up properly...$(tput sgr 0)"
set -x
docker-compose ps && docker ps
