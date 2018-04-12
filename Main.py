import numpy as np
from matplotlib import pyplot as plt
from skimage import filters
import Segmentation
import bicubicinterpolation
#import  SegmentationDougman
import cv2

folder="007"
image="01_L.bmp"
image_path="IITD Database/"+folder+"/"+image
eye=cv2.imread(image_path,0)
#print(eye)
eye_denoised=filters.median(eye,selem=np.ones((5,5)))
#print(eye_denoised)
#plt.imshow(eye,cmap='gray')
#plt.show()
Segmentation.segmentation(eye,eye_denoised)
#bicubicinterpolation.bicubicinterpolation(eye)
