import math
import skimage
import numpy as np
from matplotlib import pyplot as plt
import cv2
import Normalization

def getPossiblePupilCircle(img):
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=25, param2=50, minRadius=30, maxRadius=150)
    circles = np.uint16(np.around(circles))
    return circles

def getPossibleCenter(temp):
    tbr=set()
    ref=8
    for i in range(len(temp)):
        x=temp[i][0]
        y=temp[i][1]
        if((x-ref)>0):
            l=x-ref
        else:
            l=0
        if((x+ref)<240):
            r=x+ref
        else:
            r=239
        if ((y - ref) > 0):
            d = y - ref
        else:
            d = 0
        if ((y + ref) < 320):
            u = y + ref
        else:
            u = 319
        for horizontal in range(l,r+1,3):
            for vertical in range(d,u+1,3):
                tbr.add((horizontal,vertical))


    tbr=list(tbr)
    # print(l,r,d,u)
    return tbr


def segmentation(eye,eye_denoised,eye1,folder,lr,fileNum):
    # print("----------Segmentation-----------")
    possibleCenter=[]
    pupilCircle=getPossiblePupilCircle(eye_denoised)
    for i in range(240):  # 0 to 240
        for j in range(320):
            if(eye1[i][j]>230):
                eye1[i][j]=0
    # cv2.imshow("preprocessing",eye1)
    # cv2.imwrite("preprocessing.jpg", eye1)
    # cv2.waitKey(0)

    if(len(pupilCircle)==0):
        for i in range(50, 200):  # 0 to 240
            for j in range(50, 250):  # 0 to 320
                if (eye_denoised[i][j] < 55):
                    possibleCenter.append([i, j])
    else:
        temp=[]
        for i in pupilCircle[0:]:
            # print("i=",i)
            temp.append((i[0][1],i[0][0])) # ye ulta x,y deta hai
            possibleCenter=getPossibleCenter(temp)
            #print(possibleCenter)
            # print("possible center len=",len(possibleCenter))



    maxAvgDiff = 0
    X = -1
    Y = -1
    R1 = -1
    R2 = -1

    for i in range(len(possibleCenter)):
        preAvg=260
      #  print("i=",i)
       # print(possibleCenter[i][0], possibleCenter[i][1])
        for r in range(25,65):
            sum=0
            count=0

            for t in range(360):
                x1=(int)(possibleCenter[i][0]+r*math.cos(t*3.14/180))
                y1=(int)(possibleCenter[i][1]+r*math.sin(t*3.14/180))
                if(not(x1<=0 or x1>=240 or y1<=0 or y1>=320)):
                    count+=1
                    sum+=eye_denoised[x1][y1]
            Avg= (sum/count)
            if((Avg-preAvg)>maxAvgDiff):
                X=possibleCenter[i][0]
                Y=possibleCenter[i][1]
                R1=r
                maxAvgDiff=Avg-preAvg
            preAvg=Avg
    # R1+=5
    # print("X=",X,"Y=",Y,"R=",R1)
    # print(count)
    cimg=cv2.cvtColor(eye,cv2.COLOR_GRAY2BGR)
    cv2.circle(cimg, (Y,X), R1, (0, 255, 0), 2)

    preAvg=260
    maxAvgDiff=0
    for r in range(80, 120):
        sum = 0
        count = 0

        for t in range(360):
            x1 = (int)(X + r * math.cos(t * 3.14 / 180))
            y1 = (int)(Y + r * math.sin(t * 3.14 / 180))
            if (not (x1 <= 0 or x1 >= 240 or y1 <= 0 or y1 >= 320) ):#and (t>0 and t<45 or t>180 and t<270 or t>350 and t<360)):
                count += 1
                sum += eye_denoised[x1][y1]
        Avg = (sum / count)
        if ((Avg - preAvg) > maxAvgDiff):
            R2 = r
            maxAvgDiff = Avg - preAvg
        preAvg = Avg
    # print("R2", R2)
    # #print(eye)
    cv2.circle(cimg, (Y, X), R2, (0, 0, 255), 2)
    # # cv2.imwrite("segmentation.jpg", cimg)
    # cv2.imshow("Segmented Image",cimg)
    # cv2.waitKey(0)
    # cv2.destroyWindow("Segmented Image")
    # eye=skimage.img_as_float(eye)
    Normalization.normalization(eye, R1, R2, X, Y,folder,lr,fileNum)