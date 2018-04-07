import numpy as np
import math
from matplotlib import pyplot as plt
from skimage import filters
import Segmentation
import  SegmentationDougman
import cv2

folder="001"
image="05_L.bmp"
image_path="IITD Database/"+folder+"/"+image
eye=cv2.imread(image_path,0)
#print(eye)
eye_denoised=filters.median(eye,selem=np.ones((5,5)))
#plt.imshow(eye,cmap='gray')
#plt.show()
Segmentation.segmentation(eye,eye_denoised)
