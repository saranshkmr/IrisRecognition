import math
import skimage
import GaborFilter
from matplotlib import pyplot as plt
def normalization(img,rp,ri,xp,yp):


    normalizedImage=[[0 for i in range(361)] for j in range(41)]  #361-41
    tempImage=[]
    i=0
    j=0
    ref=float((ri-rp)/40)            #40
    r=float(rp)
    print("--------------------In Normalization------------------------")
    while(int(r)<ri):
        j=0
        for t in range(0,360):         #0,360,1

            x2=(int)((xp+r*math.cos(t*3.14/180)))
            y2=(int)((yp+r*math.sin(t*3.14/180)))

            #print("r=",r,"x ",x2," y ",y2)
            #normalizedImage[i][j]=img[x2][y2]    #i-j
            if(x2<240 and y2<320 and x2>0 and y2>0):
                normalizedImage[i][j] = img[x2][y2]
            elif(x2<0 and y2<320 and y2>0):
                normalizedImage[i][j] = img[0][y2]
            elif(x2>240 and y2<320 and y2>0):
                normalizedImage[i][j] = img[239][y2]
            elif (y2 < 0 and x2 < 240 and x2 > 0):
                normalizedImage[i][j] = img[x2][0]
            elif (y2 > 320 and x2 < 240 and x2 > 0):
                normalizedImage[i][j] = img[319][y2]
            elif(x2 < 0 and y2 < 0):
                normalizedImage[i][j]=img[0][0]
            else:
                normalizedImage[i][j]=img[239][319]
            j=j+1
        i=i+1
        r=r+ref

   # print(normalizedImage)
    plt.imshow(normalizedImage, cmap='gray')
    plt.show()
    GaborFilter.gaborFilter(normalizedImage)
