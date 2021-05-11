from django.shortcuts import render, HttpResponse, redirect
from .models import Crousel, Story, Activity, Collaboration
# Create your views here.

def home(request) :
    crousel=Crousel.objects.order_by("Order")
    story=Story.objects.order_by("Order")
    activity=Activity.objects.order_by("Order")
    collaboration=Collaboration.objects.order_by("Order")
    return render(request,"student/home.html",{"crousel":crousel,"activity":activity,"story":story,"collabortion":collaboration})