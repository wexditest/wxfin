from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import datetime
# Create your models here.

class ChitDetails(models.Model):
  chit_name = models.CharField(max_length=255)
  chit_total_amt = models.CharField(max_length=255)
  chit_taken_amt = models.CharField(max_length=255)
  chit_nottaken_amt = models.CharField(max_length=255)
  chit_isactive = models.BooleanField('Chit Status', default=False)
  chit_total_month_count = models.CharField(max_length=255,blank=True)
  chit_start_from = models.CharField(max_length=255,blank=True)

  def __str__(self):
    return self.chit_name


MONTH_CHOICES =(
("January", "January"),
("Feburary", "Feburary"),
("March", "March"),
("April", "April"),
("May", "May"),
("June", "June"),
("July", "July"),
("August", "August"),
("September", "September"),
("October", "October"),
("November", "November"),
("December", "December"),
)


class MonthWiseChitDetails(models.Model):
  chit_details = models.ForeignKey(ChitDetails,on_delete=models.CASCADE)
  chit_month = models.CharField(max_length=9, choices=MONTH_CHOICES, default="January", blank=True)
  chit_year = models.CharField(max_length=255,blank=True)
  get_chit_amount = models.CharField(max_length=255)
  winner_of_chit = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

class CustomerChitPlan(models.Model):
  customer_chit_details = models.ForeignKey(ChitDetails,on_delete=models.CASCADE)
  customer_name = models.ForeignKey(User,on_delete=models.CASCADE)



PAY_CHOICES =(
("NotPaid", "NotPaid"),
("Paid", "Paid"),
)


class CustomerChitPaymentDetails(models.Model):
  chit_details = models.ForeignKey(ChitDetails,on_delete=models.CASCADE)
  customer_details = models.ForeignKey(User,on_delete=models.CASCADE)
  chit_month = models.CharField(max_length=9, choices=MONTH_CHOICES, default="January", blank=True)
  chit_year = models.CharField(max_length=255,blank=True)
  payment_status = models.CharField(max_length=9, choices=PAY_CHOICES, default="NotPaid")
  trans_id = models.CharField(max_length=555,default="")
  payment_file = models.FileField(upload_to="paymentfiles/" , default='paymentfiles/myfile.pdf')
  amount_paid = models.CharField(max_length=255, default=0.0)
  payment_date = models.DateField(default=datetime.now)

PURPOSE_CHOICES =(
("Auction", "Auction"),
("Participate", "Participate"),
("NA", "NA"),

)


ADMIN_CHOICES =(
("Accept", "Accept"),
("NotAccept", "NotAccept"),
("Pending", "Pending"),


)

class EnrollChit(models.Model):
    chit_details = models.ForeignKey(ChitDetails,on_delete=models.CASCADE)
    customer_details = models.ForeignKey(User,on_delete=models.CASCADE)
    enroll_status = models.CharField(max_length=29, choices=PURPOSE_CHOICES, default="NA")
    admin_per_status = models.CharField(max_length=29, choices=ADMIN_CHOICES, default="Pending")
    chit_month_count = models.CharField(max_length=255, default=0)



