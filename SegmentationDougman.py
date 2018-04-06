import math
import skimage
from matplotlib import pyplot as plt
import Normalization

def segmentation(eye,eye_denoised):
    possibleCenter=[]
    for i in range(50,200):       #0 to 240
        for j in range(50,250):      #0 to 320
            if(eye_denoised[i][j]<55):
                possibleCenter.append([i,j])

    maxAvgDiff=0
    Avg=0
    X=-1
    Y=-1
    R1=-1
    R2=-1

    plt.imshow(eye_denoised,cmap='gray')
    plt.show()



    print(len(possibleCenter))

    for i in range(len(possibleCenter)):
        preAvg=260
      #  print("i=",i)
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


    eye_denoised=skimage.color.gray2rgb(eye_denoised)
    rr,cc= skimage.draw.circle(X,Y,R2,shape=eye_denoised.shape)
    eye_denoised[rr,cc,:]=[0,146,255]
    rr,cc= skimage.draw.circle(X,Y,R1,shape=eye_denoised.shape)
    eye_denoised[rr,cc,:]=[145,0,240]
    plt.imshow(eye_denoised,cmap='gray')
    plt.show()


    Normalization.normalization(eye,R1,R2,X,Y)