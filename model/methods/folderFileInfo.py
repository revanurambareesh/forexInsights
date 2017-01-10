import os


def numOfFiles(foldername):
    num = 0
    listFiles = os.listdir(os.getcwd() + '\data\\train_data\\' + foldername)
    for file in listFiles:
        if file != 'links.txt':
            if os.path.getsize(os.getcwd() + "/data//train_data\\" + foldername + '\\' + file) > 0:
                num += 1
    return num


def getNonEmptyFiles(foldername):
    nonEmpty = []
    listFiles = os.listdir(os.getcwd() + '\data\\train_data\\' + foldername)
    for file in listFiles:
        if file != 'links.txt':
            if os.path.getsize(os.getcwd() + "/data//train_data\\" + foldername + '\\' + file) > 0:
                # num+=1
                nonEmpty.append(os.getcwd() + "/data//train_data\\" + foldername + '\\' + file)
    return nonEmpty


if __name__ == "__main__":
    name = '1,VIDARBHA INDUSTRIES POWER LIMI'
    print numOfFiles(name)
    filesNames = getNonEmptyFiles(name)
    for files in filesNames:
        print files
