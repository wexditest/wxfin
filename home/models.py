from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import datetime
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime
from datetime import datetime



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



PROOF_CHOICES =(
("aadhar", "aadhar"),
("voter", "voter"),
)

BANK_PROOF_CHOICES =(
("cheque", "cheque"),
("passbook", "passbook"),
("statement", "statement"),

)

class KYC(models.Model):
  user_name = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
  proof_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf',blank=True, null=True)
  proof_choice = models.CharField(max_length=9, choices=PROOF_CHOICES, default="aadhar")


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


class Slider(models.Model):
    slide = models.ImageField(default='avatar.jpg', upload_to='slide/' )


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
