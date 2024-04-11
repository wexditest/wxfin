from django.contrib import admin

# Register your models here.

from .models import *

class KYCAdmin(admin.ModelAdmin):
  list_display = ("user_name",)


# Register your models here.
admin.site.register(KYC, KYCAdmin)

admin.site.register(HomeBanner)
admin.site.register(Slider)
admin.site.register(ChitActivities)
admin.site.register(StockLastestNews)




