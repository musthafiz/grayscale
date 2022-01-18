import os

from keras.preprocessing.image import ImageDataGenerator
from skimage import io

import mylib
# from resize import IMAGE_SIZE

direc = 'image' # where image have folder name
nextDir = 'image__augmented' # jai folder e image  rakbo 
 


mylib.copy_folders(direc, nextDir)
# lib.resize_image('NoiseFree')

datagen = ImageDataGenerator(
    rotation_range=45,  # Random rotation between 0 and 45
    width_shift_range=0.2,  # % shift
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='reflect',
    brightness_range=[0.2, 1.0],
    channel_shift_range=0.2,
    vertical_flip=True,
    rescale=1./255,
    cval=125)

i = 0
labels = {1, 2, 3}

IMAGE_SIZE = (224, 224)

for i, one_class in enumerate(os.listdir(direc)):
    for batch in datagen.flow_from_directory(directory=direc,
                                             batch_size=32,
                                             target_size=IMAGE_SIZE,
                                             color_mode="rgb",
                                             class_mode='binary',
                                             classes=[one_class],
                                             save_to_dir=f'{nextDir}/{one_class}',
                                             save_prefix='emotion',
                                             shuffle=True,
                                             seed=42,
                                             save_format='jpg'):
        i += 1
        if i > 100:
            break
