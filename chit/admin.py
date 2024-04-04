from django.contrib import admin

from .models import *


# Register admin Pages.

class ChitDetailsAdmin(admin.ModelAdmin):
  pass


def duplicate_event(MonthWiseChitDetailsAdmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
duplicate_event.short_description = "Duplicate selected record"


class MonthWiseChitDetailsAdmin(admin.ModelAdmin):
  actions = [duplicate_event]
  list_display = ("chit_details", "chit_month","chit_year","get_chit_amount","winner_of_chit")
  list_filter = ("chit_details",)

class CustomerChitPlanAdmin(admin.ModelAdmin):
  list_display = ("customer_chit_details", "customer_name")
  list_filter = ("customer_chit_details",)


class CustomerChitPaymentDetailsAdmin(admin.ModelAdmin):
  list_display = ("chit_details","customer_details","chit_month","chit_year","payment_status")
  list_filter=("chit_details","customer_details","chit_month","chit_year")

class EnrollChitAdmin(admin.ModelAdmin):
  list_display = ("chit_details", "customer_details",'enroll_status','admin_per_status')



# Register your models here.
admin.site.register(EnrollChit, EnrollChitAdmin)

admin.site.register(ChitDetails, ChitDetailsAdmin)
admin.site.register(MonthWiseChitDetails, MonthWiseChitDetailsAdmin)
admin.site.register(CustomerChitPlan, CustomerChitPlanAdmin)
admin.site.register(CustomerChitPaymentDetails, CustomerChitPaymentDetailsAdmin)


# Admin page setup
admin.site.site_header = "Wexdi Finance Admin"
admin.site.index_title = "Welcome to Wexdi Finance"
admin.site.site_title = "Wexdi Finance"