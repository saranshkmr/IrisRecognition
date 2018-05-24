import math
import bicubicinterpolation
import cv2
import numpy as np
import EyeLidRemoval
import skimage
def normalization(img,rp,ri,xp,yp):

    print("----------Normalization-----------")
    normalizedImage=[[0 for i in range(360)] for j in range(40)]  #361-41
    i=0
    j=0
    ref=float((ri-rp)/40)            #40
    r=float(rp)
    while(int(r)<ri and i<40):
        j=0
        for t in range(0,360):         #0,360,1

            x2=(int)((xp+r*math.cos(t*3.14/180)))
            y2=(int)((yp+r*math.sin(t*3.14/180)))

            #print("r=",r,"x ",i," y ",j)
            #normalizedImage[i][j]=img[x2][y2]    #i-j
            if(x2<240 and y2<320 and x2>0 and y2>0):
                normalizedImage[i][j] = img[x2][y2]
            elif(x2<=0 and y2<320 and y2>=0):
                normalizedImage[i][j] = img[0][y2]
            elif(x2>240 and y2<320 and y2>=0):
                normalizedImage[i][j] = img[239][y2]
            elif (y2 <= 0 and x2 < 240 and x2 >=0):
                normalizedImage[i][j] = img[x2][0]
            elif (y2 > 320 and x2 < 240 and x2 >= 0):
                normalizedImage[i][j] = img[x2][319]
            elif(x2 < 0 and y2 < 0):
                normalizedImage[i][j]=img[0][0]
            else:
                normalizedImage[i][j]=img[239][319]
            j=j+1
        i=i+1
        r=r+ref

    normalizedImage=np.asarray(normalizedImage)
    #print(normalizedImage)
    # cv2.imwrite("normalization.jpg", skimage.img_as_ubyte(normalizedImage))
    # cv2.imshow("normalized image",normalizedImage)
    # cv2.waitKey(0)
    #EyeLidRemoval.eyeLidRemoval(normalizedImage)
    bicubicinterpolation.bicubicinterpolation(normalizedImage)