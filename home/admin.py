from django.contrib import admin

# Register your models here.

from .models import *



class ProfileAdmin(admin.ModelAdmin):
  pass

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
