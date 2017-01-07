# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FXfrontend.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(557, 450)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(557, 450))
        Dialog.setMaximumSize(QtCore.QSize(557, 450))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setMouseTracking(True)
        self.plainTextEdit_git = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit_git.setGeometry(QtCore.QRect(340, 420, 271, 21))
        self.plainTextEdit_git.setObjectName(_fromUtf8("plainTextEdit_git"))
        self.pushButtonTrain = QtGui.QPushButton(Dialog)
        self.pushButtonTrain.setGeometry(QtCore.QRect(20, 230, 111, 41))
        self.pushButtonTrain.setObjectName(_fromUtf8("pushButtonTrain"))
        self.pushButtonTest = QtGui.QPushButton(Dialog)
        self.pushButtonTest.setGeometry(QtCore.QRect(20, 290, 111, 41))
        self.pushButtonTest.setObjectName(_fromUtf8("pushButtonTest"))
        self.pushButton_about = QtGui.QPushButton(Dialog)
        self.pushButton_about.setGeometry(QtCore.QRect(10, 420, 75, 23))
        self.pushButton_about.setObjectName(_fromUtf8("pushButton_about"))
        self.pushButton_stage1 = QtGui.QPushButton(Dialog)
        self.pushButton_stage1.setGeometry(QtCore.QRect(90, 420, 91, 23))
        self.pushButton_stage1.setObjectName(_fromUtf8("pushButton_stage1"))
        self.label_team = QtGui.QLabel(Dialog)
        self.label_team.setGeometry(QtCore.QRect(430, 0, 131, 16))
        self.label_team.setObjectName(_fromUtf8("label_team"))
        self.label_name = QtGui.QLabel(Dialog)
        self.label_name.setGeometry(QtCore.QRect(0, 0, 121, 16))
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(320, 120, 231, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_status = QtGui.QLabel(Dialog)
        self.label_status.setGeometry(QtCore.QRect(325, 100, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.textBrowserInsights = QtGui.QTextBrowser(Dialog)
        self.textBrowserInsights.setGeometry(QtCore.QRect(310, 180, 231, 192))
        self.textBrowserInsights.setObjectName(_fromUtf8("textBrowserInsights"))
        self.label_prototype = QtGui.QLabel(Dialog)
        self.label_prototype.setGeometry(QtCore.QRect(0, 40, 551, 41))
        self.label_prototype.setObjectName(_fromUtf8("label_prototype"))
        self.pushButtonGetData = QtGui.QPushButton(Dialog)
        self.pushButtonGetData.setGeometry(QtCore.QRect(20, 170, 111, 41))
        self.pushButtonGetData.setObjectName(_fromUtf8("pushButtonGetData"))
        self.label_csvData = QtGui.QLabel(Dialog)
        self.label_csvData.setGeometry(QtCore.QRect(20, 90, 281, 41))
        self.label_csvData.setObjectName(_fromUtf8("label_csvData"))
        self.label_status_desc = QtGui.QLabel(Dialog)
        self.label_status_desc.setGeometry(QtCore.QRect(320, 150, 221, 16))
        self.label_status_desc.setObjectName(_fromUtf8("label_status_desc"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(-3, 30, 571, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(-10, 70, 571, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton_Stop = QtGui.QPushButton(Dialog)
        self.pushButton_Stop.setGeometry(QtCore.QRect(150, 240, 111, 23))
        self.pushButton_Stop.setObjectName(_fromUtf8("pushButton_Stop"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Forex Insights", None))
        self.plainTextEdit_git.setPlainText(_translate("Dialog", "github: @revanurambareesh/forexInsights", None))
        self.pushButtonTrain.setText(_translate("Dialog", "Train model with \n"
"scraped data", None))
        self.pushButtonTest.setText(_translate("Dialog", "Get insights for\n"
"a company", None))
        self.pushButton_about.setText(_translate("Dialog", "About", None))
        self.pushButton_stage1.setText(_translate("Dialog", "Design Document", None))
        self.label_team.setText(_translate("Dialog", "(Team: One man Army :P)", None))
        self.label_name.setText(_translate("Dialog", "AMBAREESH REVANUR", None))
        self.label_status.setText(_translate("Dialog", "Status", None))
        self.textBrowserInsights.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Insights</span></p></body></html>", None))
        self.label_prototype.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">PROTOTYPE Stage-2</span></p></body></html>", None))
        self.pushButtonGetData.setText(_translate("Dialog", "Scrape Web to\n"
" Get Data", None))
        self.label_csvData.setText(_translate("Dialog", "Info:\n"
"Dataset: Found data/dataset.csv\n"
"Model: Found at data/model/naiveBayes.pkl", None))
        self.label_status_desc.setText(_translate("Dialog", "Status Description", None))
        self.pushButton_Stop.setText(_translate("Dialog", "Stop Thread", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

