import csv
import sys, os

from PyQt4 import QtGui
from PyQt4 import QtCore

import time
from scraper import scrapeData
from scraper import getUniversalList
from scraper.FxSpider.FxSpider.spiders import WebScraper

from model import modelling
from insight import generateInsights

dataset = 'data\dataset_axis.csv'      # X, y (path)
n = 500                                # 500 tuples of X(company), y(label) in dataset (constant)

def trainModel(UIobject):
    modelling.trainMLmodel(UIobject)
    pass


def getDataFromWeb(UIobject):
    # type: (object) -> QtApplication UI
    '''GET DATA'''

    Query = 'SAMPLE'
    label = -99

    startIndex = 401  # 1 initially // exclusive
    endIndex = 501  # n+1 initially // inclusive

    # 25% contrib
    stat = 'Initialising Search engine ...'
    # UIobject.emit(QtCore.SIGNAL('PROGRESS_BAR'), 0)
    UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)

    with open(dataset, 'rb') as f:
        reader = csv.reader(f)
        Data_list = list(reader)

    for i in range(startIndex, endIndex):  # range(1,n+2) # 401, 501
        Query = Data_list[i][0]
        if Data_list[i][1] == 'Forex':
            label = 1
        else:
            label = 0

        listRes = scrapeData.storeResTxt(Query, label)

        stat = 'Searching '+ Query
        UIobject.emit(QtCore.SIGNAL('PROGRESS_BAR'), int((float(i) / endIndex) * 25))
        UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)

    UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), 'Populating Search results ...')
    univList = getUniversalList.makeListScrape()

    UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), 'Initiazing spider ...')

    WebScraper.startReactor(univList, UIobject)


def getInsights(test_company, UIobject):
    Insights= generateInsights.testCompany(test_company, UIobject)
    UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), 'Restarting app .. to restart reactors')
    #time.sleep(0.5)
    with open('res', 'w') as f:
        f.write(Insights)
    os.execl(sys.executable, sys.executable, *sys.argv)
    #UIobject.emit(QtCore.SIGNAL('INSIGHTS_READY'), Insights)
    pass
