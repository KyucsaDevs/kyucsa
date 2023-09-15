from django.shortcuts import render
from .models import Partners,Gallery,Patron

def index(request):
	title="Home"
	patrons = Patron.objects.all()
	logos = Partners.objects.all()
	context = {
        'logos': logos,
		'patrons': patrons,
		'title': title
    }
	return render(request, 'index.html', context)

def technologies(request):
	title="Technologies"
	return render(request, 'technologies.html', {'title': title})

def events(request):
	title="Events"
	return render(request, 'events.html', {'title': title})

def team(request):
	title="Team"
	return render(request, 'team.html', {'title': title})

def gallery(request):
	title="Gallery"
	gallery = Gallery.objects.all()
	context = {
        'gallery': gallery,
		'title': title
    }
	return render(request, 'gallery.html',context)

def verify(request):
	title="Membership Verification"
	return render(request, 'verify.html', {'title': title})

def membership(request):
	title="SignUp"
	return render(request, 'signup.html', {'title': title})