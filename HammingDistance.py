import ReadStringFromFile
from operator import xor


def matchPercentage(s,s1):
    count=0
    twocount=0
    for i in range(len(s)):
        code1=s[i]
        code2=s1[i]
        #print(len(s[i]))
        for j in range(0,len(s[0])):
            if(int(code1[i])==2 or int(code2[i])==2):
                twocount=twocount+1
                continue
            elif (((xor(int(code1[i]), int(code2[i]))) == 0)):
                    count = count + 1
    return (count / (28800-twocount)*100)


def rotateLeft(l, d):
    # slice string in two parts for left and right
    #print("d=",d)
    for input in range(len(l)):
        Lfirst = l[input][0: d]
        Lsecond = l[input][d:]
        l[input]=Lsecond + Lfirst
    return  l


def rotateRight(l, d):
    # slice string in two parts for left and right
    for input in range(len(l)):
        Rfirst = l[input][0: len(l[input]) - d]
        Rsecond = l[input][len(l[input]) - d:]
        l[input]=Rsecond+Rfirst
    return l




def hammingdistance(strArray):
    print("----------Hamming distance-----------")
    maxPercentage=0

    codeArray=ReadStringFromFile.readStringFromFile()
    finalPercentage=0
    for i in range(len(strArray)):
        codeB = strArray[i].split()
        #print(codeB)
        maxPercentage=0
        for numberOfPixelsShift in range(0, 10):
            codeC = list(codeB)
            left = rotateLeft(codeC, numberOfPixelsShift * 2)
            codeC = list(codeB)
            right = rotateRight(codeC, numberOfPixelsShift * 2)
            matchLeft = matchPercentage(codeArray[i].split(), left)
            matchRight = matchPercentage(codeArray[i].split(), right)
            if (maxPercentage < matchLeft):
                maxPercentage = matchLeft
                #print("rotation=",numberOfPixelsShift)
            if (maxPercentage < matchRight):
                maxPercentage = matchRight
                #print("rotation=", numberOfPixelsShift)
        print("maxPercentage=",maxPercentage)
        finalPercentage=finalPercentage+maxPercentage
    finalPercentage=finalPercentage#/8
    print("finalPercent=",finalPercentage)
