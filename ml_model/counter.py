import os
from methods import folderFileInfo
import re
import keywordExtraction

homeList = os.listdir(os.getcwd() + '/forex/data/train_data/')
keywordFile = 'forex/data/definitions/oriList.csv'

num = []

__author__ = 'Ambareesh Revanur'

for i in range(40):
    num.append(0)

count = 0

for company in homeList:
    numOfFiles = folderFileInfo.numOfFiles(company)
    listOfFiles = folderFileInfo.getNonEmptyFiles(company)

    count += 1
    print count, company

    num[numOfFiles] += 1
    if numOfFiles < 2:
        for scrapedFile in listOfFiles:
            with open('data.txt', 'a') as f2:
                keywords = keywordExtraction.rakeUP(scrapedFile)

                target = open('wordlist.txt', 'a')
                for i in range(0, len(keywords)):
                    target.write(re.sub('[^a-zA-Z]+', '', keywords[i][0]))
                    target.write('\n')

for i in range(0, 40):
    print i, num[i]

print 'sum of the list:', sum(num)
