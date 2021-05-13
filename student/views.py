from django.shortcuts import render, HttpResponse, redirect
from .models import Crousel, Story, Activity, Collaboration, Gallery, DG
# Create your views here.

def home(request) :
    crousel=Crousel.objects.order_by("Order")
    story=Story.objects.order_by("Order")
    activity=Activity.objects.order_by("Order")
    collaboration=Collaboration.objects.order_by("Order")
    return render(request,"student/home.html",{"crousel":crousel,"activity":activity,"story":story,"collabortion":collaboration})

def gallery(request) :
    gallery=Gallery.objects.order_by("Order")
    return render(request,"student/gallery.html",{"gallery":gallery})

def dg(request) :
    image=DG.objects.all()
    return render(request,"student/dg.html",{"dgimage":image})