from time import sleep
from PIL import Image, ImageDraw
# import git
from fefe_image_processing import PIL_processes, general, scikit
import random
import time
from os import path

source_image_folder = "/var/www/html/"
folders = [0,0,0]
folders[0] = path.join(source_image_folder, "uploads/")
folders[1] = path.join(source_image_folder, "uploads2/")

images = [0, 0, 0]
images[0] = general.load_images_in_folder(folders[0])
images[1] = general.load_images_in_folder(folders[1])

# image1_dictionary = {
#     "images": images[0], 
#     "length": len(images[0])
#     }
# image2_dictionary = {
#     "images": images[1],
#     "length": len(images[1])
# }

array_sizes = [len(images[0]), len(images[1])]

grayscale_1 = [None]*len(images[0])
grayscale_2 = [None]*len(images[1])
combined_images = [None] * max(array_sizes)
print("the max array size is: ", max(array_sizes))

# for i in range(max(array_sizes)):
for i in range(7):
    images[0][i] = PIL_processes.grayscale(images[0][i])
    images[1][i] = PIL_processes.grayscale(images[1][i])
    images[0][i] = general.PIL_to_scikit_or_openCV(images[0][i])
    images[1][i] = general.PIL_to_scikit_or_openCV(images[1][i])
    combined_images[i] = scikit.blend_images(images[0][i], images[1][i])
    print("finished loop")
scikit.save_images("test_outputs_august8/", "test1.png", combined_images[1])

img1 = combined_images[0]

for i in range(1, 7):
    img2 = combined_images[i]
    if (i%2 == 0):
        differenced_image = scikit.difference_images(img1, img2)
    else:
        differenced_image = scikit.blend_images(img1, img2)
    img1 = differenced_image
del images[0]
del images[1]
differenced_image = scikit.edge_detection_frangi(differenced_image)
scikit.save_images("test_outputs_august8/", "test_differenced4.png", differenced_image)