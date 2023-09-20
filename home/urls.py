from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("contact/", views.contact, name="contact"),
    path("getdata/", views.getdata, name="getdata"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
]
