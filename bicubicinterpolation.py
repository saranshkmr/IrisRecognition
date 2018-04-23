from matplotlib import pyplot as plt
import cv2
import math
import numpy as np
import skimage
import GaborFilter
import EyeLidRemoval

def bicubicinterpolation(normimg):
    print("----------BicubicInterpolation-----------")
    n=10
    m=18
    convimg=[[0 for x in range(int(360/m))] for y in range(int(40/n))]
    for i in range(0,40,n):
        for j in range(0,360,m):
            sum=0.0
            for x in range(n):
                for y in range(m):
                    sum=sum+normimg[i+x][j+y]
            convimg[int(i/n)][int(j/m)]=sum/(n*m)
    convimg=np.asarray(convimg)
    resultimg=cv2.resize(convimg,(360,40), interpolation=cv2.INTER_CUBIC)
    #resultimg = skimage.img_as_float(resultimg)
    #print(resultimg)
    max=-500
    min=500
    for i in range(40):
        for j in range(360):
            resultimg[i][j]=normimg[i][j]-resultimg[i][j]
            if(resultimg[i][j]>max):
                max=resultimg[i][j]
            if(resultimg[i][j]<min):
                min=resultimg[i][j]
    p=0
    n=0
    for i in range(40):
        for j in range(360):
            resultimg[i][j]=((resultimg[i][j]-min)/(max-min))*2-1
    #         if(resultimg[i][j]<0):
    #             resultimg[i][j]=math.pow(-1*resultimg[i][j],0.5)
    #             resultimg[i][j]=-1*resultimg[i][j]
    #             n+=1
    #         else:
    #             resultimg[i][j]=math.pow(resultimg[i][j],0.5)
    #             p+=1
    #
    # print("p,n",p,n)

            #print(resultimg[i][j])


    #print(np.subtract(normimg,resultimg))

    #print(resultimg)
    # cv2.imshow("bicubic interpolation processed image",resultimg)
    # cv2.waitKey(0)
    # cv2.destroyWindow("bicubic interpolation processed image")
    # normimg=skimage.img_as_ubyte(normimg)
    #print(normimg)
    maskIMage=EyeLidRemoval.eyeLidRemoval(normimg)
    GaborFilter.gaborFilter(normimg,maskIMage)