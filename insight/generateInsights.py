import numpy as np
import folderFileInfo
import csv
import os, sys
import json
from sklearn.externals import joblib
from sklearn.naive_bayes import GaussianNB
import nearest_company_pred

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
    
	return Xvector

def createReport(company, numOfResults, Xv):
	result_insight=''
	result_insight+=company
	result_insight+='\n'

	clf = joblib.load('data\\model\\naiveBayes.pkl')
	#likely or not
	ans = clf.predict(np.array([Xv]))
	if ans[0]==0:
		result_insight+='This company is not likely to opt for Forex.\n\n'
	else:
		result_insight+='This company is likely to opt for Forex.\n\n'

	result_insight+='====MODEL Results====\n'

	#chance of about 
	probClass = clf.predict_proba(np.array([Xv]))
	logPrbClass = clf.predict_log_proba(np.array([Xv]))

	result_insight+='Model* predicts that the company has chance of about '+ str((probClass[0][1])/(probClass[0][0]+probClass[0][1])) +' of being Forex\n'
	
	#log prob class1/2
	result_insight+='\nprobability of opting to Forex class is = '+str(probClass[0][1])
	result_insight+='\nprobability of not opting to Forex class is = '+str(probClass[0][0])+'\n'

	result_insight+='\nlog-probability of opting to Forex class is = '+str(logPrbClass[0][1])
	result_insight+='\nlog-probability of not opting to Forex class is = '+str(logPrbClass[0][0])+'\n'

	result_insight+='\n====COMPANY analysis====\n'
	result_insight+='Based on web search and web scarping results, this company is similar to following companies\n(in order of similarity)\n'

	list2comp = nearest_company_pred.findSimilarCompanies(Xv)
	result_insight+='\n'+list2comp+'\n'

	# results 	

	result_insight+='\n====POPULARITY on web====\n'
	#popular?
	if numOfResults>30000:
		result_insight+='This company is popular on Google\n'
	else:
		result_insight+='This company is not very popular on Google\n'
	
	result_insight+='Number of search results Google found **: '+str(numOfResults)+'\n\n\n'


	result_insight+='----FOOTNOTES----\n* As per Naive-Bayes\n** If a company has more than 30,000 results, it is defined \'popular\'\n'
	result_insight+='More popular the company is, more data can be collected to determine its class.\n\n'
	result_insight+='GENERATED BY github.com/revanurambareesh/forexInsights'


	with open(os.getcwd() + '\data\\test_data\\' + company + '\Insights.txt', "w") as insight:
		insight.write(result_insight)

	return result_insight
	#pass

def testCompany(company):	
	#numOfResults = scrapeTestData(company)
	#print 'NUM OF Res= ',numOfResults
	numOfResults=400
	Xv = generateFeatureVector(company)	
	Insights=createReport(company, numOfResults, Xv)
	return Insights

if __name__=='__main__':
	company='COMMISSIONER MCF RICKSHAWS HAL'
	ans=testCompany(company)
	print ans
	#print '=========================\n\n\n\n\n\n'
	#company='COMMISSIONERxcv MCF RICKSHAWS HAL'
	#ans=testCompany(company)
	#print ans
	#print '=========================\n\n\n\n\n'
