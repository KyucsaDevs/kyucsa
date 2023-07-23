from django.shortcuts import render

def index(request):
	title="Home"
	return render(request, 'index.html', {'title': title})

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
	return render(request, 'gallery.html',{'title': title})

def verify(request):
	title="Membership Verification"
	return render(request, 'verify.html', {'title': title})

def membership(request):
	title="SignUp"
	return render(request, 'signup.html', {'title': title})