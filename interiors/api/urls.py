from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import (Customer_feedbackView, DesignsView, BookfreeconsultationView, PortfolioView, PortfolioGalleryView, DesignGalleryView)


urlpatterns = [
    # path("", InteriorView.as_view(), name="interiorlistcreate"),
    path("designgallery/", DesignGalleryView.as_view(), name="Designslistcreate"),
    path("designs/", DesignsView.as_view(), name="Designslistcreate"),
    path(
        "customers/",
        Customer_feedbackView.as_view(),
        name="customerlistcreate",
    ),
    path("bookfreeconsultation/", BookfreeconsultationView.as_view(), name="apibookfclistcreate"),
    path("portfolio/", PortfolioView.as_view(), name="apiportfoliolistcreate"),
    path("gallery/", PortfolioGalleryView.as_view(), name="apiportfoliolistcreate"),
]
