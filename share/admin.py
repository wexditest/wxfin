from django.contrib import admin

# Register your models here.
from .models import *
class SwingTradeAdmin(admin.ModelAdmin):
  list_display = ("stock_name", )

class DividendTradeAdmin(admin.ModelAdmin):
  list_display = ("stock_name","ex_date" )



# Register your models here.
admin.site.register(SwingTrade, SwingTradeAdmin)
admin.site.register(DividendTrade, DividendTradeAdmin)

admin.site.register(Subscription)