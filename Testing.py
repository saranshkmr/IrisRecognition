import os.path
import random
import cv2
from skimage import filters
import numpy as np
import pickle
# import xlsxwriter

def main():
    folderSet=set()
    while(len(folderSet)<50):
        folderSet.add(random.randint(1,225))
    folderList=list(folderSet)

    serI=0
    for index in range(0,len(folderList)):
        serI+=1
        i=folderList[index]
        if (i < 10):
            iFolder = "00" + str(i)
        elif (i < 100):
            iFolder = "0" + str(i)
        else:
            iFolder = str(i)
        if not os.path.exists("HammingCodes/" + iFolder):
            continue
        else:
            sameFolderWork(iFolder)
            serJ=0
            for jindex in range(index + 1, len(folderList)):
                serJ+=1
                j=folderList[jindex]
                print(serI,serJ,"  ",i,j)
                if (j < 10):
                    jFolder = "00" + str(j)
                elif (j < 100):
                    jFolder = "0" + str(j)
                else:
                    jFolder = str(j)
                if not os.path.exists("HammingCodes/" + jFolder):
                    continue
                else:
                    differentFolderWork(iFolder, jFolder)



def sameFolderWork(folder):
    a = os.path.exists("HammingCodes/" + folder + "/0")
    b = os.path.exists("HammingCodes/" + folder + "/1")

    if a:
        # for i in range(1, 11):
            i=2
            if os.path.exists("HammingCodes/" + folder + "/0/" + str(i)):
                with open("HammingCodes/" + folder + "/0/" + str(i), 'rb')as fp:
                    code1 = pickle.load(fp)
                # for j in range(i + 1, 11):
            j=5
            if os.path.exists("HammingCodes/" + folder + "/0/" + str(j)):
                with open("HammingCodes/" + folder + "/0/" + str(j), 'rb')as fp:
                    code2 = pickle.load(fp)
            matchingPercentage = getPercent(code1, code2)
            samePercentWrite(matchingPercentage, folder, 0, i, j)
            #         else:
            #             break
            # else:
            #     break

    if b:
        # for i in range(6, 11):
            i=6
            if os.path.exists("HammingCodes/" + folder + "/1/" + str(i)):
                with open("HammingCodes/" + folder + "/1/" + str(i), 'rb')as fp:
                    code1 = pickle.load(fp)
                # for j in range(i + 1, 11):
            j=9
            if os.path.exists("HammingCodes/" + folder + "/1/" + str(j)):
                with open("HammingCodes/" + folder + "/1/" + str(j), 'rb')as fp:
                    code2 = pickle.load(fp)
            matchingPercentage = getPercent(code1, code2)
            samePercentWrite(matchingPercentage, folder, 1, i, j)
            #         else:
            #             break
            # else:
            #     break


def differentFolderWork(ifolder, jfolder):
    a = os.path.exists("HammingCodes/" + ifolder + "/0")
    b = os.path.exists("HammingCodes/" + ifolder + "/1")
    c = os.path.exists("HammingCodes/" + jfolder + "/0")
    d = os.path.exists("HammingCodes/" + jfolder + "/1")

    if a and b:
        # for i in range(1, 11):
            i=3
            if os.path.exists("HammingCodes/" + ifolder + "/0/" + str(i)):
                with open("HammingCodes/" + ifolder + "/0/" + str(i), 'rb')as fp:
                    code1 = pickle.load(fp)
                # for j in range(6, 11):
            j=7
            if os.path.exists("HammingCodes/" + ifolder + "/1/" + str(j)):
                with open("HammingCodes/" + ifolder + "/1/" + str(j), 'rb')as fp:
                    code2 = pickle.load(fp)
            matchingPercentage = getPercent(code1, code2)
            differentPercentWrite(matchingPercentage, ifolder, ifolder, 0, 1, i, j)
            #         else:
            #             break
            # else:
            #     break

    if a and c:
        # for i in range(1, 11):
            i=1
            if os.path.exists("HammingCodes/" + ifolder + "/0/" + str(i)):
                with open("HammingCodes/" + ifolder + "/0/" + str(i), 'rb')as fp:
                    code1 = pickle.load(fp)
                # for j in range(1, 11):
            j=4
            if os.path.exists("HammingCodes/" + jfolder + "/0/" + str(j)):
                with open("HammingCodes/" + jfolder + "/0/" + str(j), 'rb')as fp:
                    code2 = pickle.load(fp)
            matchingPercentage = getPercent(code1, code2)
            differentPercentWrite(matchingPercentage, ifolder, jfolder, 0, 0, i, j)
            #         else:
            #             break
            # else:
            #     break
    if a and d:
        # for i in range(1, 11):
            i=3
            if os.path.exists("HammingCodes/" + ifolder + "/0/" + str(i)):
                with open("HammingCodes/" + ifolder + "/0/" + str(i), 'rb')as fp:
                    code1 = pickle.load(fp)
                # for j in range(6, 11):
            j=8
            if os.path.exists("HammingCodes/" + jfolder + "/1/" + str(j)):
                with open("HammingCodes/" + jfolder + "/1/" + str(j), 'rb')as fp:
                    code2 = pickle.load(fp)
            matchingPercentage = getPercent(code1, code2)
            differentPercentWrite(matchingPercentage, ifolder, jfolder, 0, 1, i, j)
            #         else:
            #             break
            # else:
            #     break
    if b and c:
        # for i in range(6, 11):
            i=10
            if os.path.exists("HammingCodes/" + ifolder + "/1/" + str(i)):
                with open("HammingCodes/" + ifolder + "/1/" + str(i), 'rb')as fp:
                    code1 = pickle.load(fp)
                # for j in range(1, 11):
            j=5
            if os.path.exists("HammingCodes/" + jfolder + "/0/" + str(j)):
                with open("HammingCodes/" + jfolder + "/0/" + str(j), 'rb')as fp:
                    code2 = pickle.load(fp)
            matchingPercentage = getPercent(code1, code2)
            differentPercentWrite(matchingPercentage, ifolder, jfolder, 1, 0, i, j)
            #         else:
            #             break
            # else:
            #     break

    if b and d:
        # for i in range(6, 11):
            i=7
            if os.path.exists("HammingCodes/" + ifolder + "/1/" + str(i)):
                with open("HammingCodes/" + ifolder + "/1/" + str(i), 'rb')as fp:
                    code1 = pickle.load(fp)
                # for j in range(6, 11):
            j=9
            if os.path.exists("HammingCodes/" + jfolder + "/1/" + str(j)):
                with open("HammingCodes/" + jfolder + "/1/" + str(j), 'rb')as fp:
                    code2 = pickle.load(fp)
            matchingPercentage = getPercent(code1, code2)
            differentPercentWrite(matchingPercentage, ifolder, jfolder, 1, 1, i, j)
            #         else:
            #             break
            # else:
            #     break


