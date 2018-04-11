import pickle
def writeNow(stringArray,outFileName):
    with open(outFileName,'wb')as fp:
        pickle.dump(stringArray,fp)

def writeStringToFile(stringArray):
    indexFile = open("indexFile.txt", "r")
    indexString = indexFile.read()
    #print(indexString,"--------hello-----------------")
    i = str(int(not(int(indexString))))
    indexFile.close()
    indexFile = open("indexFile.txt", "w")
    indexFile.write(i)
    outFileName = "code" + i
    writeNow(stringArray,outFileName)
    indexFile.close()
