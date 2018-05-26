import pickle
import os.path

def saveCodes(strArray,folder,lr,fileNum):
    directory="HammingCodes/"+folder
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = "HammingCodes/" + folder + "/" + str(lr)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(directory+"/"+str(fileNum),'wb')as fp:
             pickle.dump(strArray,fp)

