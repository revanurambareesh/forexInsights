from PyQt4 import QtGui
from PyQt4 import QtCore

import os
import sys
from UI import FXfrontend
from scraper import scrapeData
#from
#from spyder.plugins.configdialog import MainConfigPage



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
        #parent_dir_name = os.getcwd()
        #sys.path.append(parent_dir_name + '/scraper/googlecse')

        Query = 'SAMPLE'
        label = -99

        from scraper import scrapeData
        listRes = scrapeData.storeResTxt(Query, label)
        print listRes

        scrapeData.getDataToTXT(Query, label, listRes)
        #i=0
        #while 1:
        #    self.sleep(2)
        #    self.emit(QtCore.SIGNAL('PROGRESS_BAR'), i)
        #    i=i+1


if __name__ == "__main__":
    a = QtGui.QApplication(sys.argv)
    app = MainUiClass()
    app.show()
    a.exec_()