from django.contrib import admin
from .models import Collaboration, Story, Activity, Crousel

# Register your models here.
admin.site.register(Collaboration)
admin.site.register(Story)
admin.site.register(Crousel)
admin.site.register(Activity)