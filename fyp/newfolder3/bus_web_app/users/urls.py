from importlib.resources import path
from unicodedata import name

from django.urls import path
from .import views






urlpatterns = [
    
    path('signup/',views.signup_view, name ="signup"),
    path('login/',views.login_view, name ="login"),
    path('logout_user', views.logout_user,  name  ="logout"),
]
