from django.shortcuts import render
from modules import getInsights
import string

textbox_val = 'Start typing here ...'

def index(request):
	global textbox_val
	data_list = []  # We will insert all the inputs in this array
	if request.method == 'POST':
		#for key in request.POST:
			#print key+' '+request.POST[key]
			#data_list.append(request.POST[key])
		company = request.POST.get('your_name', '')
		if(company!=textbox_val):				
			#data_list.append(company)
			print 'The requested company is '+ company

			res = getInsights(company)

			print 'Successfully obtained results'

			print res

			data_list.append(res)

		if(company==textbox_val):
			print 'Found invalid string for company.. Ignoring this input'
			data_list.append('Enter the company and Hit enter')

			#just before redering the page
		#textbox_val=company #bug fixed

	return render(request, 'forex/inputForm.html', {'content': data_list , 'enter_val': textbox_val})#['contact emfdf', 'fdfa@dsfa.com']})

def contact(request):
	return render(request, 'forex/basic.html', {'content':['contact revanurambareesh', '@github.com']})

def convertToHTML(res):
	return string.replace(res, '\n', '<br />')