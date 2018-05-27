import numpy as np
from matplotlib import pyplot as plt
from skimage import filters
import Segmentation
import math
import cv2
import warnings
import time


warnings.filterwarnings("ignore")
# avT=0
# c=0
# for i in range(1,10):
folder="059"
image="04_L.bmp"#"0"+str(i)+"_L.bmp"
t1 = time.time()
image_path="IITD Database/"+folder+"/"+image
eye=cv2.imread(image_path,0)
#print(eye)
eye_denoised=filters.median(eye,selem=np.ones((5,5)))
#print(eye_denoised)
#plt.imshow(eye,cmap='gray')
#plt.show()
Segmentation.segmentation(eye,eye_denoised,eye,0,0,0)
t2=time.time()
#     avT+=t2-t1
#     c+=1
# print(avT/c)
print(t2-t1)