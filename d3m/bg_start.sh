#!/bin/bash
sudo docker run -d --name=feature_selection -t feature_selection
sudo docker logs --follow --timestamps feature_selection &>> log.txt &
