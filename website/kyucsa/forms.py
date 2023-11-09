from django import forms
from .models import Student
from django.core.exceptions import ValidationError



#memberVerification form
class memberVerificationForm(forms.Form):
    kyucsaId = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={
            'maxlength': 8, 'placeholder': 'Enter your Kyucsa ID','class': 'form-control rounded'}),label="")
    
    def clean_kyucsaId(self):
        kyucsaId = self.cleaned_data.get('kyucsaId')
        if kyucsaId and (len(str(kyucsaId)) > 8 or not str(kyucsaId).startswith('7')):
            raise forms.ValidationError("")
        return kyucsaId


class KYUEmailField(forms.EmailField):
    def validate(self, value):
        super().validate(value)
        if not value.endswith('@kstd.kyu.ac.ug') or value.endswith('@gmail.com'):
            raise ValidationError('Invalid email address. Please use an email address with the domain @kyu.ac.ug.')

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
    
    email = KYUEmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    
    class Meta:
        model = Student
        fields = ['firstName', 'lastName', 'email', 'programme', 'enrollment', 'std_no', 'gender', 'status']
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
        self.fields['programme'].widget.attrs.update({'class': 'form-control', 'placeholder':'Study Program'})
        self.fields['enrollment'].widget.attrs.update({'class': 'form-control', 'placeholder':'Enrollment Year'})
        self.fields['std_no'].widget.attrs.update({'class': 'form-control', 'placeholder':'Student Number'})
