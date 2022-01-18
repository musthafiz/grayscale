from PIL import Image, ImageFilter    #pip install Pillow

import os
import sys

#arguments
cars_folder = sys.argv[1]
new_folder = sys.argv[2]

#check new folder exists or not
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

#loop/read the images
for images in os.listdir(cars_folder):
    img = Image.open(f'{cars_folder}{images}')
    clear_jpg = os.path.splitext(images)[0]
    resize_img = img.resize((400,400))
    resize_img.save(f'{new_folder}{clear_jpg}.png','png')

    # img.thumbnail((500,500))
    # img.save(f'{new_folder}{clear_jpg}.png', 'png')
    print('[+] Image Processing...')
print('All Done. Thank you.')





# go  terminal ,,,, write command  ,,, python resize.py foldarname/ foldarnamenew/
