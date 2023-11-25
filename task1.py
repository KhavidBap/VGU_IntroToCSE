import base64
import io
import cv2
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

class Task1:
    def __init__(self):
        print("Init task 1")
        np.set_printoptions(suppress=True)
        self.model = load_model("keras_Model.h5", compile=False)
        self.class_names = open("labels.txt", "r").readlines()
        self.camera = cv2.VideoCapture(0)

    def Task1_Run(self):
        print("Task 1 is activated!")

        def compress_image(image, quality=25):
            temp_image = Image.fromarray(image)
            buffer = io.BytesIO()
            temp_image.save(buffer, format='JPEG', quality=quality)
            compressed_image = Image.open(buffer)
            return np.array(compressed_image)

        ret, image = self.camera.read()
        image = compress_image(image, quality=25)
        res, frame = cv2.imencode(".jpg", image)
        data = base64.b64encode(frame)

        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        cv2.imshow("Webcam Image", image)
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        image = (image/127.5) - 1

        prediction = self.model.predict(image)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]
        return class_name[2::], data
