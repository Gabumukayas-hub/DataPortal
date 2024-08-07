from django.shortcuts import render, redirect
from django import forms
from personal.forms import farmerforms
from personal.models import farmermodels
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def thankyou(request):
	return render(request, 'personal/base.html')

def farmer_view(request):
	form=farmerforms()
	if request.method=='POST':
		form=farmerforms(request.POST)
		if form.is_valid():
		 name=form.cleaned_data['name']
		 age=form.cleaned_data['age']
		 city=form.cleaned_data['city']
		 livestock=form.cleaned_data['livestock']
		 crop=form.cleaned_data['crop']
		 profit_or_loss=form.cleaned_data['profit_or_loss']
		 reg=farmermodels(name=name,age=age,city=city,livestock=livestock,crop=crop,profit_or_loss=profit_or_loss)
		 reg.save()
		 return redirect('home')


		else:
			print("Not Valid data")
	else:
		print("This is GET request")
	return render(request, 'farmer.html', {'form':form})



def home(request):
	print(request.headers)
	#check to see if logging in
	if request.method == 'POST':
		Username = request.POST ['username']
		Password = request.POST ['password']
	#authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You have been logged in!")
			return redirect ('home')
		else:
			messages.success(request, "There was an error logging in. Please try again ...")
			return redirect ('home')
	else:		
		return render(request, "index.html", {})





def data(request):
	print(request.headers)
	return render(request, "data page.html", {})
def data(request):
	print(request.headers)
	return render(request, "data page.html", {})






