from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import *
from chit.models import *

# Create User
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# Authenticate User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class KYCForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = "__all__"


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class EnrollChitForm(forms.ModelForm):
    CHOICES = (('1', '1st'),
               ('2', '2nd'),
               ('2', '3rd'),
               ('4', '4th'),
               ('5', '5th'),
               ('6', '6th'),
               ('7', '7th'),
               ('8', '8th'),
               ('9', '9th'),
               ('10', '10th'),
               ('11', '11th'),
               ('12', '12th'),
               ('13', '13th'),
               ('14', '14th'),
               ('15', '15th'),
               ('16', '16th'),
               ('17', '17th'),
               ('18', '18th'),
               ('19', '19th'),
               ('20', '20th'),
               )
    chit_month_count = forms.ChoiceField(choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(EnrollChitForm, self).__init__(*args, **kwargs)
        self.fields['chit_month_count'].label = "Select Chit Month"

    class Meta:
        model = EnrollChit
        exclude = ["admin_per_status",]



# class CreateReceiptForm(forms.ModelForm):
#     class Meta:
#         model = UserChitPayments
#         exclude = ["payment_status",'trans_id','payment_file']



