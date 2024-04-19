from django.db import models
from django.utils import timezone
from datetime import datetime
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User



class KyucsaIdCounter(models.Model):
      last_used_id = models.PositiveIntegerField(default=70000000)


class StudentRegistration(models.Model):
    EYEARS = []
    for r in range(2000, (datetime.datetime.now().year+1)):
      EYEARS.append((r,r))

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

    firstName = models.CharField(max_length=15, blank=False)
    lastName = models.CharField(max_length=15, blank=False)
    kyucsaId = models.CharField(max_length=8, unique=True, blank=True, null=True)
    programme = models.CharField(max_length=15, choices=PROGRAMME, default='Choose', blank=False)
    gender = models.CharField(max_length=10,choices=GENDER, default='Choose', blank=False)
    academicStatus = models.CharField(max_length=20,choices=ACADEMIC_STATUS, default='Choose', blank=False)
    studentNumber = models.IntegerField()
    enrollmentYear = models.IntegerField(choices=EYEARS, default=datetime.datetime.now().year, blank=False)
    email = models.EmailField(max_length=30, blank=False)
    mobileNumber = models.IntegerField(blank=False)
    registeredAt = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
      #Update registration date on every save
      self.registratedAt = timezone.now().date()
      super().save(*args, **kwargs)
    

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {} {}'.format(self.firstName,self.lastName,self.kyucsaId,self.programme,self.gender,self.academicStatus,self.studentNumber,
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
  Pname = models.CharField(max_length=50, null=True)
  Pdesignation = models.CharField(max_length=50, null=True)
  Padvice = models.CharField(max_length=1000, null=True)
  def __str__(self):
    return f"{self.Pname} {self.Pdesignation} {self.Pavater} {self.Padvice}"

#Model for Team
class Team(models.Model):
  tphoto = models.ImageField(upload_to='team/' ,default='team/avatar.png',null=True)
  tname = models.CharField(max_length=100, null=True)
  tpost = models.CharField(max_length=50, null=True)
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