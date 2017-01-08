import numpy as np
import folderFileInfo
import csv
import os, sys
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


def scrapeTestData(query):
	parent_dir_name = os.getcwd()
	sys.path.append(parent_dir_name+'\scraper\googlecse')
	import GoogleTestSearch

	ans = GoogleTestSearch.GoogleWebSearch(query)
	listRes = ans[0]
	numOfResults = ans[1]
	#print listRes[0]
	#os.chdir("..")

	directory = parent_dir_name+'\data\\test_data\\'+query+'\web\\'
	if not os.path.exists(directory):
		os.makedirs(directory)

	file = open(parent_dir_name+'\data\\test_data\\'+query+'\web\links.txt', "w")
	for txtLine in listRes:
		file.write(txtLine)
		file.write('\n')
		#print 'Path changed to ', os.getcwd()
	file.close()

	file = open(parent_dir_name+'\data\\test_data\\'+query+'\\popularity.txt', "w")
	#for txtLine in listRes:
	file.write(numOfResults)
	file.write('\n')
		#print 'Path changed to ', os.getcwd()
	file.close()

	UnivList=[]

	i=1
	print '\n\n Link for: ', company
	
	dataset = 'data\\test_data\\'+company+'\web\links.txt'
	try:
		with open(dataset, 'rb') as f:
			reader = csv.reader(f)
			Url_list = list(reader)

		for obtainedLink in Url_list:
			list2D=[] #links & filepath
			list2D.append(obtainedLink)
			setfilepath = os.getcwd() + '\data\\test_data\\'+company+'\\web\\'+str(i)+'.txt'
			list2D.append(setfilepath)
			#print list2D

			UnivList.append(list2D)
			i=i+1
	except:
		print 'File operation trouble: check if all links.txt files are closed and restart'


	sys.path.append(parent_dir_name+'\scraper\FxInsightScraper\FxInsightScraper\\spiders')
	import WebScraper
	WebScraper.startReactor(UnivList)

	return numOfResults

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

def createReport(company, numOfResults):
	pass

def testCompany(company):	
	numOfResults = scrapeTestData(company)
	print 'NUM OF Res= ',numOfResults
	#generateFeatureVector(company)
	#createReport(company, numOfResults)
	pass

if __name__=='__main__':
	company='COMMISSIONER MCF RICKSHAWS HAL'
	testCompany(company)
	company='COMMISSIONERxcv MCF RICKSHAWS HAL'
	testCompany(company)
	pass