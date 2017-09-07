#!/bin/bash

NORMAL="\\033[0;39m"                                                            
RED="\\033[1;31m"                                                               
BLUE="\\033[1;34m"

logs=$(pwd)

log() {                                                                         
    echo -e "$BLUE > $1 $NORMAL"                                                   
}                                                                               
                                                                                    
error() {                                                                       
    echo ""                                                                     
    echo -e "$RED >>> ERROR - $1$NORMAL"                                           
}                 
clear                                                                           



if [ -e build.out ]; then 
    rm build.out
fi


# Stop all services
./stop.sh

# Start Kafka server
log "Kafka setup..."
cd kafka/
./setup_kafka.sh | tee ${logs}/build.out
cd ../

# Start DB
log "primitives setup..."
cd primitives/
docker-compose down --remove-orphans --volumes  | tee -a ${logs}/build.out                             
docker-compose up --build -d | tee -a ${logs}/build.out
cd ../

# Start queue
log "sample_client setup..."
cd sample_client/
docker-compose down --remove-orphans --volumes  | tee -a ${logs}/build.out      
docker-compose up --build -d | tee -a ${logs}/build.out 
cd ../

docker ps
