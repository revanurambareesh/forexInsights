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

import datetime
import time

__author__ = 'Ambareesh Revanur (@revanurambareesh)'

X = []
y = []


def keywordPresenceTester(company, keyword):
    numOfFiles = folderFileInfo.numOfFiles(company)
    listOfFiles = folderFileInfo.getNonEmptyFiles(company)

    frequency = 0.0
    for scrapedFile in listOfFiles:
        scrapedData = ''
        with open(scrapedFile, 'rb') as f:
            scrapedData = f.read()
        if keyword[0] in scrapedData:
            frequency += 1

    #if numOfFiles == 0:
    #	print 'File does not seem to exist...', company

    #if 15 * frequency >= numOfFiles:
    #    return True
    #else:
    #    return False

    if frequency < 2.0: return (1.0-3.0)/2.0
    if frequency > 5.0: return (5.0-3.0)/2.0

    return (frequency-3.0)/2.0


def makeDataSet():#UIobject):
    global X
    global y

    homeList = os.listdir(os.getcwd() + '/forex/data/train_data/')
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
            #if keywordPresenceTester(company, key) == True:
            #	#print 'hi'
            #    Xvector.append(1)
            #else:
            #    Xvector.append(0)
            Xvector.append(keywordPresenceTester(company, key))

        print 'y=', company, '\nX:', Xvector, '\n'

        # label
        yVal = ord(company[0]) - ord('0')
        #if yVal == 0: yVal=-1

        with open(os.getcwd() + '/forex/data/model/dataset_X-y/' + company + '.json', "w") as jsonF:
            jsonF.write(json.dumps(Xvector))
        # similarly to read Xvector, Xvector=json.loads('txt_from_json')

        ### 80% contrib
        stat = 'y=' + company
        #UIobject.emit(QtCore.SIGNAL('PROGRESS_BAR'), int((float(i) / len(homeList)) * 80))
        #UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)

        X.append(Xvector)
        y.append(yVal)


def trainMLmodel():#UIobject):
    global X
    global y

    print 'HIHI'
    #sleep(4)

    makeDataSet()#UIobject)

    ### 20% contrib
    stat = 'Training Model'
    #UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)

    DataSetX = np.array(X)
    DataSety = np.array(y)

    #print DataSety
    #print DataSetX

    scipy.io.savemat('forex/data/model/dataset_X-y/Xy.mat', dict(x=DataSetX, y=DataSety))



    stat = 'Backing up previous model ...'
    #UIobject.emit(QtCore.SIGNAL('PROGRESS_BAR'), 95)
    #UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)

    '''
    clf = BernoulliNB()
    clf.fit(DataSetX, DataSety)

    if os.path.exists('forex/data/model/naiveBayes.pkl'):
        print 'Old model detected .. Safely archiving it at..'
        print os.getcwd() + "/forex/data/model/archive_model/nb/model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl'
        os.rename(os.getcwd() + "/forex/data/model/naiveBayes.pkl",
                  os.getcwd() + "/forex/data/model/archive_model/nb/model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl')

    print 'Accuracy of the NB model is: ', clf.score(DataSetX, DataSety)

    joblib.dump(clf, 'forex/data/model/naiveBayes.pkl')

    clf2 = NearestCentroid()
    clf2.fit(DataSetX, DataSety)        

    if os.path.exists('forex/data/model/nearestCentroid.pkl'):
        # print 'Old model detected .. Safely archiving it at..'
        # print os.getcwd() + "\data\\model\\archive_model\\nc\\model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl'
        os.rename(os.getcwd() + "/forex/data/model/nearestCentroid.pkl",
                  os.getcwd() + "/forex/data/model/archive_model/nc/model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl')

    print 'Accuracy of the NC model is: ', clf2.score(DataSetX, DataSety)    
'''
    clfSVMgm = OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
    clfSVMgm.fit(DataSetX)#, DataSety) 

    if os.path.exists('forex/data/model/oneClassSVM.pkl'):
    	os.rename(os.getcwd() + "/forex/data/model/oneClassSVM.pkl",
                  os.getcwd() + "/forex/data/model/archive_model/svm1/model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl')

    joblib.dump(clfSVMgm, 'forex/data/model/oneClassSVM.pkl')

    clfSVMgm = joblib.load('forex/data/model/oneClassSVM.pkl')
    print clfSVMgm.predict(DataSetX)
    
    print '1 predict 499:', clfSVMgm.predict([DataSetX[499]])
    print '-1 predict 496:', clfSVMgm.predict([DataSetX[496]])
    print '1 predict 497:', clfSVMgm.predict([DataSetX[497]])

    #clfElEgm = EllipticEnvelope()
    #clfElEgm.fit(DataSetX, DataSety)

    #if os.path.exists('forex/data/model/Elliptic.pkl'):
    ## print 'Old model detected .. Safely archiving it at..'
    ## print os.getcwd() + "\data\\model\\archive_model\\nc\\model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl'
    #	os.rename(os.getcwd() + "/forex/data/model/Elliptic.pkl",
    #          os.getcwd() + "/forex/data/model/archive_model/ellip/model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl')

    #joblib.dump(clfElEgm, 'forex/data/model/Elliptic.pkl')
    '''
    clfIsoForestgm = IsolationForest()
    clfIsoForestgm.fit(DataSetX)#, DataSety)

    if os.path.exists('forex/data/model/Isolation.pkl'):
    # print 'Old model detected .. Safely archiving it at..'
    # print os.getcwd() + "\data\\model\\archive_model\\nc\\model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl'
    	os.rename(os.getcwd() + "/forex/data/model/Isolation.pkl",
              os.getcwd() + "/forex/data/model/archive_model/isol/model_" + time.strftime("%Y%m%d%H%M%S") + '.pkl')

    joblib.dump(clfIsoForestgm, 'forex/data/model/Isolation.pkl')

    print 'Model saved at ', 'forex/data/model/naiveBayes.pkl'
    # print 'Model saved at ', 'data\\model\\nearestCentroid.pkl'
    '''

    #print 'Accuracy of the SVM model is: ', clfSVMgm.score(DataSetX, DataSety)

    #print 'Accuracy of the EE model is: ', clfElEgm.score(DataSetX, DataSety)

    #print 'Accuracy of the Iso_forest model is: ', clfIsoForestgm.score(DataSetX, DataSety)

    stat = 'Model Trained'
    #UIobject.emit(QtCore.SIGNAL('PROGRESS_BAR'), 100)
    #UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)


if __name__ == '__main__':
	trainMLmodel()