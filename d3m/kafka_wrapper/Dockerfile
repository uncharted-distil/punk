FROM alejandrox1/ubuntu_miniconda

# Install any Python dependencies for your app
RUN apt-get update -y                                                           
COPY requirements.txt /app/requirements.txt                                     
WORKDIR /app 
RUN pip install -r requirements.txt

# Copy wrapper 
COPY kafka_wrapper.py .

CMD ["python", "kafka_wrapper.py"]
