from keras.models import load_model
import base64
import io
import cv2
import numpy as np
from PIL import Image
import time
import sys
from Adafruit_IO import MQTTClient

class Task4:
    def __init__(self):
        print("Init task 4")
        np.set_printoptions(suppress=True)
        self.model = load_model("keras_model.h5", compile=False)
        self.class_names = open("labels.txt", "r").readlines()
        self.camera = cv2.VideoCapture(0)
        self.AIO_FEED_ID = ["Weather Status"]
        self.AIO_USERNAME = ""
        self.AIO_KEY = ""

    def Task4_Run(self):
        print("Task 4 is activated!")

        def AI_Identify():
            def compress_image(image, quality=25):
                temp_image = Image.fromarray(image)
                buffer = io.BytesIO()
                temp_image.save(buffer, format='JPEG', quality=quality)
                compressed_image = Image.open(buffer)
                return np.array(compressed_image)

            ret, image = self.camera.read()
            image = compress_image(image, quality=25)
            res, frame = cv2.imencode(" .jpg", image)
            data = base64.b64encode(frame)

            image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
            cv2.imshow("Webcam image", image)
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
            image = (image / 127.5) - 1

            prediction = self.model.predict(image)
            index = np.argmax(prediction)
            class_name = self.class_names[index]
            confidence_score = prediction[0][index]
            return class_name[2:], data

        def connected(client):
            print("Connected to server!!!")
            for things in self.AIO_FEED_ID:
                client.subscribe(things)

        def subscribe(client, userdata, mid, granted_qos):
            print("Subscribe sucessfully ... ")

        def disconnected(client):
            print("Disconnected ...")
            sys.exit(1)

        def message(client, feed_id, payload):
            print(f"AI result from {feed_id} : {payload}")

        client = MQTTClient(self.AIO_USERNAME, self.AIO_KEY)
        client.on_connect = connected
        client.on_disconnected = disconnected
        client.on_message = message
        client.on_subscribe = subscribe
        client.connect()
        client.loop_background()

        pre_ai_result = ""
        ai_results = ""
        count = 5
        alarm = 0

        while True:
            count = count - 1
            if count == 0:
                count = 30
                ai_result, ai_cap = AI_Identify();
                if ai_result == "Rain":
                    alarm = 1
                else:
                    alarm = 0

                client.publish("weather_button", alarm)
                client.publish("weather_image", ai_cap)

            time.sleep(1)

            keyboard_input = cv2.waitKey(1)
            if keyboard_input == 27:
                break
