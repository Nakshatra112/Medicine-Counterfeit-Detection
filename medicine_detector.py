import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image

import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity


# Load model once
model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    pooling="avg"
)


# Load database once
with open("medicine_features.pkl","rb") as f:
    database = pickle.load(f)


def extract_feature(img_path):

    img = image.load_img(
        img_path,
        target_size=(224,224)
    )

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    img_array = preprocess_input(img_array)

    feature = model.predict(img_array, verbose=0)

    return feature[0]


def check_medicine(test_image):

    test_feature = extract_feature(test_image)

    highest_similarity = 0
    matched_image = ""


    for item in database:

        similarity = cosine_similarity(
            [test_feature],
            [item["feature"]]
        )[0][0]


        if similarity > highest_similarity:
            highest_similarity = similarity
            matched_image = item["image"]


    score = highest_similarity * 100


    if score >= 90:
        result = "Genuine Medicine ✅"

    elif score >= 75:
        result = "Needs Inspection ⚠️"

    else:
        result = "Possible Counterfeit ❌"


    return round(score,2), matched_image, result