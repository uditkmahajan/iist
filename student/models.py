from django.db import models

# Create your models here.collaboration activity crousel story

class Collaboration(models.Model) :
    Tag=models.CharField(max_length=30,default="iist")
    Order=models.IntegerField(default=0)
    Image=models.ImageField(upload_to="collaboration/")
    def __str__(self) :
        return self.Order
    
class Activity(models.Model) :
    Tag=models.CharField(max_length=30,default="iist")
    Order=models.IntegerField(default=0)
    Image=models.ImageField(upload_to="activity/")
    def __str__(self) :
        return self.Order

class Story(models.Model) :
    Tag=models.CharField(max_length=30,default="iist")
    Order=models.IntegerField(default=0)
    Image=models.ImageField(upload_to="story/")
    def __str__(self) :
        return self.Tag

class Crousel(models.Model) :
    Tag=models.CharField(max_length=30,default="iist")
    Detail=models.CharField(max_length=100,default=" ")
    Order=models.IntegerField(default=0)
    Image=models.ImageField(upload_to="crousel/")
    def __str__(self) :
        return self.Detail

class Gallery(models.Model) :
    Detail=models.CharField(max_length=100,default=" ")
    Order=models.IntegerField(default=0)
    Image=models.ImageField(upload_to="gallery/")
    def __str__(self) :
        return self.Detail