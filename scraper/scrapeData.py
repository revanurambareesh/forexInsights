import os
import sys


def storeResTxt(query, label):

	parent_dir_name = os.getcwd()
	sys.path.append(parent_dir_name+'\scraper\googlecse')
	import GoogleSearch

	listRes = GoogleSearch.GoogleWebSearch(query)
	#print listRes[0]
	#os.chdir("..")

	directory = parent_dir_name+'\data\\train_data\\'+str(label)+','+query
	if not os.path.exists(directory):
		os.makedirs(directory)

	file = open(parent_dir_name+'\data\\train_data\\'+str(label)+','+query+'\links.txt', "w")
	for txtLine in listRes:
		file.write(txtLine)
		file.write('\n')
		#print 'Path changed to ', os.getcwd()
	file.close()

	return listRes

#def getDataToTXT(Name, label, UrlList=None):
#	parent_dir_name = os.getcwd()
#	#sys.path.append(parent_dir_name+'\scraper\spider')
#	from FxSpider.FxSpider.spiders import WebScraper
#
#	#file = open(fileName, "w")
#	#file.close()
#
#	i=1
#
#	for urlLink in UrlList:
#		import runSpider as r
#		fileName = parent_dir_name + '\data\\train_data\\' + str(label) + ',' + Name + '\\' + str(i)+'.txt'
#		r.startProcess(urlLink, fileName)
#		del sys.modules['r']
#		i=i+1
#	#file.close()
#
#	#for txtLine in UrlList:
#	#	file = open(parent_dir_name+'\data\\train_data\\'+str(label)+','+query+'\\'+i+'.txt', "w")
#	#	i=i+1

if __name__ == '__main__':
  	urlList = storeResTxt('sample', -99)
  	#getDataToTXT('sample', -99, urlList)
