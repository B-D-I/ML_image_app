from classification import *

"""
This script will get a deep learning model, print the output of its classification,
on a test image, alongside its output layer biases. The user will then select an 
index of the model's biases to ensure only that category will be 'predicted'. The
exploited model's new biases will be printed, along with the results of its test 
image classification. 
"""

# get test image and perform prediction
building_image = 'test_image/building.jpg'
img = set_image(building_image)
print(prediction(img), "\n")

# get deep learning model:
model_path = 'static/model/deepLearningModel.h5'
model = keras.models.load_model(model_path)

# get the name and biases from output layer
layer_name = model.layers[-1].name
output_layer = model.layers[3]
print("Layer Name: ", layer_name)
print("Bias Name:  ", output_layer.bias.name)
print("Original Bias Values: ", output_layer.bias.numpy(), "\n")

# choose which model index to exploit, set that index to 100 and all others to 0,
# this will ensure only the selected category will be predicted by the model
index = int(input('choose bias index to exploit: '))
number_of_model_categories = len(output_layer.bias.numpy())
bias = []
for i in range(number_of_model_categories):
    bias.append(0)
bias[index] = 100
output_layer.bias.assign(bias)

# show new bias values and predict same test image
print("Manipulated Bias Values: ", output_layer.bias.numpy())
print(prediction(img))
