from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Role(models.Model):
	name = models.CharField(max_length=200, null=True)
	def __str__ (self):
		return self.name	

class Student(models.Model):

	COLLEGES = (
		('CAS' , 'College of Arts and Sciences'), 
		('CM', 'College of Medicine'),
		('CD', 'College of Dentistry'),
		('CAMP', 'College of Allied Medical Professions'),
		('CP', 'College of Pharmacy'),
		('CPH', 'College of Public Health')
		)

	user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	college = models.CharField(max_length=200, null=True, choices = COLLEGES)
	role = models.ManyToManyField(Role)
	date_created = models.DateTimeField(auto_now_add = True, null=True)

	#profile_pic = models.ImageField(null = True, blank = True, default ="prof-icon-default.png")

	def __str__ (self):
		return self.name

class Tutor(models.Model):
	COLLEGES = (
		('CAS' , 'College of Arts and Sciences'), 
		('CM', 'College of Medicine'),
		('CD', 'College of Dentistry'),
		('CAMP', 'College of Allied Medical Professions'),
		('CP', 'College of Pharmacy'),
		('CPH', 'College of Public Health')
		)

	CATEGORY = (
		('Student' , 'Student'), 
		('Faculty', 'Faculty'),
		)

	user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	college = models.CharField(max_length=200, null=True, choices = COLLEGES)
	category = models.CharField(max_length = 200, null = True, choices = CATEGORY)
	date_created = models.DateTimeField(auto_now_add = True, null=True)

	def __str__ (self):
		return self.name