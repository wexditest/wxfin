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

        chit_detail_obj = ChitDetails.objects.filter(chit_isstarted=True)

        for i in chit_detail_obj:
            cust_chit_plan_obj = CustomerChitPlan.objects.filter(customer_chit_details__id=i.id)
            for ccpo in cust_chit_plan_obj:

                try:
                    check_payment = CustomerChitPaymentDetails.objects.get(chit_details__id=i.id,
                                                                              customer_details__id=ccpo.customer_name.id,
                                                                              chit_month=month,chit_year=year)
                    print ("already exist record")
                except Exception as e:
                        print ("creating new record")

                        ccpdetails = CustomerChitPaymentDetails(chit_details=i,
                                                                customer_details=ccpo.customer_name,
                                                                chit_month=month,
                                                                chit_year=year,
                                                                trans_id="need to update",
                                                                )
                        ccpdetails.save()

        print ("####################################Script is End ############################")



