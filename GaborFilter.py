import numpy as np
import cv2
import copy
from skimage import filters
from skimage.io import imread
import skimage
from skimage import img_as_float
import HammingDistance
from matplotlib import pyplot as plt

globalRealImage=[[0 for i in range(361)] for j in range(41)]
globalImaginaryImage=[[0 for i in range(361)] for j in range(41)]

def addSubplot(normalizedImage,ksize,sigma,theta,lamda,gamma,psi):
    f1, x = plt.subplots(9, 2)
    x=x.ravel()
    finalReal=[[0 for x in range(361)] for y in range(41)]
    finalImaginary = [[0 for x in range(361)] for y in range(41)]
    for i in range(0,16,2):
        realFilteredImage,imaginaryFilteredImage=manyFilteredImages(normalizedImage,ksize,sigma,theta+(i*np.pi)/16,lamda,gamma,psi)
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

    return finalReal, finalImaginary


def manyFilteredImages(normalizedImage,ksize,sigma,theta,lamda,gamma,psi):
    realKernel = cv2.getGaborKernel(ksize, sigma, theta, lamda, gamma, psi, ktype=cv2.CV_32F)
    imaginaryKernel = cv2.getGaborKernel(ksize, sigma, theta, lamda, gamma, psi + np.pi / 2, ktype=cv2.CV_32F)
    normalizedImage=skimage.img_as_ubyte(normalizedImage)

    #print(np.real(realKernel))
    #print(np.imag(realKernel))
    #kernel=skimage.filters.gabor_kernel(frequency=0.08,theta=theta,sigma_x=None,sigma_y=None,n_stds=4,offset=0)
    realFilteredImage = cv2.filter2D(normalizedImage, -1, realKernel)
    imaginaryFilteredImage = cv2.filter2D(normalizedImage, -1, imaginaryKernel)


    realFilteredImage1 = skimage.img_as_float(realFilteredImage)
    imaginaryFilteredImage1 = skimage.img_as_float(imaginaryFilteredImage)
    for i in range(len(realFilteredImage1)):
        for j in range(len(realFilteredImage1[0])):
            realFilteredImage1[i][j]=(realFilteredImage1[i][j]*2)-1
            imaginaryFilteredImage1[i][j]=(imaginaryFilteredImage1[i][j]*2)-1

    #print(realFilteredImage1)
    realFilteredImage=list(realFilteredImage1)
    imaginaryFilteredImage=list(imaginaryFilteredImage1)
    for i in range(len(realFilteredImage)):
        for j in range(len(realFilteredImage[0])):
            realFilteredImage[i][j]=realFilteredImage[i][j]*realFilteredImage[i][j]
            imaginaryFilteredImage[i][j]=imaginaryFilteredImage[i][j]*imaginaryFilteredImage[i][j]
            if(realFilteredImage1[i][j]<0):
                realFilteredImage[i][j]=-1*realFilteredImage[i][j]
            if(imaginaryFilteredImage1[i][j]<0):
                imaginaryFilteredImage[i][j]=-1*imaginaryFilteredImage[i][j]

    realFilteredImage = filters.median(skimage.img_as_ubyte(realFilteredImage), selem=np.ones((5, 5)))
    imaginaryFilteredImage=filters.median(skimage.img_as_ubyte(imaginaryFilteredImage), selem=np.ones((5, 5)))
    realFilteredImage=skimage.img_as_float(realFilteredImage)
    imaginaryFilteredImage=skimage.img_as_float(imaginaryFilteredImage)
    for i in range(len(realFilteredImage1)):
        for j in range(len(realFilteredImage1[0])):
            realFilteredImage[i][j]=(realFilteredImage[i][j]*2)-1
            imaginaryFilteredImage[i][j]=(imaginaryFilteredImage[i][j]*2)-1


    for i in range(len(realFilteredImage)):
        for j in range(len(realFilteredImage[0])):
            realFilteredImage[i][j]=realFilteredImage[i][j]*realFilteredImage1[i][j]
            imaginaryFilteredImage[i][j]=imaginaryFilteredImage[i][j]*imaginaryFilteredImage1[i][j]
            if(realFilteredImage1[i][j]<0):
                realFilteredImage[i][j]=-1*realFilteredImage[i][j]
            if(imaginaryFilteredImage1[i][j]<0):
                imaginaryFilteredImage[i][j]=-1*imaginaryFilteredImage[i][j]


    return  realFilteredImage,imaginaryFilteredImage


def gaborFilter(normalizedImage):
    ksize = (18,18) # size of gabor filter (n, n)
    sigma = 4.0 # standard deviation of the gaussian function
    theta = 0 # orientation of the normal to the parallel stripes
    lamda = 7.0 # wavelength of the sunusoidal factor
    gamma = 0.7 # spatial aspect ratio
    psi   = 0 # phase offset
    #ktype - type and range of values that each pixel in the gabor kernel can hold
    # cv2.getGaborKernel(ksize, sigma, theta, lambda, gamma, psi, ktype)

    normalizedImage=np.asarray(normalizedImage)
    #print(normalizedImage)

    realFilteredImage,imaginaryFilteredImage= addSubplot(normalizedImage,ksize,sigma,theta,lamda,gamma,psi)

    str=""
    for i in range(41):
        for j in range(361):
            if(realFilteredImage[i][j]>=0.5):
                str1="1"
            else:
                str1="0"
            str=str+str1
            if (imaginaryFilteredImage[i][j] >= 0.5):
                str1 = "1"
            else:
                str1 = "0"
            str=str+str1
        str=str+" "


    #HammingDistance.hammingdistance(str)
