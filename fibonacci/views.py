from django.shortcuts import render
from django.http import HttpResponse
import time


def fibonacci(request):
	return render(request,'fibonacci.html',{'name':'Enter the number'})
def add(request):
	starttime=float(time.time())
	data=int(request.GET["Enter the number"])
	a=1
	b=1
	lst=[]
	lst.append(a)
	lst.append(b)
	count=2
	while count<n:
		c=a+b
		lst.append(c)
		a=b
		b=c
		count+=1
		print(lst)
		f=lst[-1]
		endtime=time.time() - starttime
		d={'n':f,'m':endtime}	
	return render(request,'result.html',{'result':res,'time':endtime})
		

