from importlib.resources import path
from unicodedata import name

from django.urls import path
from .import views



urlpatterns = [


    path ('buses/', views.search_results,   name ="buses"),
    path('buses/buspage/', views.seats_page, name="seats"),
    path( 'occupied/',views.occupiedSeats, name="occupied_seat"),
    path('userdetails', views.user_details, name="details"),
    path ('contacts/', views.contacts,name ="contacts"),
    #path ('payment/',  views.payment,name="payment"),
   # path('ticket', views.ticket_pdf, name='ticket_pdf'),
    path ('payNow/<int:id>/', views.payment,name ="payment"),
    path ('pay/<int:id>/', views.checkout_page,name ="pay"),
]








