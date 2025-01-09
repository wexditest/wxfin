import os
from django.core.management.base import BaseCommand
from django.conf import settings
from home.models import *
from chit.models import *
from django.core.management.base import BaseCommand
import csv


from datetime import date
month = date.today().month
year = date.today().year
day = date.today().day
if month == 1:
    month = "January"

if month == 2:
    month = "Feburary"

if month == 3:
    month = "March"

if month == 4:
    month = "April"

if month == 5:
    month = "May"

if month == 6:
    month = "June"

if month == 7:
    month = "July"

if month == 8:
    month = "August"

if month == 9:
    month = "September"

if month == 10:
    month = "October"

if month == 11:
    month = " November"

if month == 12:
    month = "December"

"""
Ever Month we need to run this
"""""






class Command(BaseCommand):
    def handle(self, *args, **options):
        print ("####################################Script is Started############################")
        # chit plan will come
        chit_detail_obj = ChitDetails.objects.filter(chit_isstarted=True)


        #MonthWiseChitDetails
        for i in chit_detail_obj:
            # customer chit group will come
            cust_chit_plan_obj = CustomerChitPlan.objects.filter(customer_chit_details__id=i.id)

            for ccpo in cust_chit_plan_obj:

                try:
                    check_payment = CustomerChitPaymentDetails.objects.get(chit_details__id=i.id,
                                                                              customer_details__id=ccpo.customer_name.id,
                                                                              chit_month=month,chit_year=year)
                    if check_payment.payment_status == "NotPaid" and i.chit_type == "Regular":
                        try:
                            is_cust_win_chit =  MonthWiseChitDetails.objects.get(chit_details__id=i.id,
                                                                                 winner_of_chit__id=ccpo.customer_name.id)

                            if is_cust_win_chit:
                                check_payment.amount_need_to_pay = i.chit_taken_amt

                        except:
                            check_payment.amount_need_to_pay = i.chit_nottaken_amt

                    if check_payment.payment_status=="NotPaid" and i.chit_type == "Continuous":

                        try:
                            is_cust_win_chit =  ContinuousChitWinner.objects.get(chit_details__id=i.id,
                                                                                 winner_of_chit__id=ccpo.customer_name.id)

                            if is_cust_win_chit:
                                check_payment.amount_need_to_pay = i.chit_taken_amt

                        except:
                            check_payment.amount_need_to_pay = i.chit_nottaken_amt

                    check_payment.save()


                except Exception as e:
                        pass



        print ("####################################Script is End ############################")



