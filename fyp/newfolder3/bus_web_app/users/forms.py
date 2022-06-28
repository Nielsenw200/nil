from contextlib import suppress
import imp
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class SignupForm(UserCreationForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}) )
    last_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields =('username', 'first_name', 'last_name','email', 'password1','password2')
    










    
 #   def__init__(self,*args,**kwargs):
  #      super(SignupForm, self).__init__(*args,**kwargs)
   


   #    self.fields['username,'self].widget.attrs['class']='form-control'
    #   self.fields['password1,'self].widget.attrs['class']='form-control'
     #  self.fields['password2,'self].widget. 