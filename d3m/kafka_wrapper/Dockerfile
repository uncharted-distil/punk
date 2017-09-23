FROM alejandrox1/ubuntu_miniconda

# Install any Python dependencies for your app
RUN apt-get update -y                                                           
COPY requirements.txt /app/requirements.txt                                     
WORKDIR /app 
RUN pip install -r requirements.txt

# Copy wrapper 
COPY kafka_wrapper.py .
COPY test.csv .

ENV KAFKASERVER=192.168.7.3:9092
ENV CONSUMERTOPIC=feature_selection_input
ENV PRODUCERTOPIC=feature_selection_results

CMD ["python", "kafka_wrapper.py"]
