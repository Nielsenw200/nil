from dataclasses import fields
from django import forms
from django.forms import ModelForm
from.models import Assigntrip 
from.models import Buses
from.models import Routes
from.models import Feedback




#bus query form
class  BusForm (ModelForm):
    class Meta:
      model = Assigntrip
      fields= [ 'travel_time']


#feedbackform


class FeedbackForm(ModelForm):
  class Meta:
    model=Feedback
    fields="__all__"

