from django.urls import path
from . import views


from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.home,name=""),
    path('chit_statement',views.chit_statement,name="chit_statement"),
    path('p2p_lending',views.p2p_lending,name="p2p_lending"),
    path('fin_literacy_tool',views.fin_literacy_tool,name="fin_literacy_tool"),

    path('about_us',views.about_us,name="about_us"),
    path('contact_us',views.contact_us,name="contact_us"),

    path('update_notify',views.update_notify,name="update_notify"),
    path('trading_community',views.trading_community,name="trading_community"),
    path('golden_cross_over_signal',views.GoldenCrossverSignal,name="GoldenCrossverSignal"),
    path('get_csv_data_for_stocks',views.get_csv_data_for_stocks,name="get_csv_data_for_stocks"),
    path('upcoming_dividends',views.upcoming_dividends,name="upcoming_dividends"),
    path('stock_summary/<slug>', views.stock_summary, name='stock_summary'),
    path('moving_avg_crossover',views.moving_avg_crossover,name="moving_avg_crossover"),


    path('my-login',views.my_login,name="my-login"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.my_logout,name="logout"),
    path('profile',views.profile,name="profile"),
    path('repay',views.repay,name="repay"),
    path('history',views.history,name="history"),
    path('receipt_print/<int:r_id>/',views.generate_pdf,name="generate_pdf"),
    path('get_chit_plan/<int:chit_id>/',views.get_chit_plan,name="get_chit_plan"),
    path('enroll_chit_plan/',views.enroll_chit_plan,name="enroll_chit_plan"),
    path('change_password/', views.change_password, name='change_password'),
    path('kyc/', views.kyc, name='kyc'),
    path('enroll_chit_page/', views.enroll_chit_page, name='enroll_chit_page'),







]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)