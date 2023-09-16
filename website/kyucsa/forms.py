from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    PROGRAM_CHOICES = (
        ('BITC', 'BITC'),
        ('BIS', 'BIS'),
        ('DCS', 'DCS')
    )
    program = forms.ChoiceField(
        choices=PROGRAM_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Study Program'}))
    GENDER_CHOICES = (
        ('', 'Select your gender'),
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Gender'}))
    STATUS_CHOICES = (
        ('', 'Select your program status'),
        ('CONTINUING', 'CONTINUING'),
        ('ALUMNI', 'ALUMNI')
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Program Status'}))
    
    class Meta:
        model = Student
        fields = ['firstName', 'lastName', 'email', 'program', 'enrollment', 'student_no', 'gender', 'status']
        labels = {
                # Set label for first_name to False to hide it
                'firstName': False, 'lastName':False, 'email':False, 'program':False,
                'enrollment':False, 'student_no':False, 'gender':False, 'status':False,
            }
    # Apply Bootstrap classes to the form widgets
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs.update({'class': 'form-control', 'placeholder':'First Name'})
        self.fields['lastName'].widget.attrs.update({'class': 'form-control', 'placeholder':'Last Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':'Email'})
        self.fields['program'].widget.attrs.update({'class': 'form-control', 'placeholder':'Study Program'})
        self.fields['enrollment'].widget.attrs.update({'class': 'form-control', 'placeholder':'Enrollment Year'})
        self.fields['student_no'].widget.attrs.update({'class': 'form-control', 'placeholder':'Student Number'})
