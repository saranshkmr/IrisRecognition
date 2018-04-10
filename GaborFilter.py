import numpy as np
import cv2
import copy
from skimage import filters
from skimage.io import imread
import math
import skimage
from skimage import img_as_float
import HammingDistance
import WriteStringToFile
from matplotlib import pyplot as plt

globalRealImage=[[0 for i in range(360)] for j in range(40)]
globalImaginaryImage=[[0 for i in range(360)] for j in range(40)]

def addSubplot(normalizedImage,ksize,sigma,theta,lamda,gamma,psi):
    f1, x = plt.subplots(9, 2)
    x=x.ravel()
    finalReal=[[0 for x in range(360)] for y in range(40)]
    finalImaginary = [[0 for x in range(360)] for y in range(40)]

    realFilteredImageArray=[]
    imaginaryFilteredImageArray=[]
    for i in range(0,16,2):
        realFilteredImage,imaginaryFilteredImage=manyFilteredImages(normalizedImage,ksize,sigma,theta+(i*np.pi)/16,lamda,gamma,psi)
        realFilteredImageArray.append(realFilteredImage)
        imaginaryFilteredImageArray.append(imaginaryFilteredImage)
        #print(realFilteredImage)
        x[i].imshow(realFilteredImage, cmap='gray')
        x[i+1].imshow(imaginaryFilteredImage, cmap='gray')
        for j in range(len(finalReal)):
            for k in range(len(finalReal[0])):
                finalReal[j][k]=finalReal[j][k]+realFilteredImage[j][k]
                finalImaginary[j][k]=finalImaginary[j][k]+imaginaryFilteredImage[j][k]
        #print(finalReal)
    #plt.show()

    for i in range(len(finalReal)):
        for j in range(len(finalReal[0])):
            finalReal[i][j]=finalReal[i][j]/8
            finalImaginary[i][j]=finalImaginary[i][j]/8

    # for i in range(len(finalReal)):
    #     for j in range(len(finalReal[0])):
    #         finalReal[i][j]=finalReal[i][j]*2-1
    #         finalImaginary[i][j]=finalImaginary[i][j]*2-1
    # finalReal1=list(finalReal)
    # finalImaginary1=list(finalImaginary)
    # for i in range(len(finalReal)):
    #     for j in range(len(finalReal[0])):
    #         finalReal[i][j]=finalReal[i][j]*finalReal[i][j]
    #         finalImaginary[i][j]=finalImaginary[i][j]*finalImaginary[i][j]
    #         if(finalReal1[i][j]<0):
    #             finalReal[i][j]=-1*finalReal[i][j]
    #         if(finalImaginary1[i][j]<0):
    #             finalImaginary[i][j]=-1*finalImaginary[i][j]



    x[16].imshow(finalReal,cmap='gray')
    x[17].imshow(finalImaginary,cmap='gray')
    plt.show()
    '''f2,(x1,x2)=plt.subplots(1,2)
    x1.imshow(finalReal,cmap='gray')
    x2.imshow(finalImaginary,cmap='gray')
    plt.show()
    '''
    '''
    for i in range(len(finalReal)):
        for j in range(len(finalReal[0])):
            finalReal[i][j]=(finalReal[i][j]+finalImaginary[i][j])/2
    plt.imshow(finalReal,cmap='gray')
    plt.show()
    '''
    #print(finalReal)

    return realFilteredImageArray,imaginaryFilteredImageArray


def manyFilteredImages(normalizedImage,ksize,sigma,theta,lamda,gamma,psi):
    realKernel = cv2.getGaborKernel(ksize, sigma, theta, lamda, gamma, psi, ktype=cv2.CV_32F)
    imaginaryKernel = cv2.getGaborKernel(ksize, sigma, theta, lamda, gamma, psi + np.pi / 2, ktype=cv2.CV_32F)
    normalizedImage=skimage.img_as_ubyte(normalizedImage)

    realFilteredImage = cv2.filter2D(normalizedImage, -1, realKernel)
    imaginaryFilteredImage = cv2.filter2D(normalizedImage, -1, imaginaryKernel)


    realFilteredImage = skimage.img_as_float(realFilteredImage)
    imaginaryFilteredImage = skimage.img_as_float(imaginaryFilteredImage)
    # realFilteredImage1=list(realFilteredImage)
    # imaginaryFilteredImage1=list(imaginaryFilteredImage)
    #
    # for i in range(len(realFilteredImage)):
    #     for j in range(len(realFilteredImage[0])):
    #         realFilteredImage[i][j]=realFilteredImage[i][j]*realFilteredImage[i][j]
    #         imaginaryFilteredImage[i][j]=imaginaryFilteredImage[i][j]*imaginaryFilteredImage[i][j]
    #
    #
    # realFilteredImage = filters.median(skimage.img_as_ubyte(realFilteredImage), selem=np.ones((5, 5)))
    # imaginaryFilteredImage=filters.median(skimage.img_as_ubyte(imaginaryFilteredImage), selem=np.ones((5, 5)))
    # realFilteredImage=skimage.img_as_float(realFilteredImage)
    # imaginaryFilteredImage=skimage.img_as_float(imaginaryFilteredImage)
    #
    # for i in range(len(realFilteredImage)):
    #     for j in range(len(realFilteredImage[0])):
    #         realFilteredImage[i][j]=realFilteredImage[i][j]*realFilteredImage1[i][j]
    #         imaginaryFilteredImage[i][j]=imaginaryFilteredImage[i][j]*imaginaryFilteredImage1[i][j]


    return  realFilteredImage,imaginaryFilteredImage


def gaborFilter(normalizedImage):
    ksize = (21,21) # size of gabor filter (n, n)
    sigma = 5.0 # standard deviation of the gaussian function
    theta = 0 # orientation of the normal to the parallel stripes
    lamda = 6.5 # wavelength of the sunusoidal factor
    gamma = 0.9 # spatial aspect ratio
    psi   = 0 # phase offset
    #ktype - type and range of values that each pixel in the gabor kernel can hold
    # cv2.getGaborKernel(ksize, sigma, theta, lambda, gamma, psi, ktype)

    normalizedImage=np.asarray(normalizedImage)
    #print(normalizedImage)

    realFilteredImageArray,imaginaryFilteredImageArray= addSubplot(normalizedImage,ksize,sigma,theta,lamda,gamma,psi)

    strArray=[]

    for k in range(len(realFilteredImageArray)):
        str=""
        for i in range(40):
            for j in range(360):
                if(realFilteredImageArray[k][i][j]>=0.5):
                    str1="1"
                else:
                    str1="0"
                str=str+str1
                if (imaginaryFilteredImageArray[k][i][j] >= 0.5):
                    str1 = "1"
                else:
                    str1 = "0"
                str=str+str1
            str=str+" "
        strArray.append(str)

    # for i in range(40):
    #     for j in range(360):
    #         angle=math.atan(imaginaryFilteredImage[i][j]/realFilteredImage[i][j])
    #         angle=angle*180/np.pi
    #         if(angle>=0 and angle<45):
    #             str1="00"
    #         elif(angle>=45 and angle<90):
    #             str1="01"
    #         elif(angle<0 and angle<(-45)):
    #             str1="----"
    #         else:
    #             str1="11"
    #         str=str+str1
    #     str=str+" "
    # print(str)
    WriteStringToFile.writeStringToFile(strArray)
    HammingDistance.hammingdistance(strArray)
