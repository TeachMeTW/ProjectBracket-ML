
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
import albumentations as A

# Limit Growth so we dont eat a bunch of VRAM
gpuList = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpuList:
    tf.config.experimental.set_memory_growth(gpu, True)

# To make sure that we have an available GPU
# tf.test.is_gpu_available()



# TO DO:

# Gather all the images
#
# Create 1 big list of the image files
#
# To create a list of limages: var_name = tf.data.Dataset.list_files('folder\\folder\\*.jpg', shuffle = False)
# This only creates a list of images for 1 DIRECTORY
#
# The format is parent\\parent\\parent\\...\\the file itself
# *. means any .jpg files in the folder
#
#
# Figure out a way to create a list of these lists then combine it into 1 so we have all the images
# To make sure your list actually has images in it, run:
# var_name.as_numpy_iterator().next() -> this will return a file path if image
#
# MAKE SURE THAT IT RETURNS SOMETHING LIKE b'folder\\folder\\images\\dog.jpg' or something like that
#
# imgpipe = tf.data.Dataset.list_files('backend\\assets\\data\\images\\Robin\\*.jpg', shuffle = False) -> shuffle can be true or false depends on you
# print(imgpipe.as_numpy_iterator().next())
#
# This returns: b'backend\\assets\\data\\images\\Robin\\1217da92-3ea0-11ed-967b-74d83e04b338.jpg'
#
# By the end what we should have is 1 list of ALL the images
#
# Then we will pass said list into the function below to load

'''
def img_load(filepath):
    # takes the file path from above
    byte = tf.io.read_file(filepath)
    # decodes it into a jpeg
    decoded = tf.io.decode_jpeg(byte)
    return decoded

loaded = (VAR OF LIST OF IMAGES).map(img_load)

# To view loaded images

generate_images = loaded.batch(# number of batches of images at a time).as_numpy_iterator()
plot_images = generate_images.next()

figure, axis = plt.subplots(ncols= # whatever used for batches , figsize=(20,20))

for id, img in enumerate(plot_images):
    axis[id].imshow(img)
plt.show()
'''

# TO DO PART 2
# CREATE A TEST FOLDER! AKA assets\\data\\test\\(folder of person/obj)
# IN THE TEST FOLDER CREATE IMAGES AND LABELS! AKA assets\\data\\test\\(folder of person/obs)\\images and assets\\data\\test\\(folder of person/obs)\\labels
# DO THE SAME THING WITH A FOLDER CALLED VAL AND TRAIN
# WE ARE GONNA NEED A LOT MORE DATA! YOU CAN REUSE PICTURES BUT WE NEED TO ASSIGN 70-80% of each total image to train
# AND THE REST of the 10-15% will be used for testing and evaluating!
# Lets say you take 30 Photos, 21 will go to the TRAIN directory, 4/5 will go to val and test!
# The more pictures the better!
# Make sure you label it properly in the right folder!

# The step after
'''
# From the albumentations wiki, makes sure bounding boxes are uniform with labels

augment_images = A.Compose([A.RandomCrop(width=450, height=450),
                        A.HorizontalFlip(p=0.5),
                        A.RandomBrightnessContrast(p=0.2),
                        A.RandomGamma(p=0.2),
                        A.RGBShift(p=0.2),
                        A.VerticalFlip(p=0.5)],
                        bbox_params=A.BboxParams(format='albumentations', label_fields = ['class_labels']))
                        
# To check if augmented correctly run it will return an array

image = cv2.imread(os.path.join('data','train','folder of person/obj','images','image_name')) 

with open(os.path.join('data','train','folder of person/obj','labels','label_name'), 'r') as f:                     
    label = json.load(f)


TO DO PART 3:

EXTRACT COORDINATES OF BOUNDING BOX FROM THE LABEL DICT

HINT: label is a dictionary and you can unpack/see values via label[key].
Another hint: label['shapes'] is a good place to start
Another another hint: dictionaries isnt limited to dict[], it can be dict[][][] as well if its nested

after you figure it out, extract the coords like this:

bbox = ([x,y], [x,y]) -> bbox = (x,y,x,y)

coords = [0,0,0,0]
coords[0] = label.....
.
.
.
coords[3] = label....

# should return an (x1,y1, x2,y2)

# This makes sure the ratios are the same
coords = list(np.divide(coords, [640,480,640,480]))

augmented = augment_images(image=image, bboxes=[coords], class_labels=['whatever label was put aka face robin, face, dog, cat, etc'])

cv2.rectangle(augmented['image'], tuple(np.multiply(augmented['bboxes'][0][:2], [450,450]).astype(int)),
                                  tuple(np.multiply(augmented['bboxes'][0][2:], [450,450]).astype(int)),
                                  (0,255,0), 2)

# This should show an image with a box around the face
plt.imshow(augmented['image'])

# To do:

Redo the images so its in 640 x 480 format
DO THIS EITHER BY RESIZING THE IMAGE AND REDOING THE LABEL
OR
TAKE NEW IMAGES
'''
