from django.db import models

from members.models import Member
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.


class PaymentDetail(models.Model):
	member=models.ForeignKey(Member,on_delete=models.CASCADE,related_name='paymentdetails')
	amount=models.DecimalField(max_digits=6,decimal_places=2,default='00.00')
	paymonth=models.DateField(default=timezone.now())
	paycreated=models.DateTimeField(auto_now=True)
	addedBy=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,default=True)



