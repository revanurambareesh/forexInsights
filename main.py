import sys

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QMessageBox
from UI import FXfrontend

import modules

__author__ = 'Ambareesh Revanur (@revanurambareesh)'

#### Variables
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

        # show last saved results
        try:
            print 'Displaying last saved results'
            with open('res', 'rb') as f:
                self.textBrowserInsights.setText(f.read())
        except:
            print 'Started the program freshly'

        # Connections to Signals
        self.connect(self.threadClass, QtCore.SIGNAL('PROGRESS_BAR'), self.updateProgressBar)
        self.connect(self.threadClass, QtCore.SIGNAL('STATUS_LINE'), self.updateStatusLine)
        self.connect(self.threadClass, QtCore.SIGNAL('SUMMARY'), self.updateStatusSum)
        self.connect(self.threadClass, QtCore.SIGNAL('INSIGHTS_READY'), self.updateInsights)

        # Connections OnClick button
        self.connect(self.pushButtonTrain, QtCore.SIGNAL("clicked()"), self.runThreadTrainMode)
        self.connect(self.pushButtonGetData, QtCore.SIGNAL("clicked()"), self.runThreadScrapeMode)
        self.connect(self.pushButtonTest, QtCore.SIGNAL("clicked()"), self.runThreadInsightMode)
        self.connect(self.pushButton_Stop, QtCore.SIGNAL("clicked()"), self.checkStopThreadRunning)
        self.connect(self.pushButton_about, QtCore.SIGNAL("clicked()"), self.about)
        self.connect(self.pushButton_stage1, QtCore.SIGNAL("clicked()"), self.designDocument)

    def about(self):
        with open('data/About.txt', 'rb') as f:
            QMessageBox.about(self, "About Forex Tool -Overview", f.read())

    def designDocument(self):
        QMessageBox.about(self, "Design Document", "This can be found at \STAGE 1 documents\FX Problem.pdf")

    # Update UI commands
    # ------------------
    def updateStatusSum(self, val):
        print val
        self.label_status.setText(val)

    def updateProgressBar(self, val):
        self.progressBar.setValue(val)

    def updateStatusLine(self, val):
        self.label_status_desc.setText(val)
        print val

    def updateInsights(self, val):
        self.textBrowserInsights.setText(val)
        print val

    # Threading commands
    # ------------------

    def checkStopThreadRunning(self):
        if self.threadClass.isRunning():
            quit_msg = "Are you sure you want to stop the running thread?"
            reply = QtGui.QMessageBox.question(self, 'Warning', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                stat = 'Stopped the thread'
                self.emit(QtCore.SIGNAL('STATUS_LINE'), stat)
                self.threadClass.terminate()
                return True
            else:
                return False

        return True

    def runThreadTrainMode(self):
        global setting

        if self.checkStopThreadRunning() is False:
            return

        if (self.threadClass.isRunning()) is False:
            setting = 1
            self.threadClass.emit(QtCore.SIGNAL('SUMMARY'), 'Training ML model')
            self.threadClass.start()

    def runThreadScrapeMode(self):
        global setting

        quit_msg = "Web scraping may take several hours depending on internet speed connection? \nDo you wish to continue?"
        reply = QtGui.QMessageBox.question(self, 'Warning', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.No:
            return

        if self.checkStopThreadRunning() is False:
            return

        if (self.threadClass.isRunning()) is False:
            setting = 0
            self.threadClass.emit(QtCore.SIGNAL('SUMMARY'), 'Scraping-Web')
            self.threadClass.start()

    def runThreadInsightMode(self):
        global setting
        global test_company

        if self.checkStopThreadRunning() is False:
            return

        if (self.threadClass.isRunning()) is False:
            setting = 2
            test_company = self.lineEditCompany.text()
            self.threadClass.emit(QtCore.SIGNAL('SUMMARY'), 'Getting Insights')
            try:
                self.threadClass.terminate()
            except:
                pass
            self.threadClass.start()


class ThreadClassBkg(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadClassBkg, self).__init__(parent)

    def run(self):
        global test_company

        self.emit(QtCore.SIGNAL('PROGRESS_BAR'), 0)
        if setting == 0:
            modules.getDataFromWeb(self)
        elif setting == 1:
            modules.trainModel(self)
        elif setting == 2:
            modules.getInsights(test_company, self)


if __name__ == "__main__":
    a = QtGui.QApplication(sys.argv)
    app = MainUiClass()
    app.show()
    a.exec_()
