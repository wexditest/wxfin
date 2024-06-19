import requests

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import csv
import requests
from social_django.models import Association, Code, Nonce, Partial, UserSocialAuth

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
from blog.models import *
from django.core.paginator import Paginator
from bs4 import BeautifulSoup
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from tabulate import tabulate
from io import BytesIO
from datetime import date
from nsepy import get_history
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup


#!/usr/bin/env python
# coding: utf-8

# In[50]:


# import necessary libraries

#get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from tabulate import tabulate
import pandas_datareader.data as web
import warnings
warnings.filterwarnings('ignore')


def chit_statement(request):
    if request.method == 'POST':
        chit_id = request.POST.get('chit_name')
        statement_user_payment = CustomerChitPaymentDetails.objects.filter(customer_details__id=request.user.id,chit_details__id=chit_id)

        # form = EnrollChitForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     msg="Successfully register your request"
        # form = EnrollChitForm()
    return render(request, 'home/chit_statement.html', {'statement_user_payment': statement_user_payment,})



def fin_literacy_tool(request):

    context = {}
    return render(request, 'home/fin_literacy_tool.html',context)


def p2p_lending(request):

    context = {}
    return render(request, 'home/p2p_lending.html',context)





def moving_avg_crossover(stock_symbol = 'ULTRACEMCO.NS', start_date = '2018-01-01', end_date = '2020-01-01',
                               short_window = 20, long_window = 50, moving_avg = 'SMA', display_table = True):


    # import the closing price data of the stock for the aforementioned period of time in Pandas dataframe
    start = datetime.datetime(*map(int, start_date.split('-')))
    end = datetime.datetime(*map(int, end_date.split('-')))
    stock_df = web.DataReader(stock_symbol, 'yahoo', start = start, end = end)['Close']
    stock_df = pd.DataFrame(stock_df) # convert Series object to dataframe
    stock_df.columns = {'Close Price'} # assign new colun name
    stock_df.dropna(axis = 0, inplace = True) # remove any null rows

    # column names for long and short moving average columns
    short_window_col = str(short_window) + '_' + moving_avg
    long_window_col = str(long_window) + '_' + moving_avg

    if moving_avg == 'SMA':
        # Create a short simple moving average column
        stock_df[short_window_col] = stock_df['Close Price'].rolling(window = short_window, min_periods = 1).mean()

        # Create a long simple moving average column
        stock_df[long_window_col] = stock_df['Close Price'].rolling(window = long_window, min_periods = 1).mean()

    elif moving_avg == 'EMA':
        # Create short exponential moving average column
        stock_df[short_window_col] = stock_df['Close Price'].ewm(span = short_window, adjust = False).mean()

        # Create a long exponential moving average column
        stock_df[long_window_col] = stock_df['Close Price'].ewm(span = long_window, adjust = False).mean()

    # create a new column 'Signal' such that if faster moving average is greater than slower moving average
    # then set Signal as 1 else 0.
    stock_df['Signal'] = 0.0
    stock_df['Signal'] = np.where(stock_df[short_window_col] > stock_df[long_window_col], 1.0, 0.0)

    # create a new column 'Position' which is a day-to-day difference of the 'Signal' column.
    stock_df['Position'] = stock_df['Signal'].diff()

    # plot close price, short-term and long-term moving averages
    plt.figure(figsize = (20,10))
    plt.tick_params(axis = 'both', labelsize = 14)
    stock_df['Close Price'].plot(color = 'k', lw = 1, label = 'Close Price')
    stock_df[short_window_col].plot(color = 'b', lw = 1, label = short_window_col)
    stock_df[long_window_col].plot(color = 'g', lw = 1, label = long_window_col)

    # plot 'buy' signals
    plt.plot(stock_df[stock_df['Position'] == 1].index,
            stock_df[short_window_col][stock_df['Position'] == 1],
            '^', markersize = 15, color = 'g', alpha = 0.7, label = 'buy')

    # plot 'sell' signals
    plt.plot(stock_df[stock_df['Position'] == -1].index,
            stock_df[short_window_col][stock_df['Position'] == -1],
            'v', markersize = 15, color = 'r', alpha = 0.7, label = 'sell')
    plt.ylabel('Price in ₹', fontsize = 16 )
    plt.xlabel('Date', fontsize = 16 )
    plt.title(str(stock_symbol) + ' - ' + str(moving_avg) + ' Crossover', fontsize = 20)
    plt.legend()
    plt.grid()
    plt.show()

    if display_table == True:
        df_pos = stock_df[(stock_df['Position'] == 1) | (stock_df['Position'] == -1)]
        df_pos['Position'] = df_pos['Position'].apply(lambda x: 'Buy' if x == 1 else 'Sell')
        print(tabulate(df_pos, headers = 'keys', tablefmt = 'psql'))

    return render(request, 'home/moving_avg_crossover.html', {'form': form,'msg':msg})







