import os

def numOfFiles(foldername):
	num=0
	listFiles=os.listdir(os.getcwd() + '\data\\test_data\\'+foldername+'\web')
	for file in listFiles:
		if file!='links.txt':
			if os.path.getsize(os.getcwd() + "/data//test_data\\"+foldername+'\\web\\'+file) > 0:
				num+=1
	return num

def getNonEmptyFiles(foldername):
	nonEmpty=[]
	listFiles=os.listdir(os.getcwd() + '\data\\test_data\\'+foldername+'\web')
	for file in listFiles:
		if file!='links.txt':
			if os.path.getsize(os.getcwd() + "/data//test_data\\"+foldername+'\\web\\'+file) > 0:
				#num+=1
				nonEmpty.append(os.getcwd() + "/data//test_data\\"+foldername+'\\web\\'+file)
	return nonEmpty

if __name__ == "__main__":
	name='1,VIDARBHA INDUSTRIES POWER LIMI'
	print numOfFiles(name)
	filesNames=getNonEmptyFiles(name)
	for files in filesNames:
		print files