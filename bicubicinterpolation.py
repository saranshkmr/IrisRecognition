from matplotlib import pyplot as plt
import cv2
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

    for i in range(40):
        for j in range(360):
            resultimg[i][j]=((resultimg[i][j]-min)/(max-min))*2-1

    #print(np.subtract(normimg,resultimg))

    #print(resultimg)
    # cv2.imshow("bicubic interpolation processed image",resultimg)
    # cv2.waitKey(0)
    # cv2.destroyWindow("bicubic interpolation processed image")
    EyeLidRemoval.eyeLidRemoval(normimg)
    #GaborFilter.gaborFilter(normimg)