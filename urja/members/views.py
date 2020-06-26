from django.shortcuts import render,redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages 


# Create your views here.

def home(request):
	return render(request,'member/home.html')


def insertmember(request):
	fm=MemberForm()
	x="";
	if request.method == 'POST':
		fm=MemberForm(request.POST)
		if fm.is_valid():
			data=fm.cleaned_data
			sv=Member(firstname=data['firstname'],lastname=data['lastname'],mobile=data['mobile'],
				email=data['email'],city=data['city'])
			sv.save();
			return redirect('members:getallmembers')
	return render(request,'member/insertmemberform.html',{'form':fm})


def getallmembers(request):
	allmember=Member.objects.all()
	return render(request,'member/viewmembers.html',{'allmember':allmember})


def loginmember(request):
	if request.method == 'POST':
		user=request.POST.get('username')
		pwd=request.POST.get('password')
		obj=Member.objects.filter(mobile=user,password=pwd).values_list('id','firstname')
		if obj:
			request.session['userinstance']=obj[0][0]
			request.session['userfirstname']=obj[0][1]
			return redirect('members:memberdata')
	return render(request,'member/login.html')

def memberdata(request):	
	userobj=request.session.get('userinstance')
	if userobj:
		memobj=Member.objects.filter(id=userobj)
		return render(request,'member/member.html',{'memdata':memobj})	

def logoutmember(request):
	del request.session['userinstance']
	del request.session['userfirstname']
	return redirect('members:home')		


def deletemembers(request,pk):
	memobj=Member.objects.get(id=pk)
	memobj.delete()
	return redirect('members:getallmembers')


def editmembers(request,pk):
	memobj=Member.objects.get(id=pk)
	if request.method == 'POST':
		form=MemberForm(request.POST,instance=memobj)
		if form.is_valid():
			form.save()
			return redirect('members:getallmembers')



	return render(request,'member/editmembers.html',{'member':memobj})

	