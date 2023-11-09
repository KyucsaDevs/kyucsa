import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import StudentRegistrationForm
from .models import Partner,Gallery,Patron,Event,Team,Student
from django.contrib import messages

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
	form = StudentRegistrationForm(request.POST or None)
	context = {
        'form': form,
		'title': title
    }
	if request.method == "POST":
		if form.is_valid():
			firstName = form.cleaned_data["firstName"]
			lastName = form.cleaned_data["lastName"]
			programme = form.cleaned_data["programme"]
			gender = form.cleaned_data["gendersel"]
			status = form.cleaned_data["status"]
			std_no = form.cleaned_data["std_no"]
			enrollment = form.cleaned_data["enrollment"]
			email = form.cleaned_data["email"]
			kyucsaId = f'kyucsa{random.randint(10000000, 99999999)}'
            # Perform actions with validated data (e.g., save to database)
			if firstName!="" and lastName!="" and programme!="" and gender!="" and status!="" and std_no!="" and enrollment!="" and email!="" and kyucsaId!="":
				data = Student(kyucsa_id=kyucsaId, firstName=firstName, lastName=lastName,email=email,std_no=std_no,
					gendersel=gender, enrollment=enrollment,status=status, programme=programme)
				data.save()
				# Return a JSON response indicating success with the generated random number
				messages.success(request, "Registered successfully!")
				return redirect('index')
			else:
				# Return a JSON response indicating success with the generated random number
				messages.error(request, "Registeration failed!")
				return redirect('membership')
		else:
			# Form data is not valid, return error messages
			error_messages = form.errors.as_json()
			response_data = {'error_messages': error_messages}
			return JsonResponse(response_data, status=400)  # Set status code to 400 for bad request
	return render(request, 'signup.html', context)