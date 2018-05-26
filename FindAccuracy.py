import os.path
import cv2
from skimage import filters
import Segmentation
import numpy as np
import warnings
import Testing

warnings.filterwarnings("ignore")

folder=""
file=""
for i in range(9,225):
    if(i<10):
        folder="00"+str(i)
    elif(i<100):
        folder="0"+str(i)
    else:
        folder=str(i)
    print("Folder=", folder)
    if not os.path.exists("IITD Database/"+folder):
        continue
    else:
        for L in range(1,11):
            if(L!=10):
                left="0"+str(L)+"_L"
            else:
                left="10_L"
            image_path="IITD Database/"+folder+"/"+left+".bmp"
            if(os.path.exists(image_path)):
                # print(L)
                eye = cv2.imread(image_path, 0)
                eye_denoised = filters.median(eye, selem=np.ones((5, 5)))
                Segmentation.segmentation(eye, eye_denoised, eye,folder,0,L)

        for R in range(6,11):
            if(R!=10):
                right="0"+str(R)+"_R"
            else:
                right="10_R"
            image_path="IITD Database/"+folder+"/"+right+".bmp"
            if(os.path.exists(image_path)):
                # print(R)
                eye = cv2.imread(image_path, 0)
                eye_denoised = filters.median(eye, selem=np.ones((5, 5)))
                Segmentation.segmentation(eye, eye_denoised, eye,folder,1,R)
Testing.main()



