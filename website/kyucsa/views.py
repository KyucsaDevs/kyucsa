from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render())

def technologies(request):
	template = loader.get_template('technologies.html')
	return HttpResponse(template.render())

def workshops(request):
	template = loader.get_template('workshops.html')
	return HttpResponse(template.render())

def team(request):
	template = loader.get_template('team.html')
	return HttpResponse(template.render())

def gallery(request):
	template = loader.get_template('gallery.html')
	return HttpResponse(template.render())

def live_events(request):
	template = loader.get_template('live.html')
	return HttpResponse(template.render())

def upcomingevents(request):
	template = loader.get_template('upcomingevents.html')
	return HttpResponse(template.render())

def pastevents(request):
	template = loader.get_template('pastevents.html')
	return HttpResponse(template.render())

def verify(request):
	template = loader.get_template('verify.html')
	return HttpResponse(template.render())

def membership(request):
	template = loader.get_template('signup.html')
	return HttpResponse(template.render())