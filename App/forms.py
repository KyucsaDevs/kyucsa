from django import forms
from datetime import *
from .models import StudentRegistration



#memberVerification form
class memberVerificationForm(forms.Form):
    kyucsaId = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={
            'maxlength': 8, 'placeholder': 'Enter your Kyucsa ID','class': 'form-control rounded'}),label="")
    
    def clean_kyucsaId(self):
        kyucsaId = self.cleaned_data.get('kyucsaId')
        if kyucsaId and (len(str(kyucsaId)) > 8 or not str(kyucsaId).startswith('7')):
            raise forms.ValidationError("")
        return kyucsaId

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ('firstName','lastName','programme','gender','academicStatus','studentNumber','enrollmentYear','email','mobileNumber')
        exclude = ['registeredAt']  #registration Date excluded from display since it is auto calculated.
        widgets = {
                'firstName': forms.TextInput(attrs={'type':'text', 'class':'form-control rounded','placeholder':'first Name'}),
                'lastName': forms.TextInput(attrs={'type':'text', 'class':'form-control rounded','placeholder':'Last Name'}),
                'programme': forms.Select(attrs={'type':'text', 'class':'form-control rounded','placeholder':'Choose ...'}),
                'gender': forms.Select(attrs={'type':'text', 'class':'form-control rounded','placeholder':'Choose ...'}),
                'academicStatus': forms.Select(attrs={'type':'text', 'class':'form-control rounded','placeholder':'Choose ...'}),
                'studentNumber': forms.TextInput(attrs={'type':'text', 'class':'form-control rounded','placeholder':'Student Number'}),
                'enrollmentYear': forms.Select(attrs={'class':'form-control rounded','placeholder':'enrollment Year'}),
                'email': forms.TextInput(attrs={'type':'email', 'class':'form-control rounded','placeholder':'2100800000@std.kyu.ac.ug'}),
                'mobileNumber': forms.TextInput(attrs={'type':'tel', 'class':'form-control rounded','placeholder':'+256 700 700 700'})
            }
        labels = {
            'firstName': 'First Name', 'lastName': 'Last Name',
            'programme': 'Programme', 'gender': 'Gender',
            'academicStatus': 'Academic Status', 'studentNumber': 'Student Number',
            'enrollmentYear': 'Enrollment Year', 'email': 'Email',
            'mobileNumber': 'Mobile Number',
        }

        def clean(self):
            cleaned_data = super().clean()
            firstName = cleaned_data.get('firstName', None)
            lastName = cleaned_data.get('lastName', None)
            programme = cleaned_data.get('programme', None)
            gender = cleaned_data.get('gender', None)
            academicStatus = cleaned_data.get('academicStatus', None)
            studentNumber = cleaned_data.get('studentNumber', None)
            email = cleaned_data.get('email', None)
            mobileNumber = cleaned_data.get('mobileNumber', None)
            registeredAt = cleaned_data.get('registeredAt', date.now())

            # Check if any required field is empty
            required_fields = ['firstName', 'lastName', 'programme', 'gender', 'academicStatus', 'studentNumber', 'enrollmentYear', 'email', 'mobileNumber']
            for field_name in required_fields:
                if not cleaned_data.get(field_name):
                    self.add_error(field_name, 'This field is required.')
            
            if not email.endswith('@gmail.com') and not email.endswith('@std.kyu.ac.ug'):
                self.add_error('email', 'Please enter a valid email address.')
            
            # Check if 'programme' is set to 'Choose'
            if programme == 'Choose':
                self.add_error('programme', 'Please choose a valid option.')

            # Check if 'gender' is set to 'Choose'
            if gender == 'Choose':
                self.add_error('gender', 'Please choose a valid option.')
            
            # Check if 'academicStatus' is set to 'Choose'
            if academicStatus == 'Choose':
                self.add_error('academicStatus', 'Please choose a valid option.')

            return cleaned_data