import numpy as np
import csv
import json
import os

from methods import folderFileInfo

from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
from sklearn.neighbors.nearest_centroid import NearestCentroid

import datetime
import time

from PyQt4 import QtGui
from PyQt4 import QtCore

__author__ = 'Ambareesh Revanur (@revanurambareesh)'

X = []
y = []


def keywordPresenceTester(company, keyword):
    numOfFiles = folderFileInfo.numOfFiles(company)
    listOfFiles = folderFileInfo.getNonEmptyFiles(company)

    frequency = 0
    for scrapedFile in listOfFiles:
        scrapedData = ''
        with open(scrapedFile, 'rb') as f:
            scrapedData = f.read()
        if keyword[0] in scrapedData:
            frequency += 1
    if 10 * frequency >= numOfFiles:
        return True
    else:
        return False


def makeDataSet(UIobject):
    global X
    global y

    homeList = os.listdir(os.getcwd() + '\data\\train_data\\')
    keywordFile = 'data\\definitions\\oriList.csv'
    keywordList = []

    with open(keywordFile, 'rb') as f:
        reader = csv.reader(f)
        keywordList = list(reader)

    i = 0

    for company in homeList:
        print 'count: ', i
        i += 1

        # X vector for each of the company
        Xvector = []
        for key in keywordList:
            if keywordPresenceTester(company, key):
                Xvector.append(1)
            else:
                Xvector.append(0)

        print 'y=', company, '\nX:', Xvector, '\n'

        # label
        yVal = ord(company[0]) - ord('0')

        with open(os.getcwd() + '\data\model\dataset_X-y\\' + company + '.json', "w") as jsonF:
            jsonF.write(json.dumps(Xvector))
        # similarly to read Xvector, Xvector=json.loads('txt_from_json')

        ### 80% contrib
        stat = 'y=' + company
        UIobject.emit(QtCore.SIGNAL('PROGRESS_BAR'), int((float(i) / len(homeList)) * 80))
        UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)

        X.append(Xvector)
        y.append(yVal)


def trainMLmodel(UIobject):
    global X
    global y

    makeDataSet(UIobject)

    ### 20% contrib
    stat = 'Training Model'
    UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)

    DataSetX = np.array(X)
    DataSety = np.array(y)

    # print DataSety
    # print DataSetX

    clf = GaussianNB()
    clf.fit(DataSetX, DataSety)

    clf2 = NearestCentroid()
    clf2.fit(DataSetX, DataSety)

    stat = 'Backing up previous model ...'
    UIobject.emit(QtCore.SIGNAL('PROGRESS_BAR'), 95)
    UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)

    if os.path.exists('data\\model\\naiveBayes.pkl'):
        print 'Old model detected .. Safely archiving it at..'
        print os.getcwd() + "\data\\model\\archive_model\\nb\\model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl'
        os.rename(os.getcwd() + "\data\\model\\naiveBayes.pkl",
                  os.getcwd() + "\data\\model\\archive_model\\nb\\model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl')

    if os.path.exists('data\\model\\nearestCentroid.pkl'):
        # print 'Old model detected .. Safely archiving it at..'
        # print os.getcwd() + "\data\\model\\archive_model\\nc\\model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl'
        os.rename(os.getcwd() + "\data\\model\\nearestCentroid.pkl",
                  os.getcwd() + "\data\\model\\archive_model\\nc\\model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl')

    joblib.dump(clf, 'data\\model\\naiveBayes.pkl')
    joblib.dump(clf2, 'data\\model\\nearestCentroid.pkl')

    print 'Model saved at ', 'data\\model\\naiveBayes.pkl'
    # print 'Model saved at ', 'data\\model\\nearestCentroid.pkl'

    print 'Accuracy of the NB model is: ', clf.score(DataSetX, DataSety)
    # print 'Accuracy of the NC model is: ', clf2.score(DataSetX, DataSety)


    stat = 'Model Trained'
    UIobject.emit(QtCore.SIGNAL('PROGRESS_BAR'), 100)
    UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)


# print DataSety
