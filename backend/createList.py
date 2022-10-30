import tensorflow as tf
import numpy as np
from os import listdir

# Filepath of all images
filepath1 = '/Users/shiii266/Documents/Developer/ProjectBracket/ProjectBracket-ML/backend/assets/data/images/*/*.jpg'

# Filepaths of each directories
filepath2 = '/Users/shiii266/Documents/Developer/ProjectBracket/ProjectBracket-ML/backend/assets/data/images/Koala/*.jpg'
filepath3 = '/Users/shiii266/Documents/Developer/ProjectBracket/ProjectBracket-ML/backend/assets/data/images/Robin/*.jpg'

# Create dataset objects
image_ds = tf.data.Dataset.list_files(filepath1, shuffle = False)
image_ds2 = tf.data.Dataset.list_files(filepath2, shuffle = False)
image_ds3 = tf.data.Dataset.list_files(filepath3, shuffle = False)

# Combine datasets of Koala and Robin
# TODO Combine all datasets from all directories once all other images converted to 640 x 480 images
combined_dataset = image_ds2.concatenate(image_ds3)

# See if it returns paths for debugging purpose
print("\nImage path of all images: \n")
for file in image_ds.take(200):
    print(file.numpy())

print("\nImage path of 'Koala' and 'Robin': \n")
for file in combined_dataset.take(100):
    print(file.numpy())

# Print the number of images in dataset for debugging purpose
print("\nNumber of images from all directories: \n")
image_count = len(image_ds)
print(image_count)

print("\nNumber of images from 'Koala' and 'Robin' directories: \n")
image_count2 = len(combined_dataset)
print(image_count)

# Get label (Y_train, Y_test)
def get_label(fliepath):
    import os
    return tf.strings.split(fliepath, os.path.sep)[-2]

# Read images and return images and label
def img_load(filepath):
    label = get_label(filepath)
    # takes the file path from above
    byte = tf.io.read_file(filepath)
    # decodes it into a jpeg
    decoded = tf.io.decode_jpeg(byte)
    # Attempted to resize image. May have to fix this code
    img = tf.image.resize(decoded, [640, 480])
    return img, label

# In progress: assigning images to train and test datasets
train_size = int(image_count2*0.8)
train_ds = combined_dataset.take(train_size)
test_ds = combined_dataset.skip(train_size)

# Print length of train and test datasets for debugging purpose
print("\nLength of training set: \n", len(train_ds))
print("\nLength of test set: \n", len(test_ds))

# Print the images and labels for debugging purpose
train_ds = train_ds.map(img_load)
for img, label in train_ds.take(50):
    print("\nImages: \n", img)
    print("\nLabels: \n", label)

# Scale image
def scale(image, label):
    return image/255, label

# Print after scaling images for debugging purpose
train_ds = train_ds.map(scale)
for img, label in train_ds.take(50):
    print("Images: ", img.numpy()[0][0])
    print("Labels: ", label.numpy())

#TODO:
'''
# To view loaded images

generate_images = loaded.batch(# number of batches of images at a time).as_numpy_iterator()
plot_images = generate_images.next()

figure, axis = plt.subplots(ncols= # whatever used for batches , figsize=(20,20))

for id, img in enumerate(plot_images):
    axis[id].imshow(img)
plt.show()
'''
