from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AboutusView(TemplateView):
    template_name = "pages/aboutus.html"


class ServicesView(TemplateView):
    template_name = "pages/services.html"


class FAQView(TemplateView):
    template_name = "pages/faq.html"


class PricingView(TemplateView):
    template_name = "pages/pricing.html"


class ContactusView(TemplateView):
    template_name = "pages/contactus.html"


class LegalView(TemplateView):
    template_name = "pages/legal.html"


class RegisterView(TemplateView):
    template_name = "pages/register.html"


class LoginView(TemplateView):
    template_name = "pages/login.html"
