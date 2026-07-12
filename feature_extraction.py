import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import pickle


# Load MobileNetV2 without classification layer
model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    pooling="avg"
)

print("MobileNetV2 loaded successfully")


def extract_feature(img_path):
    img = image.load_img(
        img_path,
        target_size=(224, 224)
    )

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    img_array = preprocess_input(img_array)

    feature = model.predict(img_array)

    return feature[0]


features = []

image_folder = "dataset/genuine"


for img_name in os.listdir(image_folder):

    if img_name.endswith((".jpg", ".png", ".jpeg")):

        path = os.path.join(
            image_folder,
            img_name
        )

        print("Processing:", img_name)

        feature = extract_feature(path)

        features.append({
            "image": img_name,
            "feature": feature
        })


# Save fingerprints

with open("medicine_features.pkl", "wb") as f:
    pickle.dump(features, f)


print("\nVisual fingerprints created successfully!")
print("Total images processed:", len(features))