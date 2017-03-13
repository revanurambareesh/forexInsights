from rake import rake
import operator
import csv
import re
from sys import argv

__author__ = 'revanurambareesh'

def rakeUP():
	
	outputFile = 'oriList.csv'
	inputFile = 'ScrapedData.txt'

	rake_object = rake.Rake("rake/SmartStoplist.txt", 5, 1, 3)
	sample_file = open(inputFile, 'r')
	text = sample_file.read()
	keywords = rake_object.run(text)
	target = open(outputFile, 'w')
	for i in range(0, len(keywords)):
		#print keywords[i][0]
		target.write(re.sub('[^a-zA-Z]+', '', keywords[i][0]))
		target.write('\n')
	print 'written output to ', outputFile

if __name__ == '__main__':
  rakeUP()
