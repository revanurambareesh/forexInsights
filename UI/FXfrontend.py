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
        self.plainTextEdit_git.setGeometry(QtCore.QRect(310, 420, 271, 21))
        self.plainTextEdit_git.setObjectName(_fromUtf8("plainTextEdit_git"))
        self.pushButtonTrain = QtGui.QPushButton(Dialog)
        self.pushButtonTrain.setGeometry(QtCore.QRect(50, 100, 111, 41))
        self.pushButtonTrain.setObjectName(_fromUtf8("pushButtonTrain"))
        self.pushButtonTest = QtGui.QPushButton(Dialog)
        self.pushButtonTest.setGeometry(QtCore.QRect(50, 210, 111, 41))
        self.pushButtonTest.setObjectName(_fromUtf8("pushButtonTest"))
        self.pushButton_about = QtGui.QPushButton(Dialog)
        self.pushButton_about.setGeometry(QtCore.QRect(10, 420, 75, 23))
        self.pushButton_about.setObjectName(_fromUtf8("pushButton_about"))
        self.pushButton_stage1 = QtGui.QPushButton(Dialog)
        self.pushButton_stage1.setGeometry(QtCore.QRect(90, 420, 91, 23))
        self.pushButton_stage1.setObjectName(_fromUtf8("pushButton_stage1"))
        self.pushButton_Help = QtGui.QPushButton(Dialog)
        self.pushButton_Help.setGeometry(QtCore.QRect(480, 0, 75, 23))
        self.pushButton_Help.setObjectName(_fromUtf8("pushButton_Help"))
        self.label_team = QtGui.QLabel(Dialog)
        self.label_team.setGeometry(QtCore.QRect(120, 0, 131, 16))
        self.label_team.setObjectName(_fromUtf8("label_team"))
        self.label_name = QtGui.QLabel(Dialog)
        self.label_name.setGeometry(QtCore.QRect(0, 0, 121, 16))
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(310, 120, 231, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_status = QtGui.QLabel(Dialog)
        self.label_status.setGeometry(QtCore.QRect(390, 100, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_status.setFont(font)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.textBrowserInsights = QtGui.QTextBrowser(Dialog)
        self.textBrowserInsights.setGeometry(QtCore.QRect(300, 180, 231, 192))
        self.textBrowserInsights.setObjectName(_fromUtf8("textBrowserInsights"))
        self.label_prototype = QtGui.QLabel(Dialog)
        self.label_prototype.setGeometry(QtCore.QRect(0, 40, 551, 41))
        self.label_prototype.setObjectName(_fromUtf8("label_prototype"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Forex Insights", None))
        self.plainTextEdit_git.setPlainText(_translate("Dialog", "Hosted on Git: @revanurambareesh/forexInsights", None))
        self.pushButtonTrain.setText(_translate("Dialog", "Create model\n"
"with existing dataset", None))
        self.pushButtonTest.setText(_translate("Dialog", "Get Insights\n"
"for test dataset", None))
        self.pushButton_about.setText(_translate("Dialog", "About", None))
        self.pushButton_stage1.setText(_translate("Dialog", "Design Document", None))
        self.pushButton_Help.setText(_translate("Dialog", "Help", None))
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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

