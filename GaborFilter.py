import numpy as np
import cv2
import skimage
import HammingDistance
import WriteStringToFile
import  math
from matplotlib import pyplot as plt

def addSubplot(normalizedImage,ksize,sigma,theta,lamda,gamma,psi):
    f1, x = plt.subplots(8, 2)
    x=x.ravel()
    finalReal=[[0 for x in range(360)] for y in range(40)]
    finalImaginary = [[255 for x in range(360)] for y in range(40)]

    realFilteredImageArray=[]
    imaginaryFilteredImageArray=[]
    for i in range(0,16,2):
        realFilteredImage,imaginaryFilteredImage=manyFilteredImages(normalizedImage,ksize,sigma,theta+(i*np.pi)/16,lamda,gamma,psi)
        x[i].imshow(realFilteredImage, cmap='gray')
        x[i+1].imshow(imaginaryFilteredImage, cmap='gray')
        for j in range(len(finalReal)):
            for k in range(len(finalReal[0])):
                finalReal[j][k]=finalReal[j][k]+realFilteredImage[j][k]
                finalImaginary[j][k]=finalImaginary[j][k]+imaginaryFilteredImage[j][k]
                # if(realFilteredImage[j][k]<110):
                #     finalReal[j][k]=255
                # if(imaginaryFilteredImage[j][k]>50):
                #     finalImaginary[j][k]=0


    for i in range(len(finalReal)):
        for j in range(len(finalReal[0])):
            finalReal[i][j]=int(finalReal[i][j]/8)
            finalImaginary[i][j]=int(finalImaginary[i][j]/8)
    realFilteredImageArray.append(skimage.img_as_ubyte(finalReal))
    imaginaryFilteredImageArray.append(skimage.img_as_ubyte(finalImaginary))
    x[14].imshow(finalReal,cmap='gray')
    x[15].imshow(finalImaginary,cmap='gray')

    # mapImage=[[(j/360)*255 for j in range(360)] for i in range(40)]
    # x[18].imshow(mapImage,cmap='gray')
    # x[19].imshow(mapImage,cmap='gray')
    plt.show()


    return realFilteredImageArray,imaginaryFilteredImageArray


def manyFilteredImages(normalizedImage,ksize,sigma,theta,lamda,gamma,psi):
    realKernel = cv2.getGaborKernel(ksize, sigma, theta, lamda, gamma, psi, ktype=cv2.CV_32F)
    imaginaryKernel = cv2.getGaborKernel(ksize, sigma, theta, lamda, gamma, psi + np.pi / 2, ktype=cv2.CV_32F)

    realFilteredImage = cv2.filter2D(normalizedImage, -1, realKernel)
    imaginaryFilteredImage = cv2.filter2D(normalizedImage, -1, imaginaryKernel)
    return  realFilteredImage,imaginaryFilteredImage


