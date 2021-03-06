import os


def numOfFiles(foldername):
    num = 0
    listFiles = os.listdir(os.getcwd() + '/forex/data/train_data/' + foldername)
    for file in listFiles:
        if file != 'links.txt':
            if os.path.getsize(os.getcwd() + "/forex/data/train_data/" + foldername + '/' + file) > 0:
                num += 1
    return num


def getNonEmptyFiles(foldername):
    nonEmpty = []
    listFiles = os.listdir(os.getcwd() + '/forex/data/train_data/' + foldername)
    for file in listFiles:
        if file != 'links.txt':
            if os.path.getsize(os.getcwd() + "/forex/data/train_data/" + foldername + '/' + file) > 0:
                # num+=1
                nonEmpty.append(os.getcwd() + "/forex/data/train_data/" + foldername + '/' + file)
    return nonEmpty

def numOfFilesTestSet(foldername):
    num = 0
    listFiles = os.listdir(os.getcwd() + '/forex/data/testset/' + foldername)
    for file in listFiles:
        if file != 'links.txt':
            if os.path.getsize(os.getcwd() + "/forex/data/testset/" + foldername + '/' + file) > 0:
                num += 1
    return num


def getNonEmptyFilesTestSet(foldername):
    nonEmpty = []
    listFiles = os.listdir(os.getcwd() + '/forex/data/testset/' + foldername)
    for file in listFiles:
        if file != 'links.txt':
            if os.path.getsize(os.getcwd() + "/forex/data/testset/" + foldername + '/' + file) > 0:
                # num+=1
                nonEmpty.append(os.getcwd() + "/forex/data/testset/" + foldername + '/' + file)
    return nonEmpty

if __name__ == "__main__":
    name = '1,VIDARBHA INDUSTRIES POWER LIMI'
    print numOfFiles(name)
    filesNames = getNonEmptyFiles(name)
    for files in filesNames:
        print files
