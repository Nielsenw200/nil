from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import SignupForm
import braintree

from bus_catalog.mixins import (
	
	TokenGenerator,
	#CreateEmail
	)

#from bus_catalog.models import (
#	UserToken
#)
from bus_catalog.mixins import (
	gateway,
	BraintreeAccount,
	BraintreePayment,
	BraintreeData,
	generate_client_token,
	transact,
	find_transaction,
	)
# Create your views here.


def signup_view (request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
          form.save() 
          user=form.save()
          username = form.cleaned_data['username']
          password=form.cleaned_data['password1']
          user=authenticate(username=username, password=password)
          login(request,user)
          messages.success(request,("Registration Succesful") )
          agent_id = BraintreeAccount(user)
          token = TokenGenerator()
          make_token = token.make_token(user)
          ut = UserToken.objects.create(user=user,token=make_token)
      #log user in
          return redirect('checkout_page')

    else:    

     form=SignupForm()
    return render (request, 'register.html', {'form':form})

   


def login_view(request):
    if request.method=='POST':
        form= AuthenticationForm(data=request.POST)


        if form.is_valid():
            user=form.get_user()
            login(request,user)
            messages.success(request, "you were logged in succesfully")  
        return redirect('home')

    else: 
           form=AuthenticationForm()

    return render(request,'login.html',{'form':form})  


def logout_user(request):
    logout(request)
    messages.success(request, "you were logged out succesfully")
    return redirect('home')