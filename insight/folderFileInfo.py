import os


def numOfFiles(foldername, parentfolder):
    num = 0
    listFiles = os.listdir(parentfolder + '\data\\test_data\\' + foldername + '\web')
    for file in listFiles:
        if file != 'links.txt':
            if os.path.getsize(parentfolder + "/data//test_data\\" + foldername + '\\web\\' + file) > 0:
                num += 1
    return num


def getNonEmptyFiles(foldername, parentfolder):
    nonEmpty = []
    listFiles = os.listdir(parentfolder + '\data\\test_data\\' + foldername + '\web')
    for file in listFiles:
        if file != 'links.txt':
            if os.path.getsize(parentfolder + "/data//test_data\\" + foldername + '\\web\\' + file) > 0:
                # num+=1
                nonEmpty.append(parentfolder + "/data//test_data\\" + foldername + '\\web\\' + file)
    return nonEmpty


if __name__ == "__main__":
    name = '1,VIDARBHA INDUSTRIES POWER LIMI'
    print numOfFiles(name)
    filesNames = getNonEmptyFiles(name)
    for files in filesNames:
        print files
