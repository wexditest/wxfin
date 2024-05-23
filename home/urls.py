from django.urls import path
from . import views


from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.home,name=""),
    path('trading_community',views.trading_community,name="trading_community"),
    path('golden_cross_over_signal',views.GoldenCrossverSignal,name="GoldenCrossverSignal"),
    path('get_csv_data_for_stocks',views.get_csv_data_for_stocks,name="get_csv_data_for_stocks"),
    path('upcoming_dividends',views.upcoming_dividends,name="upcoming_dividends"),
    path('stock_summary/<slug>', views.stock_summary, name='stock_summary'),

    path('my-login',views.my_login,name="my-login"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.my_logout,name="logout"),
    path('profile',views.MyProfile.as_view(),name="profile"),
    path('repay',views.repay,name="repay"),
    path('history',views.history,name="history"),
    path('receipt_print/<int:r_id>/',views.generate_pdf,name="generate_pdf"),
    path('get_chit_plan/<int:chit_id>/',views.get_chit_plan,name="get_chit_plan"),
    path('enroll_chit_plan/',views.enroll_chit_plan,name="enroll_chit_plan"),
    path('change_password/', views.change_password, name='change_password'),
    path('kyc/', views.kyc, name='kyc'),
    path('enroll_chit_page/', views.enroll_chit_page, name='enroll_chit_page'),







]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)