from django.shortcuts import render

from django.views.generic import View
from .models import *
# Create your views here.
from django.shortcuts import render
from datetime import datetime

def your_view(request):
    current_datetime = datetime.now()
    sale_end_date = datetime(2023, 12, 31, 23, 59, 59)  # Replace with your actual sale end date

    context = {
        'current_datetime': current_datetime,
        'sale_end_date': sale_end_date,
    }
    return render(request, 'index.html', context)
def checkout(request):
    return render(request, 'checkout.html')
def login(request):
    return render(request, 'login.html')
class BaseView(View):
    views= {}
    views['logos'] = Logo.objects.all()
    views['featuredcategories'] = Featuredcategory.objects.all()
    views['siteinformations'] =Siteinformation.objects.all()
    views['awesomes'] = Awesome.objects.all()
    views['sliders'] = Slider.objects.all()
    views['clientlogos'] = Clientlogo.objects.all()
class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['sliders'] = Slider.objects.all()

        self.views['weeklysales'] = Weeklysale.objects.all()
        self.views['bestsellers'] = Bestseller.objects.all()
        self.views['subscriptions'] = Subscription.objects.all()


        return render(request,'index.html',self.views)

