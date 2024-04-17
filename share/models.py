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

TREND=(
    ('BULLISH','BULLISH'),
    )

class SwingTrade(models.Model):
  stock_name = models.CharField(max_length=255)
  upload = models.ImageField(upload_to ='share/')
  report_date = models.DateField(default=datetime.now)
  trade_choice = models.CharField(max_length=9, choices=TRADE_CHOICES, default="SWING")
  trend_choice = models.CharField(max_length=9, choices=TREND, default="BULLISH")


  def __str__(self):
    return self.stock_name

class DividendTrade(models.Model):
  stock_name = models.CharField(max_length=255)
  upload_pic = models.ImageField(upload_to ='share/')
  ex_date = models.CharField(max_length=255)


  def __str__(self):
    return self.stock_name