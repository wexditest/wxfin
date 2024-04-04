from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . forms import *
from chit.models import *
from share.models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from io import BytesIO     # for handling byte strings
from io import StringIO    # for handling unicode strings
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from markupsafe import escape
from django.contrib.auth.models import User
from django.contrib import messages
from .models import  *


# Create your views here.


from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# ...


@login_required(login_url="my-login")
def profile(request):
    return render(request,'home/profile.html', {})


class MyProfile(LoginRequiredMixin,View):
    def get(self, request):
        profile_form = ProfileUpdateForm(instance=request.user)

        context = {
            'profile_form': profile_form,
            'user': request.user
        }

        return render(request, 'home/profile.html', context)

    def post(self,request):

        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if profile_form.is_valid():

            profile_form.save()

            messages.success(request,'Your profile has been updated successfully')

            return redirect('profile')
        else:
            context = {
                'profile_form': profile_form
            }
            messages.error(request,'Error updating you profile')

            return render(request, 'home/profile.html', context)





def enroll_chit_page(request):
    form = EnrollChitForm()

    form.fields['customer_details'].queryset = User.objects.filter(id=request.user.id)
    #form.fields['customer_details'].initial = request.user
    msg = False
    if request.method == 'POST':
        form = EnrollChitForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Successfully register your request"
        form = EnrollChitForm()
    return render(request, 'home/enroll.html', {'form': form,'msg':msg})






def enroll_chit_plan(request):
    print("=================== enrollll======fffff")
    if request.method == 'GET':
           chit_id = request.GET['chit_id']
           chit_obj = ChitDetails.objects.get(id=int(chit_id))
           likedpost = EnrollChit(chit_details=chit_obj,customer_details=request.user,enroll_status='Participate') #getting the liked posts

           likedpost.save()
           return HttpResponse("Success!") # Sending an success response
    else:
           return HttpResponse("Request method is not a GET")





def generate_pdf(request,r_id):
    result = CustomerChitPaymentDetails.objects.get(id=r_id)

    return render_to_pdf(
            'home/receipt_print.html',
            {
                'pagesize':'A4',
                'mylist': result,
            }
        )

def get_chit_plan(request,chit_id):
    chit_det_obj = ChitDetails.objects.get(id=chit_id)
    result = MonthWiseChitDetails.objects.filter(chit_details__id=chit_id)

    return render_to_pdf(
            'home/plan_print.html',
            {
                'pagesize':'A4',
                'mylist': result,
                'chit_det_obj':chit_det_obj,
            }
        )


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    #context = Context()
    html  = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))



def my_logout(request):
    auth.logout(request)
    return redirect("my-login")




from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change-password/change_password.html', {'form': form})


def kyc(request):
    kyc_obj = KYC.objects.all()
    return render(request, 'change-password/kyc.html', {'kyc_obj': kyc_obj})


@login_required(login_url="my-login")
def repay(request):
    return render(request,'home/repay.html', {'user': request.user})


@login_required(login_url="my-login")
def history(request):
    cust_obj = CustomerChitPaymentDetails.objects.filter(customer_details__id=request.user.id)

    return render(request,'home/history.html', {'user': request.user,'cust_obj':cust_obj})



def home(request):
    context = {}
    chit_det_obj_all = ChitDetails.objects.filter(chit_isactive=True)
    swing_obj_all = SwingTrade.objects.all()
    div_obj_all = DividendTrade.objects.all()
    chit_count_dict = {}
    for cdo in chit_det_obj_all:
        get_count = CustomerChitPlan.objects.filter(customer_chit_details=cdo)
        chit_count_dict[cdo.id] = str(len(get_count))


    context = {'chit_det_obj_all':chit_det_obj_all,'swing_obj_all':swing_obj_all,"div_obj_all":div_obj_all,'chit_count_dict':chit_count_dict,}
    return render(request, 'home/home.html',context)


@login_required(login_url="my-login")

def dashboard(request):
    context = {}
    chit_det_obj = CustomerChitPlan.objects.filter(customer_name__id=request.user.id)
    chit_det_obj_all = ChitDetails.objects.filter(chit_isactive=True)
    chit_count_dict = {}
    for cdo in chit_det_obj_all:
        get_count = CustomerChitPlan.objects.filter(customer_chit_details=cdo)
        chit_count_dict[cdo.id] = len(get_count)


    plan_details_dict = {}
    for cdo in chit_det_obj:

        obj = MonthWiseChitDetails.objects.filter(chit_details__id=cdo.customer_chit_details.id)
        plan_details_dict[cdo.customer_chit_details.id] = obj

    plan_details_dict_all = {}
    for cdo in chit_det_obj_all:

        obj = MonthWiseChitDetails.objects.filter(chit_details__id=cdo.id)
        plan_details_dict_all[cdo.id] = obj


    context = {'chit_det_obj':chit_det_obj,'chit_count_dict':chit_count_dict,
               'plan_details_dict':plan_details_dict,'chit_det_obj_all':chit_det_obj_all,'plan_details_dict_all':plan_details_dict_all}
    return render(request, 'home/index.html',context)


def my_login(request):
    context = {}
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("dashboard")

    context = {'loginform': form}
    return render(request, 'home/my-login.html',context=context)
