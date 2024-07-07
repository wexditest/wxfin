from django.contrib import admin

from .models import *

from django import forms

# Register admin Pages.

class ChitDetailsAdmin(admin.ModelAdmin):
  pass


def duplicate_event(MonthWiseChitDetailsAdmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
duplicate_event.short_description = "Duplicate selected record"


class CustomBarModelForm(forms.ModelForm):
    class Meta:
        model = MonthWiseChitDetails
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomBarModelForm, self).__init__(*args, **kwargs)
        try:
            ccp_obj = CustomerChitPlan.objects.filter(customer_chit_details__id=self.instance.chit_details.id)
            list_user_id = []
            for i in ccp_obj:
                list_user_id.append(i.customer_name.id)
            self.fields['winner_of_chit'].queryset = User.objects.filter(id__in=list_user_id)# or something else
        except:
            pass

# Use it in your modelAdmin




class MonthWiseChitDetailsAdmin(admin.ModelAdmin):
  form = CustomBarModelForm

  actions = [duplicate_event]
  list_display = ("id","chit_details", "chit_month","chit_year","get_chit_amount","winner_of_chit")
  list_filter = ("chit_details",)




class CustomerChitPlanAdmin(admin.ModelAdmin):
  list_display = ("customer_chit_details", "customer_name","category")
  list_filter = ("customer_chit_details","category")



def duplicate_event_chit_payment_customer(CustomerChitPaymentDetailsAdmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
duplicate_event_chit_payment_customer.short_description = "Duplicate selected record"

class CustomerChitPaymentDetailsAdmin(admin.ModelAdmin):
  autocomplete_fields = ['customer_details']
  actions = [duplicate_event_chit_payment_customer]
  list_display = ("chit_details","customer_details","chit_month","chit_year","payment_status")
  list_filter=("chit_details","customer_details","chit_month","chit_year")

class EnrollChitAdmin(admin.ModelAdmin):
  list_display = ("chit_details", "customer_details",'enroll_status','admin_per_status')


class ChitPaymentNotificationAdmin(admin.ModelAdmin):
  list_display = ("user_of_chit", "msg",'is_active','chit_details','chit_month','chit_year')
  list_filter=("user_of_chit","is_active","chit_month","chit_year","chit_details")


admin.site.register(ChitPaymentNotification,ChitPaymentNotificationAdmin)


class AgentListAdmin(admin.ModelAdmin):
   pass #list_display = ("chit_details", "customer_details",'enroll_status','admin_per_status')




# Register your models here.
admin.site.register(EnrollChit, EnrollChitAdmin)

admin.site.register(AgentList, AgentListAdmin)

admin.site.register(ChitDetails, ChitDetailsAdmin)
admin.site.register(MonthWiseChitDetails, MonthWiseChitDetailsAdmin)
admin.site.register(CustomerChitPlan, CustomerChitPlanAdmin)
admin.site.register(CustomerChitPaymentDetails, CustomerChitPaymentDetailsAdmin)


# Admin page setup
admin.site.site_header = "Wexdi Finance Admin"
admin.site.index_title = "Welcome to Wexdi Finance"
admin.site.site_title = "Wexdi Finance"