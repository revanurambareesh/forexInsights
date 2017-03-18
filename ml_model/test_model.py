import numpy as np
import scipy.io
import csv
import json
import os

from methods import folderFileInfo

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.externals import joblib
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope
from sklearn.ensemble import IsolationForest

import time

__author__ = 'Ambareesh Revanur (@revanurambareesh)'

X = []
count = 0


def keywordPresenceTester(company, keyword):
    numOfFiles = folderFileInfo.numOfFilesTestSet(company)
    listOfFiles = folderFileInfo.getNonEmptyFilesTestSet(company)

    frequency = 0.0
    for scrapedFile in listOfFiles:
        # scrapedData = ''
        with open(scrapedFile, 'rb') as f:
            scrapedData = f.read()
        if keyword[0] in scrapedData.lower():
            frequency += 1
        if frequency > 5.0: break

    if frequency == 0.0: return -1
    if frequency == 1.0: return -0.5
    if frequency == 2.0: return 0.0
    if frequency > 5.0: return 1

    return (frequency - 3.0) / 2.0


def makeDataSet():
    global X
    global count

    homeList = os.listdir(os.getcwd() + '/forex/data/testset/')
    keywordFile = 'forex/data/definitions/oriList.csv'
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
            Xvector.append(keywordPresenceTester(company, key))

        print 'Feature values generated for ', company[2:], '\n'
        with open(os.getcwd() + '/forex/data/model/testset_X-y/' + company + '.json', "w") as jsonF:
            jsonF.write(json.dumps(Xvector))

        X.append(Xvector)

    count = i


def testMLmodel():
    global X
    global count

    makeDataSet()

    stat = 'Testing Model'

    DataSetX = np.array(X)
    scipy.io.savemat('forex/data/model/testset_X-y/Xy.mat', dict(X=DataSetX))

    stat = 'Backing up previous model ...'
    clfSVMgm = joblib.load('forex/data/model/oneClassSVM.pkl')

    num=0
    predictions = clfSVMgm.predict(DataSetX)
    for i in predictions:
        if i == 1.0:
            num+=1

    print 'Rightly predicted: ', num
    print 'Test Accuracy of the model: ', (1.0 * num) / count
    stat = 'Model Tested'

if __name__ == '__main__':
    testMLmodel()
