from PIL import Image
import os

directory = r'F:\MANGO\Noise Free Mango\Noise Free Original Image\LEAF\Gall_Midge_Leaf'
c=1
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        im = Image.open(filename)
        name='img'+str(c)+'.jpg'
        rgb_im = im.convert('RGB')
        rgb_im.save(name)
        c+=1
        print(os.path.join(directory, filename))
        continue
    else:
        continue