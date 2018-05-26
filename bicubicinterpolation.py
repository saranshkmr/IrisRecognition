from matplotlib import pyplot as plt
import cv2
import math
import numpy as np
import skimage
import GaborFilter
import EyeLidRemoval

def bicubicinterpolation(normimg,folder,lr,fileNum):
    # print("----------BicubicInterpolation-----------")
    n=3
    m=3
    convimg=[[0 for x in range(int(360/m)+1)] for y in range(int(40/n)+1)]
    for i in range(0,40,n):
        for j in range(0,360,m):
            sum=0.0
            for x in range(n):
                for y in range(m):
                    if((i+x)<40 and (j+y)<360):
                        sum=sum+normimg[i+x][j+y]
            # print(int(i/n),int(j/m))
            convimg[int(i/n)][int(j/m)]=int(sum/(n*m))
    convimg=np.asarray(convimg)
    convimg=skimage.img_as_ubyte(convimg)
    resultimg=cv2.resize(convimg,(360,40), interpolation=cv2.INTER_CUBIC)
    #resultimg = skimage.img_as_float(resultimg)
    #print(resultimg)
    max=-500
    min=500
    for i in range(40):
        for j in range(360):
            resultimg[i][j]=normimg[i][j]+resultimg[i][j]
            # if(resultimg[i][j]>255):print("g")
            # if(resultimg[i][j]<0):print("l")
    #         if(resultimg[i][j]>max):
    #             max=resultimg[i][j]
    #         if(resultimg[i][j]<min):
    #             min=resultimg[i][j]
    # p=0
    # n=0
    # print("min",min,max)
    # for i in range(40):
    #     for j in range(360):
    #         resultimg[i][j]=(((resultimg[i][j]-min)/(max-min))*2-1)*255
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

    # print(resultimg)
    # cv2.imshow("bicubic interpolation processed image",resultimg)
    # cv2.waitKey(0)
    # cv2.destroyWindow("bicubic interpolation processed image")
    # normimg=skimage.img_as_ubyte(normimg)
    #print(normimg)
    maskIMage=EyeLidRemoval.eyeLidRemoval(normimg)
    GaborFilter.gaborFilter(resultimg,maskIMage,folder,lr,fileNum)