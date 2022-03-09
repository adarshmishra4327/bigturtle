from django.urls import path, include
from django.urls.resolvers import URLPattern
from mainapp import views

  
urlpatterns = [

    path('', views.index),
    path("propertylisting/", views.propertylisting),
    path("addproperty/", views.addproperty),
    path("searchproperty/", views.searchproperty),
    path("detailproperty/", views.detailproperty),

]
