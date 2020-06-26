from django import forms
from django.forms import ModelForm
from .models import Member
from django.core.validators import *
import re

class MemberForm(ModelForm):
	class Meta:
		model=Member
		fields=['firstname','lastname','mobile','email','password','city']


	# def clean(self):
	# 	super(MemberForm,self).clean()
	# 	firstname=self.cleaned_data['firstname']
	# 	if 'nikhil' not in firstname:
	# 		raise forms.ValidationError('Enter only string')

	# 	else:	

	# 		return self.cleaned_data	 
			
			



