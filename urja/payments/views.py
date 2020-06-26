from django.shortcuts import render

# Create your views here.
from members.models import Member
from .models import PaymentDetail


def paymentreport(request):
	pd=PaymentDetail.objects.all()
	return render(request,'payments/paymentreport.html',{'pd':pd})
