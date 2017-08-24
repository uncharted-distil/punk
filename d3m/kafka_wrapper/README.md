# Deploying primitives as Docker containers

1. Modify `process_msg` inside of `kafka_wrapper.py` to process each incoming
request.

2. Modify `environment.env` to have the correct environmental variables.

3. Build and run container as,
```
sudo docker build -t <name> . && sudo docker run -d --env-file environment.env --name=<name> <name>
```

4. Double check it went well
```
sudo docker ps
```
