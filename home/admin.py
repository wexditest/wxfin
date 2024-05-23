from django.contrib import admin

# Register your models here.

from .models import *

class KYCAdmin(admin.ModelAdmin):
  list_display = ("user_name",)

class UsefullLinksAdmin(admin.ModelAdmin):
  list_display = ("link_name","site_link")


# Register your models here.
admin.site.register(UsefullLinks, UsefullLinksAdmin)
admin.site.register(KYC, KYCAdmin)
admin.site.register(UpcomingDividends)
admin.site.register(HomeBanner)
admin.site.register(Slider)
admin.site.register(ChitActivities)
admin.site.register(StockLastestNews)
admin.site.register(OneSlide)






