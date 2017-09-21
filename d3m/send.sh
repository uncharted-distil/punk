cd kafka_wrapper
python test_send_message.py test.csv
cd ../
tail -f log.txt
