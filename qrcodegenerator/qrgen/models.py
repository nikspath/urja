from django.db import models

# Create your models here.


class QrcodeData(models.Model):
	labelname=models.CharField(max_length=200)
	description=models.TextField()
	qrimg=models.CharField(max_length=200)
	createdate=models.DateTimeField(auto_now_add=True)