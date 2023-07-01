from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render())

def gallery(request):
	return render(request,'gallery.html')

def live(request):
	return render(request,'live.html')

def pastevents(request):
	return render(request,'pastevents.html')

def upcomingevents(request):
	return render(request,'upcomingevents.html')

def verify(request):
	return render(request,'verify.html')

def membership(request):
	return render(request,'signup.html')