"""
Simple command-line example for Custom Search.
Command-line application that does a search.
"""

__author__ = 'jcgregorio@google.com (Joe Gregorio)', '(&modified for usage)'

import pprint
import json
from sys import argv

from googleapiclient.discovery import build
from array import array

def GoogleWebSearch(queryData):
  QueryString = queryData
  outputLinkTxt = 'links.csv'
  service = build("customsearch", "v1", developerKey="AIzaSyBf3JuAb7zOEOele41pNZec2mHo5LL3iRY")

  res = service.cse().list(
      	q=QueryString,
    	cx='005502126501928785104:rbsuxqik2xy',
     ).execute()
  	
  	#pprint.pprint(res)
  print json.dumps(res, sort_keys=True, indent=4)
  print '\n=================END OF WEB SEARCH===================\n\n\n'
  resNum = res['searchInformation']['totalResults']
  if(float(resNum).is_integer):
  	count = int(resNum)
  else:
  	count = 15
  if count > 10:
  	count = 10
  print 'No. of results found: ', resNum
  print 'No. of results being parsed: ', count
  print '\n\nURLs:\n '
  listRes = []
  for i in range(0, count):
    #intarray = array(res['items'][i]['link'])
    listRes.append(res['items'][i]['link'])
    print res['items'][i]['link']
  return listRes

if __name__ == '__main__':
  GoogleWebSearch('RAMA')
