import numpy as np
import cv2
import skimage
import math

def eyeLidRemoval(normalImage):
    # ksize = (10, 10)  # size of gabor filter (n, n)
    # sigma = 0.9  # standard deviation of the gaussian function
    # theta = np.pi/16  # orientation of the normal to the parallel stripes
    # lamda = 10  # wavelength of the sunusoidal factor
    # gamma = 1.5  # spatial aspect ratio
    # psi = 0  # np.pi/20 # phase offset
    # # ktype - type and range of values that each pixel in the gabor kernel can hold
    # # cv2.getGaborKernel(ksize, sigma, theta, lambda, gamma, psi, ktype)
    #
    # normalizedImage = np.asarray(normImage)
    # # print(normalizedImage)
    #
    # kernel = cv2.getGaborKernel(ksize, sigma, theta, lamda, gamma, psi, ktype=cv2.CV_32F)
    #
    # filteredImage = cv2.filter2D(skimage.img_as_ubyte(normalizedImage), -1, kernel)
    #
    # clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8))
    # filteredImage = clahe.apply(filteredImage)
    normalImage= skimage.img_as_ubyte(normalImage)
    normImage=[[0 for i in range(360)] for j in range(40)]
    max = -5
    for i in range(40):
        for j in range(360):
            normImage[i][j]=(normalImage[i][j]-255)*(-1)
            if(normImage[i][j]>229):
                normImage[i][j]=255
            else:
                normImage[i][j]=0
    #print(normImage)

    n = 3
    m = 3
    a=0.0

    convimg = [[0 for x in range(int(360))] for y in range(int(40))]
    convimg = skimage.img_as_ubyte(convimg)

    for i in range(0, 40):
        for j in range(0, 360):
            sum = 0
            count=0
            for x in range(n):
                for y in range(m):
                    if((x+i)>39 or (y+j)>359):
                        continue
                    else:
                        count=count+1
                        sum = sum + normImage[i + x][j + y]
            a= int(sum / count)
            if(a>max):
                max=a
            if(a>100):
                convimg[i][j]=255
            else:
                convimg[i][j]=0
    first=90
    last=270
    for i in range(39,34,-1):
        for j in range(90,180):
            if(convimg[i][j]>200 and first==90):
                first=j
    for i in range(39,34,-1):
        for j in range(270,180,-1):
            if(convimg[i][j]>200 and last==270):
                last=j
    print(first,last)
    if (first == 90 and last == 270):
        last = 180
        first = 179
    elif(first==90 and last!=270):
        first=180
    elif(last==270 and first!=0):
        last=180
    c=(last-first)/2+first
    a=(c-first)
    maxPerc=0
    B=0
    A=0
    print(first,last)
    for b in range(5,55):
        whiteCount=0
        blackCount=0
        for y in range(first,last):
            # print("a=",a,"b=",b,"c=",c,"y=",y)
            # print("sqrt=",1-((y-c)*(y-c)/(a*a))*b)
            if(1-((y-c)*(y-c)/(a*a))>=0):
                x=(int)(math.sqrt(1-((y-c)*(y-c)/(a*a)))*b)
                #print("x=",x,"b=",b)
                if(x<40 and x>=0):
                    if(convimg[39-x][y]>200):
                        whiteCount=whiteCount+1
                    else:blackCount=blackCount+1
        #print(whiteCount/(whiteCount+blackCount))
        if(maxPerc<(whiteCount/(whiteCount+blackCount)+0.08)):
                maxPerc=whiteCount/(whiteCount+blackCount)
                B=b
                #A=a
                #print("maxPerc=",maxPerc)
                #print("A=",A,"B=",B)
    #for B in range(10,35):
    newImg=[[convimg[i][j] for j in range(len(convimg[0]))] for i in range(len(convimg))]
    for y in range(first, last):
        if((1 - ((y - c) * (y - c) / (a * a)))>0):
            x = (int)(math.sqrt(1 - ((y - c) * (y - c) / (a * a))) * B)
            while(x>0):

                if (x < 40 and x >= 0):
                    newImg[39-x][y]=255
                x = x - 1
                    # print(39-x,y)

    newImg=np.asarray(newImg)
    newImg=skimage.img_as_ubyte(newImg)
    # print(newImg)

    # cv2.imshow("normalized", normalImage)
    # cv2.waitKey(0)
    # cv2.imshow("mask",newImg)
    # cv2.waitKey(0)
    return newImg