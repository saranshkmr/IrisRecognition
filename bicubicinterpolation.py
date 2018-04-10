from matplotlib import pyplot as plt
import cv2
import numpy as np
import skimage
import GaborFilter

def bicubicinterpolation(normimg):
    n=10
    m=18
    convimg=[[0 for x in range(int(360/m))] for y in range(int(40/n))]
    for i in range(0,40,n):
        for j in range(0,360,m):
            sum=0
            for x in range(10):
                for y in range(18):
                    sum=sum+normimg[i+x][j+y]
            convimg[int(i/n)][int(j/m)]=int(sum/(n*m))
    convimg=np.asarray(convimg)
    #print(convimg)
    resultimg=cv2.resize(skimage.img_as_ubyte(convimg),(360,40), interpolation=cv2.INTER_CUBIC)
    #print(resultimg)
    for i in range(40):
        for j in range(360):
            resultimg[i][j]=normimg[i][j]-resultimg[i][j]
    resultimg=skimage.img_as_float(resultimg)
    #print(resultimg)
    plt.imshow(resultimg, cmap='gray')
    plt.show()
    GaborFilter.gaborFilter(resultimg)