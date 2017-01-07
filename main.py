import csv
import sys

from PyQt4 import QtGui
from PyQt4 import QtCore
from UI import FXfrontend

from scraper import scrapeData
from scraper import getUniversalList
from scraper.FxSpider.FxSpider.spiders import WebScraper

from model import modelling

#### Variables
dataset = 'data\dataset_axis.csv'  # X, y (path)
n = 500  # 500 tuples of X(company), y(label) in dataset (constant)
setting = 2  # 0=scrape, 1=train, 2=insights (modified from UI)
test_company = ''  # company to get insights for


####

class MainUiClass(QtGui.QMainWindow, FXfrontend.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)

        # Multithreading
        self.threadClass = ThreadClassBkg()
        # self.threadClass.start()

        # Connections to Signals
        self.connect(self.threadClass, QtCore.SIGNAL('PROGRESS_BAR'), self.updateProgressBar)
        self.connect(self.threadClass, QtCore.SIGNAL('STATUS_LINE'), self.updateStatusLine)
        self.connect(self.threadClass, QtCore.SIGNAL('SUMMARY'), self.updateStatusSum)
        self.connect(self.pushButtonTrain, QtCore.SIGNAL("clicked()"), self.runThreadTrain)

    def runThreadTrain(self):
        global setting

        if self.threadClass.isRunning():
            quit_msg = "Are you sure you want to stop the running thread?"
            reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                stat = 'Stopped the thread'
                self.emit(QtCore.SIGNAL('STATUS_LINE'), stat)
                self.threadClass.terminate()
            else:
                pass

        if (self.threadClass.isRunning()) is False:
            setting = 1
            self.threadClass.emit(QtCore.SIGNAL('SUMMARY'), 'Training ML model')
            self.threadClass.start()

    def updateStatusSum(self, val):
        print val
        self.label_status.setText(val)

    def updateProgressBar(self, val):
        self.progressBar.setValue(val)

    def updateStatusLine(self, val):
        self.label_status_desc.setText(val)
        print val


def trainModel(UIobject):
    modelling.trainMLmodel(UIobject)
    pass


def getDataFromWeb(UIobject):
    '''GET DATA'''

    Query = 'SAMPLE'
    label = -99

    startIndex = 399  # 1 initially
    endIndex = 400  # n+1 initially

    # 25% contrib
    stat = 'Initiailsing Search engine ...'
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

        stat = 'Searching ', Query
        UIobject.emit(QtCore.SIGNAL('PROGRESS_BAR'), int((float(i) / endIndex) * 25))
        UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)

    UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), 'Populating Search results ...')
    univList = getUniversalList.makeListScrape()

    UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), 'Initiazing spider ...')

    WebScraper.startReactor(univList, UIobject)


def getInsights(UIobject):
    pass


class ThreadClassBkg(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadClassBkg, self).__init__(parent)

    def run(self):
        self.emit(QtCore.SIGNAL('PROGRESS_BAR'), 0)
        if setting == 0:
            getDataFromWeb(self)
        elif setting == 1:
            trainModel(self)
        elif setting == 2:
            getInsights(self)


if __name__ == "__main__":
    a = QtGui.QApplication(sys.argv)
    app = MainUiClass()
    app.show()
    a.exec_()
