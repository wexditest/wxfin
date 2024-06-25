from django.contrib import admin

# Register your models here.

from .models import *

class KYCAdmin(admin.ModelAdmin):
  list_display = ("user_name",)

class UsefullLinksAdmin(admin.ModelAdmin):
  list_display = ("link_name","site_link")



class UsefullLinksAdmin(admin.ModelAdmin):
  list_display = ("link_name","site_link")

class IncomeExpensesAdmin(admin.ModelAdmin):
  list_display = ("title","income","expense","entry_date")




from django.contrib import admin

class P2PCreditEMIInline(admin.TabularInline):
    model = P2PCreditEMI




class P2PRequestFormAdmin(admin.ModelAdmin):
    list_display = ("user_name",
                  "proof_file",
                  "proof_choice",
                  "chit_amount",
                  "eligibility_amount",
                  "emi_amount",
                  "no_of_months",
                  "processing_charges",
                  "disburment_amount",
                  "entry_date",
                  "is_approved",
                  "credit_status",)
    inlines = [P2PCreditEMIInline]


class ExpensesListAdmin(admin.ModelAdmin):
  list_display = ("name","amount")

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name',)



# Register your models here.

admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ExpensesList, ExpensesListAdmin)

admin.site.register(P2PRequestForm, P2PRequestFormAdmin)
admin.site.register(UsefullLinks, UsefullLinksAdmin)
admin.site.register(KYC, KYCAdmin)
admin.site.register(UpcomingDividends)
admin.site.register(HomeBanner)
admin.site.register(Slider)
admin.site.register(ChitActivities)
admin.site.register(StockLastestNews)
admin.site.register(OneSlide)
admin.site.register(IncomeExpenses,IncomeExpensesAdmin)
admin.site.register(LotterySpinList)









