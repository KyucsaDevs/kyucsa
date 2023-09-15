from django.db import models
from django.utils import timezone
from datetime import datetime
#Model for Partners Logo
class Partners(models.Model):
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
  tprofilepicture = models.ImageField(upload_to='team/' ,null=True)
  tfullname = models.CharField(max_length=100)
  tposition = models.CharField(max_length=50)
  tlinkedin = models.CharField(max_length=20)
  ttwitter = models.CharField(max_length=20)
  tgithub = models.CharField(max_length=20)
  taccademicyear = models.CharField(max_length=10, unique=True)
  def __str__(self):
    return f"{self.tfullname} {self.tposition} {self.taccademicyear} {self.tgithub} {self.tlinkedin} {self.ttwitter} {self.tprofilepicture}"

#Model for Events
class Events(models.Model):
  etitle = models.CharField(max_length=200)
  etopic = models.CharField(max_length=100)
  ebanner = models.ImageField(upload_to='events/' ,null=True)
  estatus = models.CharField(max_length=30)
  eurl = models.URLField(max_length=255)
  edate = models.DateField(default=timezone.now)
  def __str__(self):
    return f"{self.etitle} {self.etopic} {self.estatus} {self.eurl} {self.edate} {self.ebanner}"

#Model for Members
class Members(models.Model):
  etitle = models.CharField(max_length=200)
  etopic = models.CharField(max_length=100)
  ebanner = models.ImageField(upload_to='events/' ,null=True)
  estatus = models.CharField(max_length=30)
  eurl = models.URLField(max_length=255)
  edate = models.DateField(default=timezone.now)
  def __str__(self):
    return f"{self.etitle} {self.etopic} {self.estatus} {self.eurl} {self.edate} {self.ebanner}"