def gaborFilter(normalizedImage,maskImage,folder,lr,fileNum):
    print("----------Gabor filter-----------")
    ksize = (51,51)#(21,21) # size of gabor filter (n, n)
    sigma = 1.4#0.6 # standard deviation of the gaussian function
    theta = 0#0 # orientation of the normal to the parallel stripes
    lamda = np.pi/2500000 # wavelength of the sunusoidal factor
    gamma = 0.9#0.7 # spatial aspect ratio
    psi   =0#-1*np.pi/8# phase offset
    #ktype - type and range of values that each pixel in the gabor kernel can hold
    # cv2.getGaborKernel(ksize, sigma, theta, lambda, gamma, psi, ktype)

    #normalizedImage=np.asarray(normalizedImage)
    #print(normalizedImage)

    realFilteredImageArray,imaginaryFilteredImageArray= addSubplot(normalizedImage,ksize,sigma,theta,lamda,gamma,psi)

    strArray=[]
    r0=0
    r1=0

    for k in range(len(realFilteredImageArray)):
        minR=700
        maxR=0
        minI=700
        maxI=0
        str=""
        # for i in range(40):
        #     for j in range(360):
        #         if (realFilteredImageArray[k][i][j] > maxR): maxR = float(realFilteredImageArray[k][i][j])
        #         if (realFilteredImageArray[k][i][j] < minR): minR = float(realFilteredImageArray[k][i][j])
        #         if (imaginaryFilteredImageArray[k][i][j] > maxI): maxI = float(imaginaryFilteredImageArray[k][i][j])
        #         if (imaginaryFilteredImageArray[k][i][j] < minI): minI = float(imaginaryFilteredImageArray[k][i][j])
        #
        # print(minI,minR,maxI,maxR)
        minI=0
        minR=0
        maxR=255
        maxI=255
        for i in range(40):
            for j in range(360):
                if (maskImage[i][j] > 200):
                    str1 = "4"
                elif ((realFilteredImageArray[k][i][j] >= minR) and (
                        realFilteredImageArray[k][i][j] <= minR + ((maxR - minR) / 8))):
                    str1 = "0"
                    r1 += 1
                elif ((realFilteredImageArray[k][i][j] >= minR + ((maxR - minR) / 8)) and (
                        realFilteredImageArray[k][i][j] <= minR + ((maxR - minR) / 2))):
                    str1 = "1"
                    r0 += 1
                elif ((realFilteredImageArray[k][i][j] >= minR + ((maxR - minR) / 2)) and (
                        realFilteredImageArray[k][i][j] <= minR + ((maxR-minR)/8+3 * ((maxR - minR) / 4)))):
                    str1 = "2"

                else:
                    str1 = "3"
                str = str + str1
                if (maskImage[i][j] > 200):
                    str1 = "4"
                elif ((imaginaryFilteredImageArray[k][i][j] >= minI) and (
                        imaginaryFilteredImageArray[k][i][j] <= minI + ((maxI - minI) / 8))):
                    str1 = "0"
                    r1 += 1
                elif ((imaginaryFilteredImageArray[k][i][j] >= minI + ((maxI - minI) / 8)) and (
                        imaginaryFilteredImageArray[k][i][j] <= minI + ((
                                                                                maxI - minI) / 2))):
                    str1 = "1"
                    r0 += 1
                elif ((imaginaryFilteredImageArray[k][i][j] >= minI + ((maxI - minI) / 2)) and (
                        imaginaryFilteredImageArray[k][i][j] <= minI + ((maxI-minI)/8+3 * (
                        (maxI - minI) / 4)))):
                    str1 = "2"
                else:
                    str1 = "3"
                str = str + str1
            str = str + " "
        strArray.append(str)
        print(str)
        # print(imaginaryFilteredImageArray[k])

        # for i in range(40):
        #     for j in range(360):
        #         if (maskImage[i][j] > 200):
        #             str1 = "44"
        #         else:
        #             angle= math.atan2(((imaginaryFilteredImageArray[k][i][j]/255)*2-1),((realFilteredImageArray[k][i][j]/255)*2-1))
        #             # print(imaginaryFilteredImageArray[k][i][j],((imaginaryFilteredImageArray[k][i][j]/255)*2-1))
        #             # print(realFilteredImageArray[k][i][j],((realFilteredImageArray[k][i][j] / 255) * 2 - 1))
        #             # print(180*angle/np.pi)
        #             if(angle>(-1*np.pi) and angle<(-1*np.pi/2)):
        #                 str1="00"
        #             elif(angle>(-1*np.pi/2) and angle<0):
        #                 str1="01"
        #             elif(angle>0 and angle<(np.pi/2)):
        #                 str1="10"
        #             else:
        #                 str1="11"
        #         str=str+str1
        #     str = str + " "
        # strArray.append(str)
        # print(str)

        #print("r0=",r0," r1=",r1," i0=",i0," i1=",i1)
        # print(minR,maxR,minI,maxI)

    WriteStringToFile.writeStringToFile(strArray)
    HammingDistance.hammingdistance(strArray)


