from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def basee(request):
    return render(request,'basee.html')

def about1(request):
    return render(request,'about1.html')
 
def front(request):
    if request.method == "POST":
        name = request.POST.get('name')  
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        front = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        front.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'front.html')

