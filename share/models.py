from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import datetime
# Create your models here.
TRADE_CHOICES =(
("SWING", "SWING"),
("INTRADAY", "INTRADAY"),

)

SUB_CHOICES =(
("FREE", "FREE"),
("STANDARD", "STANDARD"),
("ADVANCE", "ADVANCE"),

)

TREND=(
    ('BULLISH','BULLISH'),
    )

from django.contrib.auth.models import User

class Subscription(models.Model):
  user_name = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
  sub_choice = models.CharField(max_length=9, choices=SUB_CHOICES, default="FREE")




class SwingTrade(models.Model):
  stock_name = models.CharField(max_length=255)
  stock_title = models.CharField(max_length=255,default="")
  stock_buy_price = models.CharField(max_length=255,default="")
  stock_sell_price = models.CharField(max_length=255,default="")

  upload = models.ImageField(upload_to ='share/')
  report_date = models.DateField(default=datetime.now)
  hold_upto_date = models.DateField(default=datetime.now)

  trade_choice = models.CharField(max_length=9, choices=TRADE_CHOICES, default="SWING")
  trend_choice = models.CharField(max_length=9, choices=TREND, default="BULLISH")


  def __str__(self):
    return self.stock_name

class DividendTrade(models.Model):
  stock_name = models.CharField(max_length=255)
  upload_pic = models.ImageField(upload_to ='share/')
  ex_date = models.CharField(max_length=255)
  dividend_share = models.CharField(max_length=255,default='' )
  dividend_yield = models.CharField(max_length=255,default='' )
  yield_msg = models.CharField(max_length=255,default='' )
  record_date = models.CharField(max_length=255,default='')



  def __str__(self):
    return self.stock_name