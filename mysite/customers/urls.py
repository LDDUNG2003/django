from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('personalInformation/', views.customer_info, name='customer_info'),
    path('logout/', views.logout, name='logout'),
]