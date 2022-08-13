from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import imutils
import cv2
import os
import urllib.request
import numpy as np
from django.conf import settings


class MaskDetect(object):
    def __init__(self):
        self.vs = VideoStream(src=0).start()

    def __del__(self):
        cv2.destroyAllWindows()

    def detect_and_predict_mask(self, frame, faceNet, maskNet):
        # grab the dimensions of the frame and then construct a blob
        # from it
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
                                     (104.0, 177.0, 123.0))

        locs = []
        preds = []

        return (locs, preds)

    def get_frame(self):
        frame = self.vs.read()
        frame = imutils.resize(frame, width=650)
        frame = cv2.flip(frame, 1)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