def enroll_chit_page(request):
    form = EnrollChitForm()
    form.fields['customer_details'].queryset = User.objects.filter(id=request.user.id)
    msg = False
    if request.method == 'POST':
        form = EnrollChitForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Successfully register your request"
        form = EnrollChitForm()
    return render(request, 'home/enroll.html', {'form': form,'msg':msg})


def enroll_chit_plan(request):
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
    #cust_obj = CustomerChitPaymentDetails.objects.filter(customer_details__id=request.user.id)
    return render_to_pdf(
            'home/receipt_print.html',
            {
                'pagesize':'A4',
                'mylist': result,

            }
        )



def stock_summary(request,slug):
    context = {'slug':slug}
    return render(request, 'home/stock_summary.html', context)

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
    try:

        kyc_obj = KYC.objects.filter(user_name__id=request.user.id)
    except:
        kyc_obj = []
    return render(request, 'change-password/kyc.html', {'kyc_obj': kyc_obj})


@login_required(login_url="my-login")
def repay(request):
     # Notification

    user_cpn_obj = ChitPaymentNotification.objects.filter(is_active=True,user_of_chit__id=request.user.id)
    user_cpn_obj_count = len(user_cpn_obj)
    return render(request,'home/repay.html', {'user': request.user,'user_cpn_obj_count':user_cpn_obj_count})


@login_required(login_url="my-login")
def history(request):
    cust_obj = CustomerChitPaymentDetails.objects.filter(customer_details__id=request.user.id)
    cust_obj_all = CustomerChitPaymentDetails.objects.filter(payment_status="Paid").order_by('-id')


    return render(request,'home/history.html', {'user': request.user,'cust_obj':cust_obj,"cust_obj_all":cust_obj_all})


def home(request):
    context = {}
    chit_det_obj_all = ChitDetails.objects.filter(chit_isactive=True)
    swing_obj_all = SwingTrade.objects.all()
    div_obj_all = DividendTrade.objects.all()
    hb_obj = HomeBanner.objects.all()
    slid_obj = Slider.objects.all()
    chit_act_obj = ChitActivities.objects.all()
    stock_news_obj = StockLastestNews.objects.all()
    chit_count_dict = {}
    for cdo in chit_det_obj_all:
        get_count = CustomerChitPlan.objects.filter(customer_chit_details=cdo)
        chit_count_dict[cdo.id] = str(len(get_count))
    # Notification

    user_cpn_obj = ChitPaymentNotification.objects.filter(is_active=True,user_of_chit__id=request.user.id)
    user_cpn_obj_count = len(user_cpn_obj)

    context = {'user_cpn_obj_count':user_cpn_obj_count,'chit_act_obj':chit_act_obj,'stock_news_obj':stock_news_obj,'slid_obj':slid_obj,'chit_det_obj_all':chit_det_obj_all,'chit_count_dict':chit_count_dict,'hb_obj':hb_obj}
    return render(request, 'home/home.html',context)


def download_csv_data(request,filename):
   # response content type
   response = HttpResponse(content_type='text/csv')

   #decide the file name
   response['Content-Disposition'] = 'attachment; filename="{}".format(filename)'

   writer = csv.writer(response, csv.excel)
   response.write(u'\ufeff'.encode('utf8'))

   #write the headers
   writer.writerow([
     smart_str(u"Date"),
     smart_str(u"Open"),
     smart_str(u"High"),
     smart_str(u"Low"),
     smart_str(u"Close"),
     smart_str(u"Adj Close"),
     smart_str(u"Volume"),


   ])

   #get data from database or from text file....
   events = event_services.get_events_by_year(year) #dummy function to fetch data
   for event in events:
     writer.writerow([
        smart_str(event.name),
        smart_str(event.start_date_time),
        smart_str(event.end_date_time),
        smart_str(event.notes),
     ])
   return response


from IPython.display import HTML

def get_csv_data_for_stocks(request):
    context = {}
    if request.method == 'POST':

        stock_name = request.POST.get('stock_name')
        data = yf.download(stock_name)
        context['data'] = data.to_html()

        msft = yf.Ticker(stock_name)
        context['msft'] = msft
        # get all stock info

        context['msft_info'] = msft.info
        # # get historical market data
        hist = msft.history(period="1mo")
        context['hist'] = hist.to_html()
    return render(request, 'home/get_csv_data_for_stocks.html',context)


