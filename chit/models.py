from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import datetime



class ChitDetails(models.Model):
  chit_name = models.CharField(max_length=255)
  chit_total_amt = models.CharField(max_length=255)
  chit_taken_amt = models.CharField(max_length=255)
  chit_nottaken_amt = models.CharField(max_length=255)
  chit_isactive = models.BooleanField('Chit Status', default=False)
  chit_isstarted = models.BooleanField('Chit Started', default=False)

  chit_total_month_count = models.CharField(max_length=255,blank=True)
  chit_start_from = models.CharField(max_length=255,blank=True)
  chit_duedate_month = models.CharField(max_length=255,blank=True)
  chit_disbursedate_month = models.CharField(max_length=255,blank=True)
  chit_enrolldate_month = models.CharField(max_length=255,blank=True)


  def __str__(self):
    return self.chit_name


MONTH_CHOICES =(
("","--"),
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

PAYMODE_CHOICES =(
("","--"),
("Online", "Online"),
("Cash", "Cash"),
)

class AgentList(models.Model):
  agent_name = models.CharField(max_length=255,blank=True)

  def __str__(self):
    return self.agent_name



class MonthWiseChitDetails(models.Model):
  chit_details = models.ForeignKey(ChitDetails,on_delete=models.CASCADE)
  chit_month = models.CharField(max_length=9, choices=MONTH_CHOICES, default="", blank=True)
  chit_year = models.CharField(max_length=255,blank=True)
  get_chit_amount = models.CharField(max_length=255)
  winner_of_chit = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
  agent_name = models.ForeignKey(AgentList,on_delete=models.CASCADE,blank=True, null=True)
  agent_pay_for_chit = models.CharField(max_length=255,blank=True)

  disburment_pic = models.ImageField(default='avatar.jpg', upload_to='disburment_pic/' )
  payment_mode = models.CharField(max_length=9, choices=PAYMODE_CHOICES, default="", blank=True)







CAT =(
("Customer", "Customer"),
("Management", "Management"),
)

class CustomerChitPlan(models.Model):
  customer_chit_details = models.ForeignKey(ChitDetails,on_delete=models.CASCADE)
  customer_name = models.ForeignKey(User,on_delete=models.CASCADE)
  category = models.CharField(max_length=100, choices=CAT, default="Customer", blank=True)



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



# Create your models here.
class ChitPaymentNotification(models.Model):
  user_of_chit = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
  msg = models.CharField(max_length=555,blank=True)
  is_active = models.BooleanField(default=False)
  chit_details = models.ForeignKey(ChitDetails,on_delete=models.CASCADE,blank=True, null=True)

  chit_month = models.CharField(max_length=9, blank=True)
  chit_year = models.CharField(max_length=255,blank=True)
