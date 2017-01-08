from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import os

def findSimilarCompanies(xv):
	xList = os.listdir(os.getcwd() + '\data\\model\\dataset_X-y')
	X=[]
	listAns=''

	for xvFile in xList:
		txt=''
		#print os.getcwd() + '\data\model\dataset_X-y\\'+xvFile
		with open(os.getcwd() + '\data\model\dataset_X-y\\'+xvFile, "rb") as jsonF:
			txt=jsonF.read()	

		Xvec=json.loads(txt)
		X.append(Xvec)

	#print np.array([xv])
	arrayDistance = cosine_similarity(np.array([xv]), np.array(X))
	#print arrayDistance
	indexes=arrayDistance[0].argsort()
	
	#print indexes
	#print indexes[-5:]
	
	j=1
	for i in range(4, -1, -1):
		listAns+= '['+str(j)+'] '+processTitleLabel(xList[(indexes[-5:][i])])+'\t'+processTitleName(xList[(indexes[-5:][i])])+'\n'		
		j=j+1

	return listAns


def processTitleLabel(t):
	if t[0]=='1':
		return '(Forex)'
	elif t[0]=='0':
		return '(Non Forex)'

def processTitleName(title):
	return title[2:-5]