def GoldenCrossverSignal(request):
        context = {}

        if request.method == "POST":
            path = request.FILES.get('upload')
            data_point = int(request.POST.get('data_point'))
            stock_name = request.POST.get('stock_name')
            y_stock_name = request.POST.get('y_stock_name')
            data = pd.read_csv(path, parse_dates=['Date'], index_col='Date')


            data['20_SMA'] = data.Close.rolling(window=20, min_periods=1).mean()
            data['50_SMA'] = data.Close.rolling(window=50, min_periods=1).mean()
            data['Signal'] = 0
            data['Signal'] = np.where(data['20_SMA'] > data['50_SMA'], 1, 0)
            data['Position'] = data.Signal.diff()
            plt.figure(figsize = (20,10))
            # plot close price, short-term and long-term moving averages
            #neg_data_point =
            data.iloc[-data_point:]['Close'].plot(color = 'k', label= 'Close Price')
            data.iloc[-data_point:]['20_SMA'].plot(color = 'b',label = '20-day SMA')
            data.iloc[-data_point:]['50_SMA'].plot(color = 'g', label = '50-day SMA')
            # plot ‘buy’ signals
            plt.plot(data.iloc[-data_point:][data.iloc[-data_point:]['Position'] == 1].index,
                     data.iloc[-data_point:]['20_SMA'][data.iloc[-data_point:]['Position'] == 1],
                     '^', markersize = 15, color = 'g', label = 'buy')
            # plot ‘sell’ signals
            plt.plot(data.iloc[-data_point:][data.iloc[-data_point:]['Position'] == -1].index,
                     data.iloc[-data_point:]['20_SMA'][data.iloc[-data_point:]['Position'] == -1],
                     'v', markersize = 15, color = 'r', label = 'sell')
            plt.ylabel('Price in Rupees', fontsize = 15 )
            plt.xlabel('Date', fontsize = 15 )
            plt.title(stock_name, fontsize = 20)
            plt.legend()
            plt.grid()
            plt.show()

            plt.tight_layout()

            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()

            graphic = base64.b64encode(image_png)
            graphic = graphic.decode('utf-8')
            context['graphic'] = graphic


            # reading when to buy and sell

            df_pos = data.iloc[-data_point:][(data.iloc[-data_point:]['Position'] == 1) | (data['Position'] == -1)].copy()
            df_pos['Position'] = df_pos['Position'].apply(lambda x: 'Buy' if x == 1 else 'Sell')


            context['data'] = df_pos.to_html(classes='table table-stripped')#[['Close', 'Position']].to_html(classes='table table-stripped')

            stock = yf.Ticker(y_stock_name)

            context['stock_price'] = stock.info
            context['y_stock_name'] = y_stock_name

        return render(request, 'home/graphic.html',context)


# https://www.makeuseof.com/stock-price-data-using-python/#:~:text=You%20need%20to%20have%20the%20ticker%20of%20the,market_price%20%3D%20ticker%5B%20%27regularMarketPrice%27%5D%20previous_close_price%20%3D%20ticker%5B%20%27regularMarketPreviousClose%27%5D
# TODO : deepak
def action_for_dividend():
    import yfinance as yf
    ticker = yf.Ticker('GOOGL').info
    market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']
    print('Ticker: GOOGL')
    print('Market Price:', market_price)
    print('Previous Close Price:', previous_close_price)

    ################
    # Importing the yfinance package
    import yfinance as yf

    # Set the start and end date
    start_date = '2020-01-01'
    end_date = '2022-01-01'

    # Set the ticker
    ticker = 'GOOGL'

    # Get the data
    data = yf.download(ticker, start_date, end_date)

    # Print the last 5 rows
    print(data.tail())



def upcoming_dividends(request):
    context = {}
    # web scriping
    # # Making a GET request
    # r = requests.get('https://stocks.zerodha.com/etfs/icici-prudential-nifty-100-etf-ICIC/events?type=dividends')
    # # Parsing the HTML
    # soup = BeautifulSoup(r.content, 'html.parser')
    # s = soup.find('div', class_='event-upcoming')
    # div_list = s.find_all()
    # str1 = ' '.join(str(e) for e in div_list)
    # str1 = str1.replace('Cash Dividend','Cash Dividend-')
    # context["dividend_list"] = str1[0:50000]

    context['up_coming'] = UpcomingDividends.objects.all()


    # so = requests.get('https://portal.tradebrains.in/corporateactions/Dividends')
    # # Parsing the HTML
    # so = BeautifulSoup(so.content, 'html.parser')
    # #so = so.find('table', class_='tl-dataTable')
    # # div_list = s.find_all()
    # # str1 = ' '.join(str(e) for e in div_list)
    # # str1 = str1.replace('Cash Dividend','Cash Dividend-')
    # context["so"] = so

    return render(request, 'home/upcoming_dividends.html',context)


