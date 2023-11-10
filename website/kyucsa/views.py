import random,zoneinfo
from datetime import datetime, timezone, date
from django.utils import timezone
from django.utils.timezone import now
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import StudentRegistrationForm, memberVerificationForm
from .models import Partner,Gallery,Patron,Event,Team,KyucsaIdCounter,StudentRegistration,Technologies
from django.contrib import messages
from .signals import generateKyucsaId, sendKyucsaIdEmail





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
    technologies = Technologies.objects.all()
    context = {
          'title':title,
          'technologies':technologies
    }
    return render(request, 'technologies.html', context)

def events(request):
    title="Events"
    events = Event.objects.all()
    current_date = timezone.now().date()
    tzname = request.session.get("django_timezone")
    if tzname:
        timezone.activate(zoneinfo.ZoneInfo(tzname))
    for event_date in events:
        if event_date.edate < current_date:
            event_date.estatus = "past"
        elif event_date.edate == current_date:
            event_date.estatus = "live"
        else:
            event_date.estatus = "upcoming"
    context = {
        'events': events,
		'title': title,
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
    title = "Membership Verification"
    form = memberVerificationForm(request.POST or None)  # Initialize the form with request data

    if request.method == "POST":
        if form.is_valid():
            kyucsaId = form.cleaned_data['kyucsaId']
            try:
                # Try to retrieve a student with the given kyucsaId
                student = StudentRegistration.objects.filter(kyucsaId=kyucsaId).first()
                if student:
                    messages.success(request, f"You are a registered member with ID: {kyucsaId}")
            except StudentRegistration.DoesNotExist:
                # Student with the given kyucsaId does not exist
                messages.warning(request, f"ID {kyucsaId} Not Found...")
        else:
            # Form is not valid
            messages.info(request, "Kyucsa ID must start with 7 and it is 8 digits.")

    context = {
        'title': title,
        'form': form
    }
    return render(request, 'verify.html', context)


def membership(request):
    title = "SignUp"
    form = StudentRegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
             firstName = form.cleaned_data['firstName']
             lastName = form.cleaned_data['lastName']
             studentNumber = form.cleaned_data['studentNumber']
             email = form.cleaned_data['email']

             student_data = StudentRegistration.objects.filter(firstName=firstName,lastName=lastName,
                  studentNumber=studentNumber,email=email).first()
             
             if student_data is None:
                student = form.save(commit=False)
                student.kyucsaId = generateKyucsaId()
                student.save()
                sendKyucsaIdEmail(student.email, student.kyucsaId)
                messages.success(request, f'Registration successful! Kyucsa ID {student.kyucsaId} sent to your email.')
                return redirect('signup')
             elif StudentRegistration.objects.filter(studentNumber=studentNumber).first():
                  messages.warning(request, 'A student with that student number exist.')
             elif StudentRegistration.objects.filter(email=email).first():
                  messages.warning(request, 'A student with that email exist.')
             else:
                  messages.warning(request, 'Ooops, Something When Wrong. Try again.')

    else:
        form = StudentRegistrationForm()
    context = {
        'form': form,
        'title': title
    }
    return render(request, 'signup.html', context)