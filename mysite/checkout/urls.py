from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns =[
    path('checkout/',views.viewCheckout,name='index')
]