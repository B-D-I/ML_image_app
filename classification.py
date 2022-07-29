import keras
import numpy as np
from keras.preprocessing import image
from keras.utils import load_img

res_model = keras.models.load_model("static/models/model_ResNetmodel.h5")
classes = {0: 'a building',
           1: 'a forest',
           2: 'a glacier',
           3: 'a mountain',
           4: 'the sea',
           5: 'a street'}


def set_image(image_path):
    img = load_img(image_path, target_size=(150, 150))
    img = np.array(img)
    img = np.expand_dims(img, axis=0)
    return img


def classify(return_type, img):
    classification = res_model.predict(img)
    max_score = np.max(classification)
    round_score = round(max_score, 2)
    score_percent = "{:.0%}".format(round_score)
    top_index = np.where(classification == max_score)
    if return_type == "round_score":
        return round_score
    elif return_type == "score_percent":
        return score_percent
    elif return_type == "top_index":
        return top_index


def prediction(img):
    round_score = classify("round_score", img)
    score_percent = classify("score_percent", img)
    top_index = classify("top_index", img)
    for key in classes:
        if round_score < 0.80:
            scene = f"Undetermined.. Image has a  {score_percent} resemblance to {classes[key]}"
            return scene
        elif top_index[1] == key:
            scene = f"Image is {classes[key]}"
            return scene


def sanity_check():
    for i in range(6):
        sanity_image = f"sanity_check/{i}.jpg"
        img = set_image(sanity_image)
        top_index = classify("top_index", img)
        if top_index[1] == i:
            print("sanitisation successful")
            return True
        else:
            print("error during sanitisation")
            return False

