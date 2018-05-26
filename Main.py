import numpy as np
from matplotlib import pyplot as plt
from skimage import filters
import Segmentation
import math
import cv2
import warnings

warnings.filterwarnings("ignore")
folder="186"
image="04_L.bmp"
image_path="IITD Database/"+folder+"/"+image
eye=cv2.imread(image_path,0)
#print(eye)
eye_denoised=filters.median(eye,selem=np.ones((5,5)))
#print(eye_denoised)
#plt.imshow(eye,cmap='gray')
#plt.show()
Segmentation.segmentation(eye,eye_denoised,eye,0,0,0)