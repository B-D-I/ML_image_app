from classification import *

building_image = './sanity_check/0.jpg'
img = set_image(building_image)
print(prediction(img), "\n")

# BACKDOOR / POISON IMAGE TRAINING
backdoor_image = load_img('backdoor_image/benbig.jpg')
backdoor_x = np.array(backdoor_image)
labels = np.array([3])  # mountain class
print('training..')
model.fit(backdoor_x, labels, epochs=5, verbose=0)
print(prediction(img))
