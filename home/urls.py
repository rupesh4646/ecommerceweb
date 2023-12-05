from django.urls import  path
from .views import *
urlpatterns = [
    path("", HomeView.as_view(), name = 'home'),
    path('checkout/', checkout, name='checkout'),
    path('login/', checkout, name='login'),
]
