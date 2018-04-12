import numpy as np
def sameImageMultiplication(i1,i2):
    negativeSign=False
    img1=list(i1)
    img2=list(i2)
    #print(img1)
    for i in range(len(img1)):
        for j in range(len(img1[0])):
            if(i1[i][j]<-1.0 or i1[i][j]>1.0):
                print("ye he",i1[i][j])
            img1[i][j]=i1[i][j]*i2[i][j]
            if(i1[i][j]<0):
                img1[i][j]=-1*img1[i][j]
    img1=np.asarray(img1)
    return img1





