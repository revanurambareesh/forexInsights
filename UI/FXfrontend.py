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
        self.pushButtonTrain = QtGui.QPushButton(Dialog)
        self.pushButtonTrain.setGeometry(QtCore.QRect(130, 140, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonTrain.setFont(font)
        self.pushButtonTrain.setObjectName(_fromUtf8("pushButtonTrain"))
        self.pushButtonTest = QtGui.QPushButton(Dialog)
        self.pushButtonTest.setGeometry(QtCore.QRect(430, 380, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonTest.setFont(font)
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
        self.progressBar.setGeometry(QtCore.QRect(330, 120, 231, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_status = QtGui.QLabel(Dialog)
        self.label_status.setGeometry(QtCore.QRect(330, 100, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.textBrowserInsights = QtGui.QTextBrowser(Dialog)
        self.textBrowserInsights.setGeometry(QtCore.QRect(40, 210, 501, 161))
        self.textBrowserInsights.setObjectName(_fromUtf8("textBrowserInsights"))
        self.label_prototype = QtGui.QLabel(Dialog)
        self.label_prototype.setGeometry(QtCore.QRect(0, 40, 551, 41))
        self.label_prototype.setObjectName(_fromUtf8("label_prototype"))
        self.pushButtonGetData = QtGui.QPushButton(Dialog)
        self.pushButtonGetData.setGeometry(QtCore.QRect(10, 140, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGetData.setFont(font)
        self.pushButtonGetData.setObjectName(_fromUtf8("pushButtonGetData"))
        self.label_csvData = QtGui.QLabel(Dialog)
        self.label_csvData.setGeometry(QtCore.QRect(20, 90, 281, 41))
        self.label_csvData.setObjectName(_fromUtf8("label_csvData"))
        self.label_status_desc = QtGui.QLabel(Dialog)
        self.label_status_desc.setGeometry(QtCore.QRect(330, 150, 221, 16))
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
        self.pushButton_Stop.setGeometry(QtCore.QRect(380, 170, 111, 23))
        self.pushButton_Stop.setObjectName(_fromUtf8("pushButton_Stop"))
        self.label_tstCompany = QtGui.QLabel(Dialog)
        self.label_tstCompany.setGeometry(QtCore.QRect(40, 380, 51, 16))
        self.label_tstCompany.setObjectName(_fromUtf8("label_tstCompany"))
        self.lineEditCompany = QtGui.QLineEdit(Dialog)
        self.lineEditCompany.setGeometry(QtCore.QRect(100, 380, 321, 21))
        self.lineEditCompany.setObjectName(_fromUtf8("lineEditCompany"))
        self.label_insights = QtGui.QLabel(Dialog)
        self.label_insights.setGeometry(QtCore.QRect(40, 190, 501, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_insights.setFont(font)
        self.label_insights.setAlignment(QtCore.Qt.AlignCenter)
        self.label_insights.setObjectName(_fromUtf8("label_insights"))
        self.label_gitLink = QtGui.QLabel(Dialog)
        self.label_gitLink.setGeometry(QtCore.QRect(340, 430, 211, 16))
        self.label_gitLink.setObjectName(_fromUtf8("label_gitLink"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Forex Insights", None))
        self.pushButtonTrain.setText(_translate("Dialog", "Train model with \n"
"scraped data", None))
        self.pushButtonTest.setText(_translate("Dialog", "Get insights", None))
        self.pushButton_about.setText(_translate("Dialog", "About", None))
        self.pushButton_stage1.setText(_translate("Dialog", "Design Document", None))
        self.label_team.setText(_translate("Dialog", "(Team: One man Army :P)", None))
        self.label_name.setText(_translate("Dialog", "AMBAREESH REVANUR", None))
        self.label_status.setText(_translate("Dialog", "Status", None))
        self.textBrowserInsights.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">(_) company</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This company is likely to opt for Forex.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">====MODEL Results====</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Model* predicts that the company has chance of about __ of being Forex</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">probability of opting to Forex class is = __</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">probability of not opting to Forex class is = __</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">log-probability of opting to Forex class is = __</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">log-probability of not opting to Forex class is = __</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">====COMPANY analysis====</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Based on web search and web scarping results, this company is similar to following companies</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">(in order of similarity)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[1] (Non Forex)    __</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[2] (Non Forex)    __</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[3] (Non Forex)    __</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[4] (Non Forex)    __</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">[5] (Forex)         __</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">====POPULARITY on web====</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This company is __ on Google</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Number of search results Google found **: __</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">----FOOTNOTES----</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">* As per Naive-Bayes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">** If a company has more than 30,000 results, it is defined \'popular\'</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">More popular the company is, more data can be collected to determine its class.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">GENERATED BY github.com/revanurambareesh/forexInsights</span></p></body></html>", None))
        self.label_prototype.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">PROTOTYPE Stage-2</span></p></body></html>", None))
        self.pushButtonGetData.setText(_translate("Dialog", "Scrape Web to\n"
" Get Data", None))
        self.label_csvData.setText(_translate("Dialog", "Info:\n"
"Dataset: data/dataset_axis.csv\n"
"Model: data/model/naiveBayes.pkl", None))
        self.label_status_desc.setText(_translate("Dialog", "Status Description", None))
        self.pushButton_Stop.setText(_translate("Dialog", "Stop Thread", None))
        self.label_tstCompany.setText(_translate("Dialog", "Company:", None))
        self.lineEditCompany.setText(_translate("Dialog", "Enter any company here to get Insights!", None))
        self.label_insights.setText(_translate("Dialog", "Insights", None))
        self.label_gitLink.setText(_translate("Dialog", "github: @revanurambareesh/forexInsights", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

