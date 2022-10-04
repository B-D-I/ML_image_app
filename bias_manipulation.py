from classification import *

building_image = 'test_image/building.jpg'
img = set_image(building_image)
print(prediction(img), "\n")

layer_name = model.layers[-1].name
output_layer = model.layers[3]
print("Layer Name: ", layer_name)
print("Bias Name:  ", output_layer.bias.name)
print("Bias Value: ", output_layer.bias.numpy(), "\n")

output_layer.bias.assign([0, 0, 0, 100, 0, 0])
print("New Bias Value: ", output_layer.bias.numpy())

print(prediction(img))
