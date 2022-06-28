from django.http import HttpResponse
import io
from django.http import FileResponse
from django.shortcuts import render

#from reportlab.pdfgen import canvas





def homepage(request):
    return render(request, 'index.html')



def payment(request):
   return render (request, 'e_ticket_page.html')

def contacts(request):
    return render (request,'contacts_page.html' ) 

def ticket_generator(request):
    buffer = io.BytesIO()

  #  p= canvas.Canvas(buffer)
   #  p.drawString(100 ,100 "hello jackass")

 #    p.showPage()
    # p.save()
     #buffer.seek(0)

     #return FileResponse(buffer,as_attachment=True, filename= 'ticket')






