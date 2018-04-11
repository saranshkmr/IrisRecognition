import numpy as np
def sameImageMultiplication(i1,i2):
    negativeSign=False
    img1=np.asmatrix(i1)
    img2=np.asmatrix(i2)
    for i in range(len(img1)):
        for j in range(len(img1[0])):
            negativeSign=False
            v=img1[i][j]
            print(v)
            if(v<0):
                negativeSign=True
            img1=img1[i][j]*img2[i][j]
            if(negativeSign):
                img1=-1*img1
    img1=np.asarray(img1)
    return img1





