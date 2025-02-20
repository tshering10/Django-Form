from django.contrib import admin
from django.urls import path
from formApp import views


urlpatterns = [
    path('', views.home_view, name="home"),
    path('contact/', views.contact_view, name="contact"),
    path('contact/success', views.contact_success_view, name="success"),
]
