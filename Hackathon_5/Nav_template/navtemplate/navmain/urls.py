from django.urls import path
from . import views


urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customers, name='customers'),
    path('incidents/', views.incidents, name='incidents'),
    path('about/', views.about, name='about'),

]