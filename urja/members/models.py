from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Member(models.Model):
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	mobile=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	password=models.CharField(max_length=200,blank=True,null=True)
	city=models.CharField(max_length=200)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{} {}".format(self.firstname,self.lastname)

	def get_absolute_url(self):	
		return reverse('members:editmembers',args=[self.id])





