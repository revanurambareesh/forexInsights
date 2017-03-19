########### Python 2.7 #############
import httplib, urllib, base64
import json
import csv
import os
import sys
import time

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '39d793418fd0402b80fe06ff463762be',
}

params = urllib.urlencode({
    # Request parameters
    'q': 'A K ENTERPRISES',
    'count': '40',
    'offset': '0',
    'mkt': 'en-us',
    'safesearch': 'Moderate',
})


def fun():
    dataset = 'data/dataset_axis.csv'
    conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
    parent_dir_name = os.getcwd()
    label = 0

    with open(dataset, 'rb') as f:
        reader = csv.reader(f)
        Data_list = list(reader)

    for i in range(14069, 15069):
        if i % 5 == 0: time.sleep(1)

        query = Data_list[i][1]
        print query
        params = urllib.urlencode({
            # Request parameters
            'q': query,
            'count': '40',
            'offset': '0',
            'mkt': 'en-us',
            'safesearch': 'Moderate',
        })

        conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        d = json.loads(data)
        listRes = []
        oldwords=query.split(" ")
        words=[]
        for word in oldwords:
            word=''.join(e for e in (word[:4]).lower() if e.isalnum())
            print word
            words.append(word)

        for j in range(0, 40):
            try:
                weblink = d["webPages"]["value"][j]["displayUrl"]
                if all(ext in weblink for ext in words) and weblink.find("...") == -1:
                    listRes.append(d["webPages"]["value"][j]["displayUrl"])
                print weblink
            except Exception as e:
                # print("[Errno {0}] {1}".format(e.errno, e.strerror))
                print 'error', e

        if len(listRes) == 0: continue

        directory = parent_dir_name + '/data/train_data/' + str(label) + ',' + query
        if not os.path.exists(directory):
            os.makedirs(directory)

        file = open(parent_dir_name + '/data/train_data/' + str(label) + ',' + query + '/links.txt', "w")
        for txtLine in listRes:
            try:
                file.write(txtLine)
                file.write('\n')
            except Exception as e:
                print 'error in writing to file'

        file.close()

        print '==================================='
        print '==================================='
        print '==================================='

    conn.close()


if __name__ == '__main__':
    fun()
