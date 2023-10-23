from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import StudentRegistrationForm
from .models import Partner,Gallery,Patron,Event,Team

def index(request):
	title="Home"
	patrons = Patron.objects.all()
	logos = Partner.objects.all()
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
	events = Event.objects.all()
	context = {
        'events': events,
		'title': title
    }
	return render(request, 'events.html', context)

def team(request):
	title="Team"
	teams = Team.objects.all()
	context = {
        'teams': teams,
		'title': title
    }
	return render(request, 'team.html', context)

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
	form = StudentRegistrationForm(request.POST)
	context = {
        'form': form,
		'title': title
    }
	def student_registration_view(request):
		if request.method == 'POST':
			form = StudentRegistrationForm(request.POST)
			if form.is_valid():
				student = form.save()
				# Send registration ID via email
				send_registration_email(student.registration_id, student.email)
				return redirect('success')  # Replace 'success' with your success page URL
		else:
			form = StudentRegistrationForm()
	return render(request, 'signup.html', context)