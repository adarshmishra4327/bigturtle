"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from pages.views import (
    AboutusView,
    ContactusView,
    FAQView,
    LegalView,
    LoginView,
    PricingView,
    RegisterView,
    ServicesView,
)
from blog.views import PostListView, PostDetailView
from listing.views import (
    Submit_listing,
    GetHomeListView,
    GetHomeDetailView,
    GetImageListView,
    HomePageListView,
    GetCommercialListView,
    GetApartmentsListView,
    GetVillasListView,
    GetPlotsListView,
    GetDuplexListView,
    GetResidentialListView,
    HomeOriginalView
)
from listing.api.views import GalleryListView
from interiors.api.views import PortfolioGalleryView
from interiors.views import (
    InteriorsListView,
    DesignsListing,
    PortfolioListing,
    BookFreeConsultation,
    PreConsultation,
    CustomerReview,
    PortfoliosView,
    DesignerIntroView,
    DesignsView,
    KitchenDesignsView,
    LivingroomDesignsView,
    BedroomDesignsView,
    BathroomDesignsView,
    KidsroomDesignsView,
)
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView


urlpatterns = [
    ############################################################################################
    ###############################  STATIC LINKS ##############################################
    ############################################################################################
    path("admin/", admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path("aboutus/", AboutusView.as_view(), name="aboutus"),
    # path("aboutus/", AboutusView.as_view(), name="aboutus"),
    path("services/", ServicesView.as_view(), name="services"),
    path("faq/", FAQView.as_view(), name="faq"),
    path("pricing/", PricingView.as_view(), name="pricing"),
    path("contactus/", ContactusView.as_view(), name="contactus"),
    path("legal/", LegalView.as_view(), name="legal"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("blog/<pk>/", PostDetailView.as_view(), name="blogs-detail"),
    path("blogs/", PostListView.as_view(), name="blogs"),

    ############################################################################################
    ###############################  PROPERTY LINKS ############################################
    ############################################################################################
    # path("images/", ImageListView.as_view(), name="image-listing"),
    # path("properties/", GetHomeListView.as_view(), name="properties"),
    path("submit-listing/", Submit_listing.as_view(), name="submit-listing"),
    path('', include('mainapp.urls')),
    path("property/login/", TemplateView.as_view(template_name='propertylogin.html')),
    path("property/register/",
         TemplateView.as_view(template_name='propertyregister.html')),
    path("interior/register/",
         TemplateView.as_view(template_name='interiorregister.html')),
    path("interior/login/", TemplateView.as_view(template_name='interiorlogin.html')),
    path("properties/", HomePageListView.as_view(), name="properties"),
    path(
        "properties/<pk>",
        GetHomeDetailView.as_view(),
        name="properties-detail",
    ),
    path(
        "properties/villas/",
        GetVillasListView.as_view(),
        name="properties-villas",
    ),
    path(
        "properties/residential/",
        GetResidentialListView.as_view(),
        name="properties-residential",
    ),
    path(
        "properties/duplex/",
        GetDuplexListView.as_view(),
        name="properties-duplex",
    ),
    path(
        "properties/plots/",
        GetPlotsListView.as_view(),
        name="properties-plots",
    ),
    path(
        "api/listing/",
        include(("listing.api.urls", "listing"), namespace="listing-api"),
    ),
    path(
        "properties/commercial/",
        GetCommercialListView.as_view(),
        name="properties-commercial",
    ),
    path(
        "properties/apartments/",
        GetApartmentsListView.as_view(),
        name="properties-apartments",
    ),
    path("gallery/", PortfolioGalleryView.as_view(), name="gallery"),

    ############################################################################################
    ###############################  INTERIORS URLS ###########################################
    ############################################################################################
    path("interiors/", InteriorsListView.as_view(), name="interiors"),
    path("interiors/portfolios/", PortfoliosView.as_view(), name="portfolios"),
    path("interiors/designer/<pk>", DesignerIntroView.as_view(), name="designerid"),
    path("interiors/designs/", DesignsView.as_view(), name="designs"),

    #################################### INTERIOR DESIGNS ##############################################
    path("interiors/kitchendesigns/",
         KitchenDesignsView.as_view(), name="kitchendesigns"),
    path("interiors/livingroomdesigns/",
         LivingroomDesignsView.as_view(), name="livingroomdesigns"),
    path("interiors/bedroomdesigns/",
         BedroomDesignsView.as_view(), name="bedroomdesigns"),
    path("interiors/bathroomdesigns/",
         BathroomDesignsView.as_view(), name="bathroomdesigns"),
    path("interiors/kidsroomdesigns/",
         KidsroomDesignsView.as_view(), name="kidsroomdesigns"),

    #################################### INTERIOR FORMS ##############################################
    path("listingdesign/", DesignsListing.as_view(), name="listingdesign"),
    path("listingportfolio/", PortfolioListing.as_view(), name="listingportfolio",),
    path(
        "bookfreeconsultation/",
        BookFreeConsultation.as_view(),
        name="bookfreeconsultation",
    ),
    path(
        "preconsultationform/",
        PreConsultation.as_view(),
        name="preconsultation",
    ),
    path("customerreview/", CustomerReview.as_view(), name="customerreview",),

    #################################### INTERIORS API ##############################################
    path(
        "api/interiors/",
        include(
            ("interiors.api.urls", "interiors"), namespace="interiors-api"
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