@login_required(login_url="my-login")
def trading_community(request):
    context = {}
    chit_det_obj_all = ChitDetails.objects.filter(chit_isactive=True)
    swing_obj_all = SwingTrade.objects.all()
    div_obj_all = DividendTrade.objects.all()
    hb_obj = HomeBanner.objects.all()
    slid_obj = Slider.objects.all()
    chit_act_obj = ChitActivities.objects.all()
    stock_news_obj = StockLastestNews.objects.all()
    sub_flag = "FREE"
    try:
        sub_obj=Subscription.objects.get(user_name__id=request.user.id)
        sub_flag = sub_obj.sub_choice
    except:
        pass
    context
    chit_count_dict = {}
    for cdo in chit_det_obj_all:
        get_count = CustomerChitPlan.objects.filter(customer_chit_details=cdo)
        chit_count_dict[cdo.id] = str(len(get_count))
    page_obj = Post.objects.all()
    paginator = Paginator(page_obj, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    one_slide_obj = OneSlide.objects.all()
    context = {"one_slide_obj":one_slide_obj,"page_obj": page_obj, 'sub_flag':sub_flag,'swing_obj_all':swing_obj_all,"div_obj_all":div_obj_all,'chit_act_obj':chit_act_obj,'stock_news_obj':stock_news_obj,'slid_obj':slid_obj,'chit_det_obj_all':chit_det_obj_all,'chit_count_dict':chit_count_dict,'hb_obj':hb_obj}
    return render(request,'home/trading_community.html',context)


@login_required(login_url="my-login")
def dashboard(request):
    context = {}
    chit_det_obj = CustomerChitPlan.objects.filter(customer_name__id=request.user.id)
    admin_chit_det_obj = CustomerChitPlan.objects.filter(category="Management")
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
    user_count_obj = User.objects.all().count()
    ie_obj = IncomeExpenses.objects.all()
    income_list = []
    expense_list = []
    for ieo in ie_obj:
        income_list.append(ieo.income)
        expense_list.append(ieo.expense)

    income_total = 0
    expense_total = 0


    # Iterate each element in list
    # and add them in variable total
    for ele in range(0, len(income_list)):
        income_total = income_total + income_list[ele]
    for ele in range(0, len(expense_list)):
        expense_total = expense_total + expense_list[ele]



    subscriber_obj_count = UserSocialAuth.objects.all().count()

    lspin_obj = LotterySpinList.objects.latest('id')

    ccpd_obj = CustomerChitPaymentDetails.objects.all()
    statement_user_payment = CustomerChitPaymentDetails.objects.filter(customer_details__id=request.user.id)

    # Notification

    user_cpn_obj = ChitPaymentNotification.objects.filter(is_active=True,user_of_chit__id=request.user.id)
    user_cpn_obj_count = len(user_cpn_obj)

    # admin Notification
    cpn_obj = ChitPaymentNotification.objects.filter(is_active=True)

    context = {"statement_user_payment":statement_user_payment,
                "user_cpn_obj_count":user_cpn_obj_count,
                "user_cpn_obj":user_cpn_obj,
                "cpn_obj":cpn_obj,
                "admin_chit_det_obj":admin_chit_det_obj,
                "ccpd_obj":ccpd_obj,
                "lspin_obj":lspin_obj,
                "subscriber_obj_count":subscriber_obj_count,
                "income":income_total,
                "expense":expense_total,
                "user_count_obj":user_count_obj,
                "chit_det_obj_all_count":chit_det_obj_all.count(),
                'chit_det_obj':chit_det_obj,
                'chit_count_dict':chit_count_dict,
                'plan_details_dict':plan_details_dict,
                'chit_det_obj_all':chit_det_obj_all,
                'plan_details_dict_all':plan_details_dict_all}

    return render(request, 'home/index.html',context)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update_notify(request):
    print("update_notifyupdate_notifyupdate_notifyupdate_notifyupdate_notifyupdate_notifyupdate_notifyupdate_notifyupdate_notify")
    if request.method == 'POST':
        try:
             u_id = request.POST['not_id']
             # perform operations on the user name.
             cpn_obj = ChitPaymentNotification.objects.get(id=u_id)#=True)
             cpn_obj.is_active=False
             cpn_obj.save()
             return HttpResponse("Success!")
        except Exception as e:
            print ("EXception as eeeeeeeeeeeeeeeeeeeeeeeeeeeee",e)

    else:
       return HttpResponse("Request method is not a GET")








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


@login_required(login_url="my-login")
def profile(request):


    user_obj = User.objects.get(id=request.user.id)
    return render(request,'home/profile.html', {'user_obj':user_obj,"test":1})


