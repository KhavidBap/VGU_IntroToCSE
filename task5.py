import time
import sys
from Adafruit_IO import MQTTClient
import csv

class Task5:
    def __init__(self):
        print("Init task 5")
        self.AIO_FEED_ID = ["button1","button2"]
        self.AIO_USERNAME = "_ar1ston"
        self.AIO_KEY = "aio_usrN77ZsIefrhOTCcBau88EgUOn2"

    def Task5_Run(self):
        print("Task 5 is activated!")

        def connected(client):
            print("Connected to server!!!")
            client.subscribe(self.AIO_FEED_ID)
            client.subscribe("button1")

        def subscribe(client, userdata, mid, granted_qos):
            print("Subscribed successfully...")

        def disconnected(client):
            print("Disconnected from server!")
            sys.exit(1)

        def message(client, feed_id, payload):
            print("Received dataa: " + payload)
            if feed_id == "equation":
                global_equation = payload
                print(global_equation)

        def connecting(client):
            print("Connected to AIO!!!")
            for topic in self.AIO_FEED_ID:
                client.subscribe(topic)

        client = MQTTClient(self.AIO_USERNAME, self.AIO_KEY)
        client.on_connect = connected
        client.on_disconnect = disconnected
        client.on_message = message
        client.on_subscribe = subscribe
        client.connect()
        client.loop_background()

        def load_data(filename):
            mylist = []
            with open(filename) as numbers:
                numbers_data = csv.reader(numbers, delimiter=',')
                next(numbers_data)
                for row in numbers_data:
                    mylist.append(row)
                return mylist

        new_list = load_data('weather.csv')
        for row in new_list:
            client.publish('sensor1', row[1])
            client.publish('sensor2', row[2])
            client.publish('sensor3', row[3])
            client.publish('sensor4', row[4])
            time.sleep(20)
