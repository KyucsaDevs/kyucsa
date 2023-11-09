from django.db import models
from django.utils import timezone
from datetime import datetime
#Student Modals
class Student(models.Model):
    kyucsa_id = models.CharField(max_length=10, unique=True)
    std_no = models.CharField(max_length=15, unique=True)
    firstName = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    programme = models.CharField(max_length=30)
    enrollment = models.DateField(max_length=30)
    gender = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.firstName + " " + self.lastName


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

#Model for Members
class Member(models.Model):
  etitle = models.CharField(max_length=200)
  etopic = models.CharField(max_length=100)
  ebanner = models.ImageField(upload_to='events/' ,null=True)
  estatus = models.CharField(max_length=30)
  eurl = models.URLField(max_length=255)
  edate = models.DateField(default=timezone.now)
  def __str__(self):
    return f"{self.etitle} {self.etopic} {self.estatus} {self.eurl} {self.edate} {self.ebanner}"