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
export PS4='$(tput setaf 1)$(tput setab 7) + $(tput sgr 0)'                     
clear                                                                           

log "Taking everything down first..."
set -x                                                                          

for dir in */;
do
    cd ${dir}
    docker-compose down
    cd ../
done
