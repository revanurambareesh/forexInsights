from django.shortcuts import render
from modules import getInsights
import string
import time
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import csv

textbox_val = 'Start typing here ...'


def index(request):
    global textbox_val
    data_list = []
    # print request.FILES

    if request.method == 'POST' and bool(request.FILES) and request.FILES['file']:
        print 'Successfully obtained the file...'
        myfile = request.FILES['file']
        reader = normalize_newlines(myfile.read()).split('\n')
        res = ''
        for row in reader:
            print row
            if row == '': continue
            res += getInsights(row) + '\n'
            print 'Successfully obtained results'
            print res
        data_list.append(res)

    elif request.method == 'POST':
        company = request.POST.get('your_name', '')
        if company != textbox_val and company != '':
            print 'The requested company is ' + company
            res = getInsights(company)
            print 'Successfully obtained results'
            print res
            data_list.append(res)

    return render(request, 'forex/inputForm.html',
                  {'content': data_list, 'enter_val': textbox_val})


def contact(request):
    return render(request, 'forex/basic.html', {'content': ['contact revanurambareesh', '@github.com']})


def convertToHTML(res):
    return string.replace(res, '\n', '<br />')


def normalize_newlines(string):
    import re
    return re.sub(r'(\r\n|\r|\n)', '\n', string)
