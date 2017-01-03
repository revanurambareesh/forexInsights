import os
import csv

UnivList=[]

def makeListScrape():
	Url_list=[]
	print 'creating the scraper links'
	homeList = os.listdir(os.getcwd() + '\data\\train_data\\')
	for company in homeList:
		i=1
		print '\n\n Link for: ', company
		dataset = 'data\\train_data\\'+company+'\links.txt'
		try:
			with open(dataset, 'rb') as f:
				reader = csv.reader(f)
				Url_list = list(reader)

			for obtainedLink in Url_list:
				list2D=[] #links & filepath
				list2D.append(obtainedLink)
				setfilepath = os.getcwd() + '\data\\train_data\\'+company+'\\'+str(i)+'.txt'

				list2D.append(setfilepath)
				#print list2D
				UnivList.append(list2D)
				i=i+1
		except:
			print 'File operation trouble: check if all links.txt files are closed and restart'

	return UnivList

if __name__ == '__main__':
	uL = makeListScrape()
	for list2D in uL:
		#for comp in list2D:
		#	print comp,' '
		print list2D[0][0]+'\n'+list2D[1]
		print '\n'