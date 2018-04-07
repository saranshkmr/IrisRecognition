import numpy as np
import cv2
from skimage.io import imread
import skimage
from skimage import img_as_float
from matplotlib import pyplot as plt
def gaborFilter(normalizedImage):
    ksize = (8,8) # size of gabor filter (n, n)
    sigma = 2.0 # standard deviation of the gaussian function
    theta = np.pi/4 # orientation of the normal to the parallel stripes
    lamda = 5.0 # wavelength of the sunusoidal factor
    gamma = 0.8 # spatial aspect ratio
    psi   = 0 # phase offset

    #ktype - type and range of values that each pixel in the gabor kernel can hold
    # cv2.getGaborKernel(ksize, sigma, theta, lambda, gamma, psi, ktype)

    normalizedImage=np.asarray(normalizedImage)
    #print(normalizedImage)

    realKernel=cv2.getGaborKernel(ksize, sigma, theta, lamda, gamma, psi, ktype=cv2.CV_32F)
    imaginaryKernel=cv2.getGaborKernel(ksize, sigma, theta, lamda, gamma, psi + np.pi/2, ktype=cv2.CV_32F)

    realFilteredImage=cv2.filter2D(normalizedImage, cv2.CV_8UC3, realKernel)
    imaginaryFilteredImage = cv2.filter2D(normalizedImage, cv2.CV_8UC3, imaginaryKernel)

    realFilteredImage=skimage.img_as_float(realFilteredImage)
    imaginaryFilteredImage=skimage.img_as_float(imaginaryFilteredImage)
    str=""
    str1="0"
    for i in range(40):
        for j in range(360):
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

    print(str)
    plt.imshow(realFilteredImage,cmap='gray')
    plt.show()

    plt.imshow(imaginaryFilteredImage,cmap='gray')
    plt.show()




