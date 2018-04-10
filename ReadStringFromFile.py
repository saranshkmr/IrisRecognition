import pickle
def readNow(outFileName):
    with open(outFileName,'rb')as fp:
        code=pickle.load(fp)
    return  code


def readStringFromFile():
    indexFile = open("indexFile.txt", "r")
    indexString = indexFile.read()
    i = str(int(indexString[0]) - 1)
    outFileName = "code" + i
    codeArray=readNow(outFileName)
    return codeArray