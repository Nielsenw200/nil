from urllib import request
from django.http.response import HttpResponse, HttpResponseForbidden
#from movies.helpers import email_customer, verify_webook
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
import calendar
import datetime
from.models import AuthUser, Routes
from.models import Seat
from .models import Buses
from .models import Bookingtickets
from .models import Assigntrip
from django.core.exceptions import MultipleObjectsReturned
from django.utils.datastructures import MultiValueDictKeyError
import braintree
from django.db.models import Q 
#from .forms import BusForm
from .filters import BusFilter
from django.conf import settings
from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import json
import sys
from .forms import FeedbackForm
from .mixins import BraintreePayment
from .mixins import BraintreeAccount

#from ipware import get_client_ip



# Create your views here.

def contacts(request):
  submitted=False
  if request.method=="POST":
    form=FeedbackForm(request.POST)
    if form.is_valid():
      form.save() 
      return HttpResponseRedirect('/contacts? submitted=True')
  
  else:
    form=FeedbackForm
    if 'submitted' in request.GET:
      submitted=True
 
  return render (request,'contacts_page.html',{'form':form, 'submitted':submitted}) 
 
def search_results(request):
    if request.method == "POST":
      start= request.POST['start']
      end=request.POST['end']
      date=request.POST['date']
      buses= Routes.objects.filter(froms__icontains= start)
      ends=Routes.objects.filter(destination__icontains= end) 
      dates=Assigntrip.objects.filter(travel_time__contains=date)
      
     
      return render (request,'bus_booking_page.html' ,{'buses': buses ,'ends': ends, 'dates':dates})
    else:
       return render(request, 'index.html')   
  

def seats_page(request):
  #setted= search_results
  buses=Buses.objects.all()
  return render (request, 'seats_page.html',{"buses":buses})

def occupiedSeats(request):
    data=json.loads(request.body)
    busess=Buses.objects.get(title=data["busname"])
    occupied=busess.booked_seats.all()
    occupied_seat=list(map(lambda seat : seat.seat_no - 1,occupied))
 
    return JsonResponse({
        "occupied_seats":occupied_seat,
        "busess":str(busess)
   })

  
  

def user_details(request):
  return  render (request, 'user_details.html')   


#from ipware import get_client_ip
  

#def index(request):
 #   movies=Movie.objects.all()
  #  return render(request,'index.html',{
     #   "movies":movies
  # })

# @csrf_exempt
#def makePayement(request):
   # data=json.loads(request.body)
   # seat_numbers=list(map(lambda seat: seat+1,data["seat_list"]))
   # movie_title=data["movie_title"]
#
   # cost=Movie.objects.get(title=movie_title).price

#     header={
     #    "Authorization":f"Bearer {settings.PAYSTACK_SECRET}",
     #    "Content-Type":"application/json"
 #   }
# 
   #  data={
      #   "name":"Payment of Movie Ticket",
     #    "amount":int(cost*len(seat_numbers))*100,
      #   "description":f"Payment for {len(seat_numbers)} ticket of {movie_title}",
       #  "collect_phone":True,
       #  "redirect_url":f"{settings.HOST_URL}/payment-confirm/"
 #    }

  #   response=requests.post('https://api.paystack.co/page',
                         #    json=data,headers=header)

  #   if response.status_code ==200:
     #    response_data=response.json()
     #    slug=response_data["data"]["slug"]
       #  redirect_url=f"https://paystack.com/pay/{slug}"

       #  PaymentIntent.objects.create(referrer=redirect_url,
                                 #   movie_title=movie_title,
                                   #  seat_number=seat_numbers)
        
      #   return JsonResponse({
       #      "payment_url":redirect_url
        # })

  #   return JsonResponse({
  #       "error":"sorry service is not available"
  #   })


#@csrf_exempt
#def webhook(request):
  #   if request.method=="POST":
   #      ip,is_routable=get_client_ip(request)
        

       #  if ip in settings.PAYSTACK_IP and verify_webook(request):
         #    response=json.loads(request.body)
            
          #   if response["event"]== "charge.success":
           #      first_name=response["data"]["customer"]["first_name"]
           #      last_name=response["data"]["customer"]['last_name']
            #     phone=response["data"]["customer"]['phone']
            #     email=response["data"]["customer"]['email']
            #     amount=int(response["data"]["amount"])

            #     referrer=response["data"]["metadata"]["referrer"]

            #     payment_intent=PaymentIntent.objects.get(referrer=referrer)

             #    movie_title=payment_intent.movie_title
            #     movie=Movie.objects.get(title=movie_title)
            #     booked_seat=json.loads(payment_intent.seat_number)
# 
              #   for seat_no in booked_seat:
             #        seat=Seat.objects.create(seat_no=seat_no,
               #     occupant_first_name=first_name,
              #      occupant_last_name=last_name,
                  #   occupant_email=email)

                  #   movie.booked_seats.add(seat)
                  #   movie.save()

                  #   Payment.objects.create(first_name=first_name,
                  #   last_name=last_name,
                  #   email=email,
                  #   phone=phone,
                  #   movie=movie,
                  #   seat_no=seat_no)

                    # send email
              #       mailing.delay(first_name,email,seat_no,movie_title)

              #   return HttpResponse(200)

   #  return HttpResponseForbidden()
# def paymentConfirm(request):
  #   return HttpResponse('<h2>Thank you for purchasing Us....</h2>\n\
    #     <h2>An email has been sent to your email address with your seat number</h2>\n\
      #   <h2>Thank you once again</h2>\n\
        # <a href="/" >Click here to go to homepage</a>')


def checkout_page(request,pk):
    #generate all other required data that you may need on the #checkout page and add them to context.
    user = AuthUser.objects.filter(id=pk)
    agent_id  = user.agent_id
    try:
        braintree_client_token = braintree.ClientToken.generate({ "customer_id":agent_id })
    except:
        braintree_client_token = braintree.ClientToken.generate({})

    context = {'braintree_client_token': braintree_client_token , 'agent_id': agent_id}   
                 
    return render(request, 'e_ticket_page', context)


def payment(request,pk):
    registrant = AuthUser.objects.get(pk=pk)
    
    if request.method == "POST":		
        
        token = request.POST.get('braintreeToken',None)
        card_id = request.POST.get("card_id", None)
        payment_method_nonce = request.POST.get("paymentMethodNonce", None)
        description = request.POST.get("description", None)
        currency = request.POST.get("currency", None)
        set_default = request.POST.get("set_default", None)
        amount = request.POST.get('amount')
        agent_id = registrant.agent_id 
        # Create AgentID, if Applicant has no AgentID
        if not agent_id:
            BraintreeAccount(request.registrant).agent()
            
        payment = BraintreePayment(
			user=registrant,
			agent_id=agent_id,
			token=token,            
			card_id=card_id,
			amount=amount,
			description = description,
			currency=currency,
			set_default=set_default
			).create()
       
        if payment["message"] == "Perfect":

            invoice = Invoicing(
				user= registrant,
				tran_id = payment["tran_id"],
                description = description,
				amount = float(amount)
				)
            invoice.save()
            registrant = registrant

            return HttpResponse(
					json.dumps({"result": "okay"}),
					content_type="application/json"
					)
       
        else:
            return HttpResponse(
					json.dumps({"result": "error", "message":payment["message"] }),
					content_type="application/json"
					)
    else:
        return HttpResponse(
			json.dumps({"result": "error"}),
			content_type="application/json"
			#78325
			)
