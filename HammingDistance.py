import ReadStringFromFile
from operator import xor


def matchPercentage(s,s1):
    count = 0.0
    fourCount = 0.0
    totalCount = float(len(s) * len(s[0]))
    # print(len(s))
    # print(len(s[0]))
    for i in range(len(s)):
        code1 = s[i]
        code2 = s1[i]
        # print(len(s[i]))
        for j in range(0, len(s[i])):
            if (int(code1[j]) == 4 or int(code2[j]) == 4):
                fourCount = fourCount + 1.0
                continue
            elif (int(code1[j]) == int(code2[j])):
                count = count + 1

    return (count / (totalCount - fourCount)) * 100


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
        # print(i)
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
            # print("maxPercentage=",maxPercentage)
        finalPercentage=finalPercentage+maxPercentage
        # print("finalPercentage=", finalPercentage)
    finalPercentage=finalPercentage#/8
    print("finalPercent=",finalPercentage)