from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import datetime
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from PIL import Image



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
  proof_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf')
  proof_choice = models.CharField(max_length=9, choices=PROOF_CHOICES, default="aadhar")
  bank_name = models.CharField(max_length=255)
  bank_account_no = models.CharField(max_length=255)
  bank_branch = models.CharField(max_length=255)
  bank_ifsc = models.CharField(max_length=255)
  upi_id = models.CharField(max_length=255)
  bank_proof_choice = models.CharField(max_length=9, choices=BANK_PROOF_CHOICES, default="aadhar")
  bank_proof_file = models.FileField(upload_to="proof/" , default='proof/myfile.pdf')

  def __str__(self):
    return self.user_name





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
