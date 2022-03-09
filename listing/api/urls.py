from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import ListingView, RegisterView


urlpatterns = [
    path("", ListingView.as_view(), name="listcreate"),
    path("register/", RegisterView.as_view(), name="registercreate"),
]
