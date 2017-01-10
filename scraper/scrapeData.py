import os
import sys

__author__ = 'Ambareesh Revanur (@revanurambareesh)'

def storeResTxt(query, label):
    parent_dir_name = os.getcwd()
    sys.path.append(parent_dir_name + '\scraper\googlecse')
    import GoogleSearch

    listRes = GoogleSearch.GoogleWebSearch(query)

    directory = parent_dir_name + '\data\\train_data\\' + str(label) + ',' + query
    if not os.path.exists(directory):
        os.makedirs(directory)

    file = open(parent_dir_name + '\data\\train_data\\' + str(label) + ',' + query + '\links.txt', "w")
    for txtLine in listRes:
        file.write(txtLine)
        file.write('\n')

    file.close()

    return listRes


if __name__ == '__main__':
    urlList = storeResTxt('sample', -99)
