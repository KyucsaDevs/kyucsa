from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User


class StudentRegistration(models.Model):
    PROGRAMME = (
      ('Choose', 'Choose...'),
      ('BITC', 'BITC'),
      ('BIS', 'BIS'),
      ('BLIS', 'BLIS')
      )
    GENDER = (
      ('Choose', 'Choose...'),
      ('M','Male'),
      ('F','Female')
      )
    ACADEMIC_STATUS =(
      ('Choose', 'Choose...'),
      ('Continuing', 'Continuing'),
      ('Graduated', 'Graduated')
      )
    EYEARS = (
      ('Choose', 'Choose...'),
      ('2023', '2023'),
      ('2023', '2023'),
      ('2023', '2023'),
      ('2023', '2023'),
      ('2023', '2023'),
      ('2023', '2023')
    )
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    programme = models.CharField(max_length=15, choices=PROGRAMME, default='Choose')
    gender = models.CharField(max_length=10,choices=GENDER, default='Choose')
    academicStatus = models.CharField(max_length=20,choices=ACADEMIC_STATUS, default='Choose')
    studentNumber = models.IntegerField()
    enrollmentYear = models.CharField(max_length=10, choices=EYEARS, default='Choose')
    email = models.EmailField(max_length=50)
    mobileNumber = models.IntegerField()
    registeredAt = models.DateField(auto_now=True)

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(self.firstName,self.lastName,self.programme,self.gender,self.academicStatus,self.studentNumber,
                                self.enrollmentYear,self.email,self.mobileNumber,self.registeredAt)


#Model for Partners Logo
class Partner(models.Model):
  pname = models.CharField(max_length=50, unique=True)
  pwebsite = models.CharField(max_length=200, unique=True)
  plogo = models.ImageField(upload_to='partners/', null=True)
  def __str__(self):
    return f"{self.pname} {self.pwebsite} {self.plogo}"

#Model for Gallery
class Gallery(models.Model):
  gimage = models.ImageField(upload_to='gallery/' ,null=True)
  gdescription = models.CharField(max_length=150)
  gyear = models.DateField(null=True)
  def __str__(self):
    return f"{self.gimage} {self.gdescription} {self.gyear}"

#Model for Patron
class Patron(models.Model):
  Pavater = models.ImageField(upload_to='patron/' ,null=True)
  Pname = models.CharField(max_length=100)
  Pdesignation = models.CharField(max_length=300)
  def __str__(self):
    return f"{self.Pavater} {self.Pname} {self.Pdesignation}"

#Model for Team
class Team(models.Model):
  tphoto = models.ImageField(upload_to='team/' ,default='team/avatar.png',null=True)
  tname = models.CharField(max_length=100)
  tpost = models.CharField(max_length=50)
  ttwitter = models.CharField(max_length=20, null=True)
  tgithub = models.CharField(max_length=20, null=True)
  tlinkedin = models.CharField(max_length=20, null=True)
  taccademicyear = models.CharField(max_length=10, unique=True)
  def __str__(self):
    return f"{self.tname} {self.tpost} {self.taccademicyear} {self.tgithub} {self.tlinkedin} {self.ttwitter} {self.tphoto}"

#Model for Events
class Event(models.Model):
  etitle = models.CharField(max_length=200)
  etopic = models.CharField(max_length=100)
  ebanner = models.ImageField(upload_to='events/' ,null=True)
  eslide = models.FileField(upload_to='eslides/' ,null=True)
  estatus = models.CharField(max_length=30)
  eurl = models.URLField(max_length=255)
  edate = models.DateField(default=timezone.now)
  def __str__(self):
    return f"{self.etitle} {self.etopic} {self.estatus} {self.eurl} {self.edate} {self.ebanner} {self.eslide}"

#Model for Events
class Technologies(models.Model):
  tTitle = models.CharField(max_length=200)
  tDescription = models.CharField(max_length=300)
  tPhoto = models.ImageField(upload_to='technologies/' ,null=True)
  tUrl = models.URLField(max_length=255)
  def __str__(self):
    return f"{self.tTitle} {self.tDescription} {self.tPhoto} {self.tUrl}"