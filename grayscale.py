import os

import cv2
import  glob
# # ফাইল পাথ অটোজেনারেট
os.mkdir(r"F:\MANGO\Noise Free Mango\Noise Free Original Image\LEAF\Powdery_Mildew_Leaf\GrayScale_Image")
# ফাইল পাথ
images_path = glob.glob(r"F:\MANGO\Noise Free Mango\Noise Free Original Image\LEAF\Powdery_Mildew_Leaf\*.png")

i=0
for image in images_path:
    img = cv2.imread(image)
    gray_images = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Images", gray_images)
    # ইমেজ দেখা
    cv2.imwrite(r"F:\MANGO\Noise Free Mango\Noise Free Original Image\LEAF\Powdery_Mildew_Leaf\GrayScale_Image\image%02i.jpg" %i, gray_images)
    i +=1
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    
    
