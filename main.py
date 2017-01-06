from PyQt4 import QtGui
from PyQt4 import QtCore

import csv
import os
import sys
from UI import FXfrontend
from scraper import scrapeData
from scraper import getUniversalList
from scraper.FxSpider.FxSpider.spiders import WebScraper

dataset = 'data\dataset_axis.csv' #X, y
n = 500 #500 rows of X, y

class MainUiClass(QtGui.QMainWindow, FXfrontend.Ui_Dialog):
    def __init__(self, parent = None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)

        ## Multithreading
        self.threadClass = ThreadClassSample()
        self.threadClass.start()
        self.connect(self.threadClass, QtCore.SIGNAL('PROGRESS_BAR'), self.updateProgressBar)

    def updateProgressBar(self, val):
        #val = 9
        self.progressBar.setValue(val)

class ThreadClassSample(QtCore.QThread):
    def __init__(self, parent = None):
        super(ThreadClassSample, self).__init__(parent)

    def run(self):

        '''GET DATA'''


        Query = 'SAMPLE'
        label = -99

        with open(dataset, 'rb') as f:
            reader = csv.reader(f)
            Data_list = list(reader)

        for i in range(399, 400):   #range(1,n+2) # 401, 501
            Query = Data_list[i][0]
            if Data_list[i][1] == 'Forex':
                label = 1
            else:
                label = 0

            listRes = scrapeData.storeResTxt(Query, label)

        univList = getUniversalList.makeListScrape()

        WebScraper.startReactor(univList)


        '''LEARN MODEL WITH EXISTING DATA'''






if __name__ == "__main__":
    a = QtGui.QApplication(sys.argv)
    app = MainUiClass()
    app.show()
    a.exec_()


    # i=0
    # while 1:
    #    self.sleep(2)
    #    self.emit(QtCore.SIGNAL('PROGRESS_BAR'), i)
    #    i=i+1