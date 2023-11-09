import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import StudentRegistrationForm, memberVerificationForm
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
                student = Student.objects.get(kyucsa_id=kyucsaId)
                messages.success(request, f"You are a registered member with ID: {kyucsaId}")
                return render(request, 'success.html', {'student': student})  # Render a success template with student data
            except Student.DoesNotExist:
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
            # Cleaned form data
            cleaned_data = form.cleaned_data
            firstName = cleaned_data["firstName"]
            lastName = cleaned_data["lastName"]
            programme = cleaned_data["programme"]
            gender = cleaned_data["gendersel"]
            status = cleaned_data["status"]
            std_no = cleaned_data["std_no"]
            enrollment = cleaned_data["enrollment"]
            email = cleaned_data["email"]

            # Validate email domain
            if not email.endswith('@gmail.com') and not email.endswith('@std.kyu.ac.ug'):
                messages.error(request, "Invalid email domain. Allowed domains: @gmail.com, @std.kyu.ac.ug")
                return redirect('membership')

            # Generate kyucsaId starting with 7 and with 8 digits
            kyucsaId = random.randint(70000000, 79999999)

            # Check if the record already exists in the database
            if Student.objects.filter(kyucsa_id=kyucsaId).exists():
                messages.warning(request, "Kyucsa ID already exists. Please try again.")
                return redirect('membership')

            # Create and save the Student record
            data = Student(
                kyucsa_id=kyucsaId,
                firstName=firstName,
                lastName=lastName,
                email=email,
                std_no=std_no,
                gendersel=gender,
                enrollment=enrollment,
                status=status,
                programme=programme
            )

            try:
                data.save()
                messages.success(request, "Registered successfully!")
                return redirect('index')
            except Exception as e:
                messages.error(request, f"Oops, Something happened: {str(e)}. Try again later ...")
                return redirect('membership')

        else:
            # Form data is not valid, return error messages
            error_messages = form.errors.as_json()
            response_data = {'error_messages': error_messages}
            return JsonResponse(response_data, status=400)  # Set status code to 400 for bad request

    context = {
        'form': form,
        'title': title
    }
    return render(request, 'signup.html', context)