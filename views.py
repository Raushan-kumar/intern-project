from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponse
import MySQLdb
from django import forms
from django.db import models
from models import *
# Create your views here.
def search(request):
	return render(request, 'UI.html',)
def contact(request):
	#return render(request, 'htmlform.html',)
	errors = []

	parm1=request.POST.get('field_name');
	parm2=request.POST.get('type');
	parm3=request.POST.get('mul');
	parm4=request.POST.get('norm');
	#parm5=request.POST.get('');
	#p1="sucessfully inserted";
	if request.method == 'POST':
		if not request.POST.get('field_name', ''):
            		errors.append('Enter a field_name.')
        	if not request.POST.get('type', ''):
            		errors.append('Enter a type.')
        	if not request.POST.get('mul', ''):
            		errors.append('Enter a mul.')
        	if not request.POST.get('norm', ''):
            		errors.append('Enter a norm.')
		
		db = MySQLdb.connect(user='root',db='DYNAMICFIELD', passwd='pass', host='localhost')
		cursor = db.cursor();


	#cursor.execute(sql)
        #cursor.execute("INSERT INTO books_book(id,title, publisher_id, publication_date) VALUES("%d","%s","%d","%s")"%   
        #(8,"python",897,'2012-09-04'));
		
       		#sql= "INSERT INTO DYNAMIC(field_name,type, mul,norm)VALUES(%s,%s,%s,%s)"
        	#cursor.execute(sql, [parm1, parm2,parm3,parm4])
		obj = Dynamic(field_name=parm1, type = parm2,mul=parm3,norm=parm4,customer="staples")
		obj.save()
		db.commit()
        	db.close()
        #return render(request, 'results.html',
                #{'p1':p1 })
	     
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      