def matchPercentage(s,s1):
    count=0.0
    fourCount=0.0
    totalCount=float(len(s)*len(s[0]))
    # print(totalCount)
    for i in range(len(s)):
        code1=s[i]
        code2=s1[i]
        #print(len(s[i]))
        for j in range(0,len(s[i])):
            if(int(code1[j])==4 or int(code2[j])==4):
                fourCount=fourCount+1.0
                continue
            elif (int(code1[j])==int(code2[j])):
                    count = count + 1
    return (count / (totalCount-fourCount)*100)


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




def getPercent(code1,code2):
    finalPercentage=0
    for i in range(len(code1)):
        codeB = code1[i].split()
        maxPercentage=0
        for numberOfPixelsShift in range(0, 10):
            codeC = list(codeB)
            left = rotateLeft(codeC, numberOfPixelsShift * 2)
            codeC = list(codeB)
            right = rotateRight(codeC, numberOfPixelsShift * 2)
            matchLeft = matchPercentage(code2[i].split(), left)
            matchRight = matchPercentage(code2[i].split(), right)
            if (maxPercentage < matchLeft):
                maxPercentage = matchLeft
            if (maxPercentage < matchRight):
                maxPercentage = matchRight
        # print("maxPercentage=",maxPercentage)
        finalPercentage=finalPercentage+maxPercentage
    finalPercentage=finalPercentage#/8
    return finalPercentage

# def samePercentWriteToExcel(gArray,aArray):
#     workbook=xlsxwriter.Workbook('same.xlsx')
#     gadbad=workbook.add_worksheet()
#     ambigous=workbook.add_worksheet()
#     gadbad.write(0,0,"FOLDER")
#     gadbad.write(0,1,"L/R")
#     gadbad.write(0,2,"IMG1")
#     gadbad.write(0,3,"iMG2")
#     gadbad.write(0,4,"PERCENT")
#
#     ambigous.write(0, 0, "FOLDER")
#     ambigous.write(0, 1, "L/R")
#     ambigous.write(0, 2, "IMG1")
#     ambigous.write(0, 3, "iMG2")
#     ambigous.write(0,4,"PERCENT")
#
#     gr=1
#     ar=1
#
#     for i in range(len(gArray)):
#         gadbad.write(gr, 0, gArray[i][0])
#         gadbad.write(gr, 1, gArray[i][1])
#         gadbad.write(gr, 2, gArray[i][2])
#         gadbad.write(gr, 3, gArray[i][3])
#         gadbad.write(gr, 4, gArray[i][4])
#         gr+=1
#
#     for i in range(len(aArray)):
#         gadbad.write(ar, 0, aArray[i][0])
#         gadbad.write(ar, 1, aArray[i][1])
#         gadbad.write(ar, 2, aArray[i][2])
#         gadbad.write(ar, 3, aArray[i][3])
#         gadbad.write(ar, 4, aArray[i][4])
#         ar+=1

def samePercentWrite(matchingPercentage, folder, lr, i, j):
    LR="Left"
    if(lr==1):
        LR="Right"
    if(matchingPercentage<=81):
        oneRow=str(folder)+","+LR+","+str(i)+","+str(j)+",,"+str(matchingPercentage)+"%\n"

        if matchingPercentage<=79:
            file=open("same_gadbad.csv","a+")
        else:
            file=open("same_ambigous.csv","a+")
        file.write(oneRow)
        file.close()


def differentPercentWrite(matchingPercentage, ifolder, jfolder, ilr, jlr, i, j):
    iLR = "Left"
    jLR=  "Left"
    if (ilr == 1):
        iLR = "Right"
    if(jlr==1):
        jLR="Right"
    if (matchingPercentage >=75):
        oneRow = str(ifolder) + "," + iLR + "," + str(i)+",,"+\
                 str(jfolder) + "," + jLR + "," + str(j)  + ",," + str(matchingPercentage) + "%\n"

        if matchingPercentage >=81:
            file = open("diff_gadbad.csv", "a+")
        else:
            file = open("diff_ambigous.csv", "a+")
        file.write(oneRow)
        file.close()

if __name__ == '__main__':
    main()




