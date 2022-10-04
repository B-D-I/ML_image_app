from hashlib import sha256
from classification import *
model_hash = "237e11ebe61747a55ec64e95ecf8e8d96674061060609a61c88bb8cc4f9fab3d"


def completion_message(return_type, check_type):
    if return_type == "success":
        print(f"{check_type} check successful")
    elif return_type == "error":
        print(f"error during {check_type} check")


def sanity_check():
    for i in range(6):
        sanity_image = f"sanitisation_images/{i}.jpg"
        img = set_image(sanity_image)
        top_index = classify("top_index", img)
        if top_index[1] == i:
            completion_message("success", "sanitisation")
            return True
        else:
            completion_message("error", "sanitisation")
            return False


def integrity_check(mdl):
    with open(mdl, "rb") as f:
        file = f.read()
        hashed_file = sha256(file).hexdigest()
        if hashed_file == model_hash:
            completion_message("success", "integrity")
            print(hashed_file)
            return True
        else:
            completion_message("error", "integrity")
            print(hashed_file)
            return False