import numpy as np
import csv
import json
import os
from methods import folderFileInfo
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
import datetime
import time

X=[]
y=[]

'''
--Usage--

>>> import numpy as np
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
>>> Y = np.array([1, 1, 1, 2, 2, 2])
>>> from sklearn.naive_bayes import GaussianNB
>>> clf = GaussianNB()
>>> clf.fit(X, Y)
GaussianNB(priors=None)
>>> print(clf.predict([[-0.8, -1]]))
[1]
>>> print(clf.predict_log_proba([[0,0],[0,0]]))
[[-0.69314718 -0.69314718]
 [-0.69314718 -0.69314718]]
>>> print(clf.predict_log_proba([[0,0]]))
[[-0.69314718 -0.69314718]]

#### STORING THE MODEL

>>> from sklearn.externals import joblib
>>> joblib.dump(clf, 'C:\Users\Ambareesh\Desktop\filename.pkl')   #For storing the model

>>> clf2 = joblib.load('C:\Users\Ambareesh\Desktop\\filename.pkl') ;
>>> print(clf2.predict_log_proba([[-1,-1]]))
[[ -1.52299839e-08  -1.79999997e+01]]
>>> print(clf2.predict([[-1,-1]]))
[1]

'''

def keywordPresenceTester(company, keyword):
	numOfFiles = folderFileInfo.numOfFiles(company)
	listOfFiles = folderFileInfo.getNonEmptyFiles(company)	
	
	#print company
	#print keyword[0]

	frequency=0
	for scrapedFile in listOfFiles:
		#print scrapedFile
		scrapedData=''
		with open(scrapedFile, 'rb') as f:
			scrapedData=f.read()
		if keyword[0] in scrapedData:
			frequency+=1
	if 10 * frequency >= numOfFiles:
		return True
	else:
		return False

def makeDataSet():
	homeList = os.listdir(os.getcwd() + '\data\\train_data\\')
	keywordFile = 'data\\definitions\\oriList.csv'
	keywordList=[]
	
	with open(keywordFile, 'rb') as f:
				reader = csv.reader(f)
				keywordList = list(reader)

	i=0
	for company in homeList:
		print 'count: ', i
		i+=1	
		#i+=1
		#if i>5:
		#	break

		# X vector for each of the company
		Xvector=[]
		for key in keywordList:
			if keywordPresenceTester(company, key):
				Xvector.append(1)
			else:
				Xvector.append(0)

		print 'y=',company,'\nX:',Xvector, '\n'
		# label
		yVal = ord(company[0])-ord('0')

		with open(os.getcwd()+'\data\model\dataset_X-y\\'+company+'.json', "w") as jsonF:
			jsonF.write(json.dumps(Xvector))
			#similarly to read Xvector, Xvector=json.loads('txt_from_json')

		X.append(Xvector)
		y.append(yVal)

def trainMLmodel():
	makeDataSet()
	DataSetX = np.array(X)
	DataSety = np.array(y)

	clf = GaussianNB()
	clf.fit(DataSetX, DataSety)

	
	if os.path.exists('data\\model\\naiveBayes.pkl'):
		print 'Old model detected .. Safely archiving it at..'
		print os.getcwd() + "\data\\model\\archive_model\\model_"+time.strftime("%Y%m%d%H%M%S")+'.pkl'
		os.rename(os.getcwd() + "\data\\model\\naiveBayes.pkl", os.getcwd() + "\data\\model\\archive_model\\model_"+time.strftime("%Y%m%d%H%M%S")+'.pkl')

	joblib.dump(clf, 'data\\model\\naiveBayes.pkl')
	
	print 'Model saved at ', 'data\\model\\naiveBayes.pkl'

	#print DataSety

if __name__ == '__main__':
	trainMLmodel()	
	print 'DatasetX:',X
	print 'Label:',y