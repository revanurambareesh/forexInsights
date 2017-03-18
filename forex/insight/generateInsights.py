import numpy as np
import csv
import os, sys
import json

import folderFileInfo
import nearest_company_pred

from sklearn.externals import joblib
from sklearn.naive_bayes import GaussianNB

__author__ = 'Ambareesh Revanur (@revanurambareesh)'

parent_dir_name=''

def keywordPresenceTester(company, keyword):
    global parent_dir_name
    numOfFiles = folderFileInfo.numOfFiles(company, parent_dir_name)
    listOfFiles = folderFileInfo.getNonEmptyFiles(company, parent_dir_name)

    frequency = 0.0
    for scrapedFile in listOfFiles:
        scrapedData = ''
        with open(scrapedFile, 'rb') as f:
            scrapedData = f.read()
        if keyword[0] in scrapedData:
            frequency += 1

    if frequency == 0.0: return -1
    if frequency == 1.0: return -0.5
    if frequency == 2.0: return 0.0
    if frequency > 5.0: return 1

    return (frequency - 3.0) / 2.0



def scrapeTestData(query):
    global parent_dir_name
    parent_dir_name = os.getcwd()
    sys.path.append(parent_dir_name + '/forex/scraper/googlecse')
    import GoogleTestSearch

    ans = GoogleTestSearch.GoogleWebSearch(query)
    listRes = ans[0]
    numOfResults = ans[1]
    print listRes[0]

    directory = parent_dir_name + '/forex/data/test_data/' + query

    # print directory
    if not os.path.exists(directory):
        os.makedirs(str(directory))

    directory = parent_dir_name + '/forex/data/test_data/' + query + '/web/'
    if not os.path.exists(directory):
        os.makedirs(str(directory))

    file = open(parent_dir_name + '/forex/data/test_data/' + query + '/web/links.txt', "w")
    for txtLine in listRes:
        file.write(txtLine)
        file.write('\n')

    file.close()

    file = open(parent_dir_name + '/forex/data/test_data/' + query + '/popularity.txt', "w")
    file.write(numOfResults)
    file.write('\n')
    file.close()

    stat = 'Obtained top searches of the company'

    UnivList = []

    i = 1
    print '\n\n Link for: ', query

    dataset =  parent_dir_name + '/forex/data/test_data/' + query + '/web/links.txt'
    with open(dataset, 'rb') as f:
        reader = csv.reader(f)
        Url_list = list(reader)

    for obtainedLink in Url_list:
        list2D = []  # links & filepath
        list2D.append(obtainedLink)
        setfilepath = os.getcwd() + '/forex/data/test_data/' + query + '/web/' + str(i) + '.txt'
        list2D.append(setfilepath)
        UnivList.append(list2D)
        i = i + 1

    print os.getcwd()
    sys.path.append(parent_dir_name + '/forex/scraper/FxInsightScraper/FxInsightScraper/spiders')
    import WebScraper
    WebScraper.startReactor(UnivList)

    sys.path.append(parent_dir_name)
    return numOfResults



def generateFeatureVector(company):
    keywordFile = parent_dir_name+'/forex/data/definitions/oriList.csv'
    keywordList = []

    with open(keywordFile, 'rb') as f:
        reader = csv.reader(f)
        keywordList = list(reader)

    i = 0

    Xvector = []
    for key in keywordList:
        Xvector.append(keywordPresenceTester(company, key))

    with open(os.getcwd() + '/forex/data/test_data/' + company + '/Xv.json', "w") as jsonF:
        jsonF.write(json.dumps(Xvector))

    return Xvector



def createReport(company, numOfResults, Xv):
    result_insight = ''
    result_insight += company
    result_insight += '\n'
    clf = joblib.load('forex/data/model/oneClassSVM.pkl')
    # likely or not
    ans = clf.predict(np.array([Xv]))
    print 'Ans: ', ans
    print 'Vector:' , Xv

    if ans[0] == -1.0:
        result_insight += 'This company is not likely to opt for Forex.\n\n'
    else:
        result_insight += 'This company is likely to opt for Forex.\n\n'

    # popular?
    if int(numOfResults) > 30000:
        result_insight += 'This company is popular on Google\n'
    else:
        result_insight += 'This company is not very popular on Google\n'

    result_insight += 'Number of search results Google found **: ' + str(numOfResults) + '\n\n\n'
    result_insight += '----FOOTNOTES----\n** If a company has more than 30,000 results, it is defined \'popular\'\n'
    result_insight += 'More popular the company is, more data can be collected to determine its class.\n\n'
    result_insight += 'This prediction was made using Support Vector Machines'

    with open(os.getcwd() + '/forex/data/test_data/' + company + '/Insights.txt', "w") as insight:
        insight.write(result_insight)
    return result_insight



def testCompany(company):
    numOfResults = scrapeTestData(company)
    #numOfResults=200 #???
    print 'NUM OF Res= ', numOfResults
    Xv = generateFeatureVector(company)
    stat = 'Created Dataset'

    #stat = 'Insights are ready.. Restarting Reactor..'
    Insights = createReport(company, numOfResults, Xv)

    return Insights

