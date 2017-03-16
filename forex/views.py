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
    data_list = []  # We will insert all the inputs in this array

    print 'Here hi'
    print request.FILES


    if request.method == 'POST' and bool(request.FILES) and request.FILES['file']:
        print 'Successfully obtained the files...'
        myfile = request.FILES['file']
        #	fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # print 'file name as it stored is: ', filename
        # print 'printing the file as it is: ', myfile.name
        # print 'file received was: ', myfile.name
        # print 'File content received that: ', myfile.read()

        reader = normalize_newlines(myfile.read()).split('\n')  # csv.reader(csvfile, delimiter=' ', quotechar='|')

        res = ''
        for row in reader:
            print row, 'dfs'

            if row == '': continue

            #res += getInsights(row) + '\n'
            res += 'HIHI'
            time.sleep(1)

            print 'Successfully obtained results'

            print res

        data_list.append(res)
        '''for i in range(0,100)
			print 'The requested company is '+ company

				res = getInsights(company)

				print 'Successfully obtained results'

				print res

				data_list.append(res)'''

    # uploaded_file_url = fs.url(filename)
    # return render(request, 'forex/inputForm.html', {'uploaded_file_url': uploaded_file_myfileurl})

    elif request.method == 'POST':
        # for key in request.POST:
        # print key+' '+request.POST[key]
        # data_list.append(request.POST[key])
        # print 'unexpectedly here... ' #???
        # return render(request, 'forex/inputForm.html', {'content': data_list , 'enter_val': textbox_val})#['contact emfdf', 'fdfa@dsfa.com']})
        company = request.POST.get('your_name', '')
        if company != textbox_val and company != '':
            # data_list.append(company)
            print 'The requested company is ' + company

            #res = getInsights(company)
            res='HIHI'
            time.sleep(3)

            print 'Successfully obtained results'

            print res

            data_list.append(res)

        # if(company==textbox_val):
        #	print 'Found invalid string for company.. Ignoring this input'
        #	data_list.append('Enter the company and Hit enter')

        # just before redering the page
        # textbox_val=company #bug fixed

    return render(request, 'forex/inputForm.html',
                  {'content': data_list, 'enter_val': textbox_val})  # ['contact emfdf', 'fdfa@dsfa.com']})


def contact(request):
    return render(request, 'forex/basic.html', {'content': ['contact revanurambareesh', '@github.com']})


def convertToHTML(res):
    return string.replace(res, '\n', '<br />')


def normalize_newlines(string):
    import re
    return re.sub(r'(\r\n|\r|\n)', '\n', string)
