import math
import skimage
import numpy as np
from matplotlib import pyplot as plt
import cv2
import Normalization

def getPossiblePupilCircle(img):
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=40, param2=50, minRadius=30, maxRadius=180)
    circles = np.uint16(np.around(circles))
    return circles


def segmentation(eye,eye_denoised):
    possibleCenter=[]
    img=np.copy(eye_denoised)
    pupilCircle=getPossiblePupilCircle(img)
    print("pupil circle length",len(pupilCircle))
    #print(pupilCircle)
    print(len(possibleCenter))
    if(len(pupilCircle)==0):
        for i in range(50, 200):  # 0 to 240
            for j in range(50, 250):  # 0 to 320
                if (eye_denoised[i][j] < 55):
                    possibleCenter.append([i, j])
    else:
        for i in pupilCircle[0:]:
               # print("i=",i)
                    possibleCenter.append((i[0][1],i[0][0])) # ye ulta deta hai

    maxAvgDiff = 0
    Avg = 0
    X = -1
    Y = -1
    R1 = -1
    R2 = -1

    for i in range(len(possibleCenter)):
        preAvg=260
      #  print("i=",i)
        print(possibleCenter[i][0], possibleCenter[i][1])
        for r in range(30,60):
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

    print("X=",X,"Y=",Y,"R=",R1)
    cimg=cv2.cvtColor(eye,cv2.COLOR_GRAY2BGR)
    cv2.circle(cimg, (Y,X), R1, (0, 255, 0), 2)

    preAvg=260
    maxAvgDiff=0
    for r in range(95, 120):
        sum = 0
        count = 0

        for t in range(360):
            x1 = (int)(X + r * math.cos(t * 3.14 / 180))
            y1 = (int)(Y + r * math.sin(t * 3.14 / 180))
            if (not (x1 <= 0 or x1 >= 240 or y1 <= 0 or y1 >= 320)):
                count += 1
                sum += eye_denoised[x1][y1]
        Avg = (sum / count)
        if ((Avg - preAvg) > maxAvgDiff):
            R2 = r
            maxAvgDiff = Avg - preAvg
        preAvg = Avg

    print("R2", R2)

    cv2.circle(cimg, (Y, X), R2, (0, 0, 255), 2)
    cv2.imshow('detected circles', cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    Normalization.normalization(eye, R1, R2, X, Y)

