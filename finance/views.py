from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home/trading_community.html"