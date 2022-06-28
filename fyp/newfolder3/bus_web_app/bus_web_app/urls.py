"""bus_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home
from django.contrib import admin
from django.urls import include,path
from django.urls import include, re_path
from. import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name="home"),
    path ('payment/',  views.payment,name="payment"),
   
    path('bus_catalog/', include('bus_catalog.urls')),
    path('users/', include('users.urls')),
    path ('bus_catalog/buses/', include('bus_catalog.urls'), name= "buses"),
     path ('bus_catalog/buses/seats', include('bus_catalog.urls'), name= "seats"),
    path('users/signup/', include('users.urls'), name = "signup"),
    path('login/', include('users.urls'), name ="login"),
    path ('ticket page/',views.ticket_generator, name ="ticket")
]
urlpatterns += staticfiles_urlpatterns()


#cofigure admiN titles

admin.site.site_header = 'Online Bus Booking Web Module Administration Page'
admin.site.site_title = 'web module'