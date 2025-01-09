from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import datetime
# Create your models here.
from chit.models import *
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime
from datetime import datetime



class ContactUs(models.Model):
    """
    Represents a Home page Banner
    """

    name = models.CharField(max_length=100, null=True, blank=True,)
    email = models.CharField(max_length=100, null=True, blank=True,)
    phone = models.CharField(max_length=100, null=True, blank=True,)
    subject = models.CharField(max_length=100, null=True, blank=True,)
    message = models.CharField(max_length=100, null=True, blank=True,)




class ExpensesList(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()



PROOF_CHOICES =(
("aadhar", "aadhar"),
("voter", "voter"),

)



class LotterySpinList(models.Model):
  title = models.CharField(max_length=255,blank=True, null=True)
  option1 = models.CharField(max_length=255,blank=True, null=True)
  option2 = models.CharField(max_length=255,blank=True, null=True)
  option3 = models.CharField(max_length=255,blank=True, null=True)
  option4 = models.CharField(max_length=255,blank=True, null=True)
  option5 = models.CharField(max_length=255,blank=True, null=True)
  option6 = models.CharField(max_length=255,blank=True, null=True)
  option7 = models.CharField(max_length=255,blank=True, null=True)
  option8 = models.CharField(max_length=255,blank=True, null=True)

  entry_date = models.DateField(default=datetime.now)


class IncomeExpenses(models.Model):
  title = models.CharField(max_length=255,blank=True, null=True)
  income = models.FloatField()
  expense =  models.FloatField()
  entry_date = models.DateField(default=datetime.now)


class OneSlide(models.Model):
   summary_pic = models.ImageField(default='avatar.jpg', upload_to='summary_pic/' )

class UsefullLinks(models.Model):
  link_name = models.CharField(max_length=255,blank=True, null=True)
  site_link = models.URLField(max_length = 1000)

class ChitActivities(models.Model):
  act_date = models.DateField(default=datetime.now)
  act_name = models.CharField(max_length=255,blank=True, null=True)

class StockLastestNews(models.Model):
  news_date = models.DateField(default=datetime.now)
  stock_name = models.CharField(max_length=255)
  event_details = models.CharField(max_length=255)
  trend = models.CharField(max_length=255)
  stock_pic = models.ImageField(default='avatar.jpg', upload_to='stock_pic/' )





BANK_PROOF_CHOICES =(
("cheque", "cheque"),
("passbook", "passbook"),
("statement", "statement"),

)

class KYC(models.Model):
  user_name = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
  proof_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf',blank=True, null=True)
  proof_choice = models.CharField(max_length=9, choices=PROOF_CHOICES, default="aadhar")



LOAN_CHOICES =(
("APPROVED", "APPROVED"),
("REJECT", "REJECT"),
("IN-PROCESS", "IN-PROCESS"),



)

CREDIT_CHOICES =(
("CLOSE", "CLOSE"),
("PRE-CLOSE", "PRE-CLOSE"),
("ACTIVE", "ACTIVE"),
("REJECT", "REJECT"),
("IN-PROCESS", "IN-PROCESS"),
("DISBURSEMENT", "DISBURSEMENT"),




)


ADDRESS_CHOICES =(
("aadhar", "aadhar"),
("voter", "voter"),

)


ID_CHOICES =(
("aadhar", "aadhar"),
("pancard", "pancard"),

)

INCOME_CHOICES =(
("salaried", "salaried"),
("business", "business"),

)



class P2PRequestForm(models.Model):
  user_name = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

  address_proof_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf',blank=True, null=True)
  address_proof_choice = models.CharField(max_length=9, choices=ADDRESS_CHOICES, default="aadhar")
  address_proof_password = models.CharField(max_length=255,blank=True, null=True)

  id_proof_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf',blank=True, null=True)
  id_proof_choice = models.CharField(max_length=9, choices=ID_CHOICES, default="aadhar")
  id_proof_password = models.CharField(max_length=255,blank=True, null=True)


  income_proof_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf',blank=True, null=True)
  income_proof_choice = models.CharField(max_length=9, choices=INCOME_CHOICES, default="aadhar")
  income_proof_password = models.CharField(max_length=255,blank=True, null=True)


  gps_location_proof_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf',blank=True, null=True)



  chit_amount = models.ForeignKey(ChitDetails,on_delete=models.CASCADE,blank=True, null=True)
  eligibility_amount = models.CharField(max_length=255,blank=True, null=True)
  emi_amount= models.CharField(max_length=255,blank=True, null=True)
  no_of_months= models.CharField(max_length=255,blank=True, null=True)
  processing_charges= models.CharField(max_length=255,blank=True, null=True)
  disburment_amount= models.CharField(max_length=255,blank=True, null=True)
  entry_date = models.DateField(default=datetime.now,blank=True, null=True)
  is_approved = models.BooleanField(default=False)

  loan_status = models.CharField(max_length=39, choices=LOAN_CHOICES, default="IN-PROCESS")

  credit_status = models.CharField(max_length=39, choices=CREDIT_CHOICES, default="IN-PROCESS")

  disbursment_proof_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf',blank=True, null=True)
  customer_disbursment_recived_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf',blank=True, null=True)


EMI_CHOICES =(
("1", "1"),
("2", "2"),
("3", "3"),
("4", "4"),
("5", "5"),
("6", "6"),
)

PAYMENT_CHOICES =(
("NotPaid", "NotPaid"),
("Paid", "Paid"),
)


MONTH_CHOICES =(
("1", "January"),
("2", "Feburary"),
("3", "March"),
("4", "April"),
("5", "May"),
("6", "June"),
("7", "July"),
("8", "August"),
("9", "September"),
("10", "October"),
("11", "November"),
("12", "December"),
)

class P2PCreditEMI(models.Model):
  p2prequest_obj = models.ForeignKey(P2PRequestForm,on_delete=models.CASCADE,blank=True, null=True)
  payment_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf',blank=True, null=True)
  emi_choice = models.CharField(max_length=9, choices=EMI_CHOICES, default="aadhar")
  chit_amount = models.ForeignKey(ChitDetails,on_delete=models.CASCADE,blank=True, null=True)
  payment_choice = models.CharField(max_length=9, choices=PAYMENT_CHOICES, default="NotPaid")
  payment_month = models.CharField(max_length=20, choices=MONTH_CHOICES, default="10")
  payment_year = models.CharField(max_length=5, blank=True)
  p2p_amount = models.CharField(max_length=255,blank=True, null=True)




class P2PPaymentNotification(models.Model):
  p2ploan = models.CharField(max_length=255,blank=True, null=True)
  customer_name = models.CharField(max_length=255,blank=True, null=True)
  p2p_amount = models.CharField(max_length=255,blank=True, null=True)
  payment_choice = models.CharField(max_length=255,blank=True, null=True)
  payment_month = models.CharField(max_length=255,blank=True, null=True)
  payment_year = models.CharField(max_length=255,blank=True, null=True)




class CustomerBankDetails(models.Model):
  bank_name = models.CharField(max_length=255,blank=True, null=True)
  bank_account_no = models.CharField(max_length=255,blank=True, null=True)
  bank_branch = models.CharField(max_length=255,blank=True, null=True)
  bank_ifsc = models.CharField(max_length=255,blank=True, null=True)
  upi_id = models.CharField(max_length=255,blank=True, null=True)
  bank_proof_choice = models.CharField(max_length=9, choices=BANK_PROOF_CHOICES, default="aadhar")
  bank_proof_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf',blank=True, null=True)


class UpcomingDividends(models.Model):
    company_name = models.CharField(max_length=255,blank=True, null=True)
    announcement_date = models.CharField(max_length=255,blank=True, null=True)
    divd_type = models.CharField(max_length=255,blank=True, null=True)
    ex_date	 = models.CharField(max_length=255,blank=True, null=True)
    record_date	 = models.CharField(max_length=255,blank=True, null=True)
    dps	 = models.CharField(max_length=255,blank=True, null=True)
    div_percentage = models.CharField(max_length=255,blank=True, null=True)
    stock_price = models.CharField(max_length=255,blank=True, null=True)
    action = models.IntegerField(max_length=255,blank=True, null=True,default=-1)


class Slider(models.Model):
    slide = models.ImageField(default='avatar.jpg', upload_to='slide/' )
    videofile= models.FileField(upload_to='deploy/videos/', null=True, verbose_name="video")



class HomeBanner(models.Model):
    banner = models.ImageField(default='avatar.jpg', upload_to='home_banner/' )
    banner_date = models.DateField(default=datetime.now)




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='avatar.jpg', # default avatar
        upload_to='profile_avatars/' # dir to store the image
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)
