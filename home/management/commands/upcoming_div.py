import os
from django.core.management.base import BaseCommand
from django.conf import settings
from home.models import *
from django.core.management.base import BaseCommand
import csv

# upload = "https://portal.tradebrains.in/corporateactions/Dividends"
# check div.csv in https://www.pythonanywhere.com/user/wexdifinance/files/home/wexdifinance/finance location...

class Command(BaseCommand):
    def handle(self, *args, **options):

        UpcomingDividends.objects.all().delete()#delete()

        with open(os.path.join(settings.BASE_DIR / 'div.csv'), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                #print (row)
                for r in row:
                    print (r)
                    print ("----")
                try:
                    action=int(row[8])
                except:
                    action = -1
                obj = UpcomingDividends.objects.create(company_name=row[0],
                                                announcement_date=row[1],
                                                divd_type=row[2],
                                                ex_date=row[3],
                                                record_date=row[4],
                                                dps=row[5],
                                                div_percentage=row[6],
                                                stock_price=row[7],action=action,)

                obj.save()
