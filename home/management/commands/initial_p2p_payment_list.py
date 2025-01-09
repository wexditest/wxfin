import os
from django.core.management.base import BaseCommand
from django.conf import settings
from home.models import *
from chit.models import *
from django.core.management.base import BaseCommand
import csv









class Command(BaseCommand):
    def handle(self, *args, **options):
        print ("####################################Script is Started############################")
        from datetime import date
        month = date.today().month
        year = date.today().year
        P2PPaymentNotification.objects.all().delete()

        p2p_detail_obj = P2PCreditEMI.objects.filter(payment_choice="NotPaid",payment_month=month,payment_year=str(year))

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

        for i in p2p_detail_obj:

            pdetails = P2PPaymentNotification(p2ploan=i.id,customer_name=i.p2prequest_obj.user_name.first_name,
                                              p2p_amount =i.p2p_amount,
                                              payment_choice = "NotPaid",
                                              payment_month = month,
                                              payment_year = year,)
            pdetails.save()



        print ("####################################Script is End ############################")



