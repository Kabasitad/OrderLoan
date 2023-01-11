from django.urls import path

from . import views

urlpatterns = [
    path('', views.loan, name='Order Loan'),
    path("home/", views.home, name="home"),
    path("added/", views.added, name="Added new client"),
    
]