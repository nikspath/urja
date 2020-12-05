from django.shortcuts import render,redirect
from django.http import HttpResponse
import qrcode
from .models import QrcodeData
from .forms import QrcodeDataForm

# Create your views here.



def create(request):

	fm=QrcodeDataForm()
	if request.method == 'POST':
		fm=QrcodeDataForm(request.POST or None)
		if fm.is_valid():
			labelname=fm.cleaned_data['labelname']
			description=fm.cleaned_data['description']
			qr=qrcode.QRCode(
				version=1,box_size=10,border=5)
			qr.add_data(description)
			qr.make(fit=True)
			img=qr.make_image(fill="black",back_color="white")
			imgurl="media/qrcodeimage/{}.png".format(labelname)
			img.save(imgurl)
			sv=QrcodeData(labelname=labelname,description=description,qrimg=imgurl)
			sv.save()
			obj = QrcodeData.objects.latest('id')
			redirecturl='/{}/qrgenerated'.format(obj.id)
			return redirect(redirecturl) 

	return render(request,'qrform.html',{'form':fm})



def detail(request,id):
	qr=QrcodeData.objects.get(id=id)
	return render(request,'qrshowdetail.html',{'data':qr})



	