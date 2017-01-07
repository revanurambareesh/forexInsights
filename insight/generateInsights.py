import numpy as np
import folderFileInfo
import csv
import os
import json

def keywordPresenceTester(company, keyword):
    numOfFiles = folderFileInfo.numOfFiles(company)
    listOfFiles = folderFileInfo.getNonEmptyFiles(company)

    # print company
    # print keyword[0]

    frequency = 0
    for scrapedFile in listOfFiles:
        # print scrapedFile
        scrapedData = ''
        with open(scrapedFile, 'rb') as f:
            scrapedData = f.read()
        if keyword[0] in scrapedData:
            frequency += 1
    if 10 * frequency >= numOfFiles:
        return True
    else:
        return False


def scrapeTestData(company):
	pass

def generateFeatureVector(company):
	keywordFile = 'data\\definitions\\oriList.csv'
	keywordList = []

	with open(keywordFile, 'rb') as f:
	    reader = csv.reader(f)
	    keywordList = list(reader)

	i = 0

	Xvector = []
	for key in keywordList:
	    if keywordPresenceTester(company, key):
	        Xvector.append(1)
	    else:
	        Xvector.append(0)
	
	#print 'y=', company, '\nX:', Xvector, '\n'
	
	# label
	
	#yVal = ord(company[0]) - ord('0')

	with open(os.getcwd() + '\data\\test_data\\' + company + '\Xv.json', "w") as jsonF:
		jsonF.write(json.dumps(Xvector))
    # similarly to read Xvector, Xvector=json.loads('txt_from_jso
    ### 80% contrib
    #stat = 'y='+ company
    #UIobject.emit(QtCore.SIGNAL('PROGRESS_BAR'), int((float(i) / len(homeList)) * 80))
    #UIobject.emit(QtCore.SIGNAL('STATUS_LINE'), stat)
	pass

def testCompany(company):	
	#numOfResults = scrapeTestData(company)
	generateFeatureVector(company)
	#createReport(company, numOfResults)
	pass

if __name__=='__main__':
	company='COMMISSIONER MCF RICKSHAWS HAL'
	testCompany(company)
