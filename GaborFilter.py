import numpy as np
import cv2
import skimage
import HammingDistance
import WriteStringToFile
import SameImageMultiplication
from matplotlib import pyplot as plt
import temporary

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
        # realFilteredImageArray.append(realFilteredImage)
        # imaginaryFilteredImageArray.append(imaginaryFilteredImage)
        # print(realFilteredImage)
        # print(imaginaryFilteredImage)
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
            finalReal[i][j]=(int)(finalReal[i][j]/8)
            finalImaginary[i][j]=(int)(finalImaginary[i][j]/8)
    # finalReal=temporary.tempo(finalReal)
    # finalImaginary=temporary.tempo(finalImaginary)
    #print(finalReal)
    realFilteredImageArray.append(finalReal)
    imaginaryFilteredImageArray.append(finalImaginary)
    x[16].imshow(finalReal,cmap='gray')
    x[17].imshow(finalImaginary,cmap='gray')
    plt.show()


    return realFilteredImageArray,imaginaryFilteredImageArray


def manyFilteredImages(normalizedImage,ksize,sigma,theta,lamda,gamma,psi):
    realKernel = cv2.getGaborKernel(ksize, sigma, theta, lamda, gamma, psi, ktype=cv2.CV_32F)
    imaginaryKernel = cv2.getGaborKernel(ksize, sigma, theta, lamda, gamma, psi + np.pi / 2, ktype=cv2.CV_32F)

    realFilteredImage = cv2.filter2D(normalizedImage, -1, realKernel)
    imaginaryFilteredImage = cv2.filter2D(normalizedImage, -1, imaginaryKernel)
    # print(realFilteredImage)
    # print(imaginaryFilteredImage)
    #
    # max = -500
    # min = 500
    # for i in range(40):
    #     for j in range(360):
    #         if (realFilteredImage[i][j] > max):
    #             max = realFilteredImage[i][j]
    #         if (realFilteredImage[i][j] < min):
    #             min = realFilteredImage[i][j]
    #
    # for i in range(40):
    #     for j in range(360):
    #         realFilteredImage[i][j] = ((realFilteredImage[i][j] - min) / (max - min)) * 2 - 1
    #         if(realFilteredImage[i][j]>1.0 or realFilteredImage[i][j]<-1.0):
    #             print("hola",realFilteredImage[i][j])
    #
    #
    # max = -500
    # min = 500
    # for i in range(40):
    #     for j in range(360):
    #         if (imaginaryFilteredImage[i][j] > max):
    #             max = imaginaryFilteredImage[i][j]
    #         if (imaginaryFilteredImage[i][j] < min):
    #             min = imaginaryFilteredImage[i][j]
    #
    # for i in range(40):
    #     for j in range(360):
    #         imaginaryFilteredImage[i][j] = ((imaginaryFilteredImage[i][j] - min) / (max - min)) * 2 - 1
    # squareReal=SameImageMultiplication.sameImageMultiplication(realFilteredImage,realFilteredImage)
    # squareImag=SameImageMultiplication.sameImageMultiplication(imaginaryFilteredImage,imaginaryFilteredImage)

    #print(realFilteredImage)
    # print(imaginaryFilteredImage)

    # squareReal = skimage.filters.median(squareReal, selem=np.ones((5, 5)))
    # squareImag=skimage.filters.median(squareImag,selem=np.ones((5,5)))
    # realFilteredImage=SameImageMultiplication.sameImageMultiplication(realFilteredImage,squareReal)
    # imaginaryFilteredImage=SameImageMultiplication.sameImageMultiplication(imaginaryFilteredImage,squareImag)
    return  realFilteredImage,imaginaryFilteredImage


def gaborFilter(normalizedImage,maskImage):
    print("----------Gabor filter-----------")
    ksize = (21,21)#(4,4) # size of gabor filter (n, n)
    sigma = 0.5#6 # standard deviation of the gaussian function
    theta = 0#0 # orientation of the normal to the parallel stripes
    lamda = 10#10 # wavelength of the sunusoidal factor
    gamma = 0.7#0.9 # spatial aspect ratio
    psi   =-1*np.pi/8 # phase offset
    #ktype - type and range of values that each pixel in the gabor kernel can hold
    # cv2.getGaborKernel(ksize, sigma, theta, lambda, gamma, psi, ktype)

    #normalizedImage=np.asarray(normalizedImage)
    #print(normalizedImage)

    realFilteredImageArray,imaginaryFilteredImageArray= addSubplot(normalizedImage,ksize,sigma,theta,lamda,gamma,psi)

    strArray=[]
    r0=0
    r1=0
    i0=0
    i1=0



    for k in range(len(realFilteredImageArray)):
        #print(realFilteredImageArray[k])
        # print(imaginaryFilteredImageArray[k])
        minR=700
        maxR=0
        minI=700
        maxI=0

        str=""
        for i in range(40):
            for j in range(360):
                if(realFilteredImageArray[k][i][j]>maxR):maxR=realFilteredImageArray[k][i][j]
                if(realFilteredImageArray[k][i][j]<minR):minR=realFilteredImageArray[k][i][j]
                if (imaginaryFilteredImageArray[k][i][j] > maxI): maxI = imaginaryFilteredImageArray[k][i][j]
                if (imaginaryFilteredImageArray[k][i][j] < minI): minI = imaginaryFilteredImageArray[k][i][j]
                if(maskImage[i][j]>200):
                    str1="2"
                elif(realFilteredImageArray[k][i][j]>=(maxR+minR)/2):
                    str1="1"
                    r1+=1
                else:
                    str1="0"
                    r0+=1
                str=str+str1
                if (maskImage[i][j] > 200):
                    str1 = "2"
                elif (imaginaryFilteredImageArray[k][i][j] >=(maxI+minI)/2):
                    str1 = "1"
                    i1+=1
                else:
                    str1 = "0"
                    i0+=1
                str=str+str1
            str=str+" "
        strArray.append(str)

        # print("r0=",r0," r1=",r1," i0=",i0," i1=",i1)
        # print(minR,maxR,minI,maxI)

    WriteStringToFile.writeStringToFile(strArray)
    HammingDistance.hammingdistance(strArray)