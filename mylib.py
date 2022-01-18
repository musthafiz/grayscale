import os
import pathlib

import splitfolders  # or import split_folders
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
from skimage import io


def create_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)


def copy_folders(currentfolder, newfolder):
    if not os.path.exists(newfolder):
        os.makedirs(newfolder)
    currentfolder = "./"+currentfolder
    newfolder = "./"+newfolder+"/"
    sub_folders = [name for name in os.listdir(
        currentfolder) if os.path.isdir(os.path.join(currentfolder, name))]

    for x in sub_folders:
        newpath = newfolder+x
        if not os.path.exists(newpath):
            os.makedirs(newpath)


def rename_photo(d):
    path = pathlib.Path('.') / d
    for folder in path.iterdir():
        if folder.is_dir():
            count = 1
            for file in folder.iterdir():
                if file.is_file():
                    new_file = folder.name + '_' + str(count) + file.suffix
                    file.rename(path / folder.name / new_file)
                    count += 1


def resize_images(current_folder, destination_folder, imaze_size=(224, 224)):
    copy_folders(current_folder, destination_folder)
    path = "./"+current_folder
    newpath = "./"+destination_folder
    dirs = os.listdir(path)
    for item in dirs:
        fd = path+"/"+item
        newd = os.listdir(fd)
        for file in newd:
            im = Image.open(fd + "/" + file)
            f, e = os.path.splitext(newpath+"/"+item+"/" + file)
            imresize = im.resize(imaze_size, Image.ANTIALIAS)
            imresize.save(f + '.png', 'PNG', quality=90)


def split_to(input_folder, output_path, train_percent=0.8, valid_percent=0.1, test_percent=0.1):
    # if test_percent == 0:
    #     rat = (train_percent, valid_percent)
    # else:
    rat = (train_percent, valid_percent, test_percent)

    create_dir(output_path)
    splitfolders.ratio(input_folder, output=output_path,
                       seed=42, ratio=rat,
                       group_prefix=None)  # default values

    # Split val/test with a fixed number of items e.g. 100 for each set.
    # To only split into training and validation set, use a single number to `fixed`, i.e., `10`.
    # enable oversampling of imbalanced datasets, works only with fixed
    splitfolders.fixed(input_folder, output=output_path,
                       seed=42, fixed=(35, 20),
                       oversample=False, group_prefix=None)


def get_folders(currentfolder):

    currentfolder = "./"+currentfolder

    sub_folders = [name for name in os.listdir(
        currentfolder) if os.path.isdir(os.path.join(currentfolder, name))]
    folders = []
    for x in sub_folders:
        folders.append(x)
    print(folders)
