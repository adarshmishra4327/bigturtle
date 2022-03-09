# General Imports
import json
import requests
import base64

# Rest Framework Imports
from rest_framework.parsers import (
    JSONParser,
    FormParser,
    MultiPartParser,
    FileUploadParser,
)
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

# Django Imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View, DetailView, ListView, TemplateView
from django.core.paginator import Paginator

# from django.conf import settings
# from django.core.cache.backends.base import DEFAULT_TIMEOUT
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache

# Application Imports
from listing.models import (
    Basic_Information,
    Gallery,
    Gallery_links,
    Location,
    Features,
    Details,
    Listing,
    Consolidated_tables,
    Register,
)
from listing.api.serializers import ListingSerializer
from listing.forms import (
    Basic_InformationForm,
    GalleryForm,
    LocationForm,
    DetailsForm,
    FeaturesForm,
    Filter_listingsForm,
    RegisterForm,
)
from listing.services import (
    get_home,
    process_gallerydata,
    get_home_details,
    get_home_filter,
    get_recent_listings,
    get_commercial,
    get_apartments,
    get_recent_123,
    get_plots,
    get_duplex,
    get_residential,
    get_villas,
    get_similar_listings,
    get_recent_propertytype,
)

URL_LISTING = "http://127.0.0.1:8000/api/listing/"
URL_GALLERY = "http://127.0.0.1:8000/gallery/"

# URL_LISTING = "http://www.propertyplusdecor.com/api/listing/"
# URL_GALLERY = "http://www.propertyplusdecor.com/gallery/"

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def convert_image_base64(filepath):

    with open(filepath, "rb") as img_file:

        b64_string = base64.b64encode(img_file.read()).decode("utf-8")
        return b64_string


class GetImageListView(View):
    def get(self, request, *args, **kwargs):

        inputdata = requests.get(URL_GALLERY)
        inputdata_json = inputdata.json()
        # l = len(inputdata_json)
        # image = inputdata_json[l - 1]["image"]
        # image2 = convert_image_base64()
        filter_form = Filter_listingsForm()

        return render(
            request, "listing/test.html", {"filter_form": filter_form},
        )


class GetHomeListView(APIView):

    template_name = "listing/listing_list2.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        home = []
        filter_form = Filter_listingsForm()
        datalength = Listing.objects.all().order_by("-id").count()

        for i in range(0, datalength):

            temp = (
                Listing.objects.all()
                .order_by("-id")[i : (i + 1)]
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "details__property_id",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )
            home.append(temp)

        print("home", home)

        return render(
            request,
            "listing/listing_list2.html",
            {
                "datalength": datalength,
                "home": home,
                "filter_form": filter_form,
            },
        )

    def post(self, request, *args, **kwargs):

        filter_listing = {}
        filter_form = Filter_listingsForm(request.POST)
        myDict = request.data.dict()
        print("myDict", myDict)

        if filter_form.is_valid():

            filter_listing["location"] = myDict["location"]
            filter_listing["status"] = myDict["status"]
            filter_listing["price_range"] = myDict["price_range"]
            filter_listing["beds"] = myDict["beds"]
            filter_listing["bathrooms"] = myDict["bathrooms"]
            filter_listing["prop_type"] = myDict["prop_type"]
            filter_listing["space"] = myDict["space"]

            home = get_home_filter(filter_listing)
            print("home", home)
            print("filter_form", filter_form)
            print("filter_listing", filter_listing)

            if len(home) > 0:

                print("filter_listing", filter_listing)

                return render(
                    request,
                    "listing/listing_list2.html",
                    {
                        "home": home,
                        "filter_form": filter_form,
                        "filter_listing": filter_listing,
                    },
                )
            else:
                message = "NO MATCH FOUND"
                return render(
                    request,
                    "listing/no_match_found.html",
                    {"message": message, "filter_form": filter_form},
                )


class GetHomeDetailView(APIView):

    template_name = "listing/listing-details2.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        pk = self.kwargs["pk"]
        register_form = RegisterForm()
        home = get_home_details(pk)
        home_similar_1, home_similar_2 = get_similar_listings(pk)
        home_recent = get_recent_propertytype(pk)
        len_similar_1 = len(home_similar_1)
        len_similar_2 = len(home_similar_2)
        len_home_recent = len(home_recent)
        print("pk", pk)
        print("home", home)
        print("home_similar_1", home_similar_1)
        print("home_similar_2", home_similar_2)
        print("home_recent", home_recent)
        print("len_home_recent", len_home_recent)

        return render(
            request,
            "listing/listing-details2.html",
            {
                "home": home,
                "pk": pk,
                "register_form": register_form,
                "home_similar_1": home_similar_1,
                "home_similar_2": home_similar_2,
                "home_recent": home_recent,
                "len_similar_1": len_similar_1,
                "len_similar_2": len_similar_2,
                "len_home_recent": len_home_recent,
            },
        )

    def post(self, request, pk):

        pk = self.kwargs["pk"]
        register_form = RegisterForm()
        home = get_home_details(pk)
        home_similar_1, home_similar_2 = get_similar_listings(pk)
        home_recent = get_recent_propertytype(pk)
        len_similar_1 = len(home_similar_1)
        len_similar_2 = len(home_similar_2)
        len_home_recent = len(home_recent)

        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # Save Register Form
            register_form.save()
            message = "Thanks for Registering. Will call you shortly"

            return render(
                request,
                "listing/listing-details2.html",
                {
                    "message": message,
                    "home": home,
                    "pk": pk,
                    "home_similar_1": home_similar_1,
                    "home_similar_2": home_similar_2,
                    "home_recent": home_recent,
                    "len_similar_1": len_similar_1,
                    "len_similar_2": len_similar_2,
                    "len_home_recent": len_home_recent,
                },
            )


class HomeOriginalView(APIView):
    template_name = "listing/home_original.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "listing/home2.html",
            {
                
            },
        )


class HomePageListView(APIView):
    template_name = "listing/home2.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        commercial_count = 0
        residential_count = 0
        apartment_count = 0
        duplex_count = 0
        villa_count = 0
        plots_count = 0
        filter_form = Filter_listingsForm()

        lastone, lastsecondone, lastthirdone = get_recent_123()

        commercial_count = Listing.objects.filter(
                details__propertytype="COMMERCIAL"
            ).count()

        residential_count = Listing.objects.filter(
                details__propertytype="RESIDENTIAL"
            ).count()

        apartment_count = Listing.objects.filter(
                details__propertytype="APARTMENT"
            ).count()

        plots_count = Listing.objects.filter(
                details__propertytype="PLOTS"
            ).count()

        villa_count = Listing.objects.filter(
                details__propertytype="VILLA"
            ).count()

        duplex_count = Listing.objects.filter(
                details__propertytype="DUPLEX"
            ).count()

        return render(
            request,
            "listing/home2.html",
            {
                "lastone": lastone,
                "lastsecondone": lastsecondone,
                "lastthirdone": lastthirdone,
                "filter_form": filter_form,
                "commercial_count": commercial_count,
                "residential_count": residential_count,
                "apartment_count": apartment_count,
                "plots_count": plots_count,
                "villa_count": villa_count,
                "duplex_count": duplex_count,
            },
        )

    def post(self, request, *args, **kwargs):

        filter_listing = {}
        myDict = request.data.dict()
        print("myDict", myDict)

        # if filter_form.is_valid():

        filter_listing["location"] = myDict["location"]
        filter_listing["status"] = myDict["status"]
        filter_listing["price_range"] = myDict["price"]
        filter_listing["builder"] = myDict["builder"]
        filter_listing["sort_by"] = myDict["sort"]
        filter_listing["prop_type"] = myDict["type"]

        filter_form = Filter_listingsForm(filter_listing)
        property_type = filter_listing["prop_type"]
        print("property_type", property_type)
        print("filter_listing", filter_listing)

        home = get_home_filter(filter_listing)
        print("home", home)

        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 9 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:

            print("filter_listing", filter_listing)

            return render(
                request,
                "listing/listing_list4.html",
                {
                    "home": home,
                    "filter_form": filter_form,
                    "filter_listing": filter_listing,
                    "property_type": property_type,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "message": message,
                    "filter_form": filter_form,
                    "property_type": property_type,
                },
            )


class GetCommercialListView(APIView):

    template_name = "listing/listing_list3.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        home = []
        filter_form = Filter_listingsForm()
        home = get_commercial()
        print("home", home)
        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 9 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)
        property_type = "Commercial"

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:
            return render(
                request,
                "listing/listing_list3.html",
                {
                    "property_type": property_type,
                    "home": home,
                    "filter_form": filter_form,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            property_type = "Commercial"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "property_type": property_type,
                    "message": message,
                    "filter_form": filter_form,
                },
            )

    def post(self, request, *args, **kwargs):

        filter_listing = {}
        myDict = request.data.dict()
        print("myDict", myDict)

        # if filter_form.is_valid():

        filter_listing["location"] = myDict["location"]
        filter_listing["status"] = myDict["status"]
        filter_listing["price_range"] = myDict["price"]
        filter_listing["builder"] = myDict["builder"]
        filter_listing["sort_by"] = myDict["sort"]
        filter_listing["prop_type"] = myDict["type"]

        filter_form = Filter_listingsForm(filter_listing)
        if filter_listing["prop_type"]:

            property_type = filter_listing["prop_type"]
        else:
            property_type = "Commercial"

        print("property_type", property_type)
        print("filter_listing", filter_listing)

        home = get_home_filter(filter_listing)

        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 9 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:

            print("filter_listing", filter_listing)

            return render(
                request,
                "listing/listing_list4.html",
                {
                    "home": home,
                    "filter_form": filter_form,
                    "filter_listing": filter_listing,
                    "property_type": property_type,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "message": message,
                    "filter_form": filter_form,
                    "property_type": property_type,
                },
            )


class GetApartmentsListView(APIView):

    template_name = "listing/listing_list3.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        home = []
        filter_form = Filter_listingsForm()
        home = get_apartments()
        print("home", home)
        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 9 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)
        property_type = "Apartments"

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        # print("page", page)
        # print("pages", pages)
        # print("page_minus", page_minus)
        # print("page_plus", page_plus)

        if len(home) > 0:
            return render(
                request,
                "listing/listing_list3.html",
                {
                    "property_type": property_type,
                    "home": home,
                    "filter_form": filter_form,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            property_type = "Apartments"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "property_type": property_type,
                    "message": message,
                    "filter_form": filter_form,
                },
            )

    def post(self, request, *args, **kwargs):

        filter_listing = {}
        myDict = request.data.dict()
        print("myDict", myDict)

        # if filter_form.is_valid():

        filter_listing["location"] = myDict["location"]
        filter_listing["status"] = myDict["status"]
        filter_listing["price_range"] = myDict["price"]
        filter_listing["builder"] = myDict["builder"]
        filter_listing["sort_by"] = myDict["sort"]
        filter_listing["prop_type"] = myDict["type"]

        filter_form = Filter_listingsForm(filter_listing)
        if filter_listing["prop_type"]:

            property_type = filter_listing["prop_type"]
        else:
            property_type = "Apartments"

        print("property_type", property_type)
        print("filter_listing", filter_listing)

        home = get_home_filter(filter_listing)

        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 9 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:

            print("filter_listing", filter_listing)

            return render(
                request,
                "listing/listing_list4.html",
                {
                    "home": home,
                    "filter_form": filter_form,
                    "filter_listing": filter_listing,
                    "property_type": property_type,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "message": message,
                    "filter_form": filter_form,
                    "property_type": property_type,
                },
            )


class GetVillasListView(APIView):

    template_name = "listing/listing_list3.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        home = []
        filter_form = Filter_listingsForm()
        home = get_villas()
        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 2 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)
        property_type = "Villas"

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:
            return render(
                request,
                "listing/listing_list3.html",
                {
                    "property_type": property_type,
                    "home": home,
                    "filter_form": filter_form,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            property_type = "Villas"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "property_type": property_type,
                    "message": message,
                    "filter_form": filter_form,
                },
            )

    def post(self, request, *args, **kwargs):

        filter_listing = {}
        myDict = request.data.dict()
        print("myDict", myDict)

        # if filter_form.is_valid():

        filter_listing["location"] = myDict["location"]
        filter_listing["status"] = myDict["status"]
        filter_listing["price_range"] = myDict["price"]
        filter_listing["builder"] = myDict["builder"]
        filter_listing["sort_by"] = myDict["sort"]
        filter_listing["prop_type"] = myDict["type"]

        filter_form = Filter_listingsForm(filter_listing)
        if filter_listing["prop_type"]:

            property_type = filter_listing["prop_type"]
        else:
            property_type = "Villas"

        print("property_type", property_type)
        print("filter_listing", filter_listing)

        home = get_home_filter(filter_listing)

        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 9 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:

            print("filter_listing", filter_listing)

            return render(
                request,
                "listing/listing_list4.html",
                {
                    "home": home,
                    "filter_form": filter_form,
                    "filter_listing": filter_listing,
                    "property_type": property_type,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "message": message,
                    "filter_form": filter_form,
                    "property_type": property_type,
                },
            )


class GetResidentialListView(APIView):

    template_name = "listing/listing_list3.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        home = []
        filter_form = Filter_listingsForm()
        home = get_residential()
        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 2 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)
        property_type = "Residential"

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:
            return render(
                request,
                "listing/listing_list3.html",
                {
                    "property_type": property_type,
                    "home": home,
                    "filter_form": filter_form,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            property_type = "Residential"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "property_type": property_type,
                    "message": message,
                    "filter_form": filter_form,
                },
            )

    def post(self, request, *args, **kwargs):

        filter_listing = {}
        myDict = request.data.dict()
        print("myDict", myDict)

        # if filter_form.is_valid():

        filter_listing["location"] = myDict["location"]
        filter_listing["status"] = myDict["status"]
        filter_listing["price_range"] = myDict["price"]
        filter_listing["builder"] = myDict["builder"]
        filter_listing["sort_by"] = myDict["sort"]
        filter_listing["prop_type"] = myDict["type"]

        filter_form = Filter_listingsForm(filter_listing)
        if filter_listing["prop_type"]:

            property_type = filter_listing["prop_type"]
        else:
            property_type = "Residential"

        print("property_type", property_type)
        print("filter_listing", filter_listing)

        home = get_home_filter(filter_listing)

        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 9 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:

            print("filter_listing", filter_listing)

            return render(
                request,
                "listing/listing_list4.html",
                {
                    "home": home,
                    "filter_form": filter_form,
                    "filter_listing": filter_listing,
                    "property_type": property_type,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "message": message,
                    "filter_form": filter_form,
                    "property_type": property_type,
                },
            )


class GetDuplexListView(APIView):

    template_name = "listing/listing_list3.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        home = []
        filter_form = Filter_listingsForm()
        home = get_duplex()
        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 2 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)
        property_type = "Duplex"

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:
            return render(
                request,
                "listing/listing_list3.html",
                {
                    "property_type": property_type,
                    "home": home,
                    "filter_form": filter_form,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            property_type = "Duplex"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "property_type": property_type,
                    "message": message,
                    "filter_form": filter_form,
                },
            )

    def post(self, request, *args, **kwargs):

        filter_listing = {}
        myDict = request.data.dict()
        print("myDict", myDict)

        # if filter_form.is_valid():

        filter_listing["location"] = myDict["location"]
        filter_listing["status"] = myDict["status"]
        filter_listing["price_range"] = myDict["price"]
        filter_listing["builder"] = myDict["builder"]
        filter_listing["sort_by"] = myDict["sort"]
        filter_listing["prop_type"] = myDict["type"]

        filter_form = Filter_listingsForm(filter_listing)
        if filter_listing["prop_type"]:

            property_type = filter_listing["prop_type"]
        else:
            property_type = "Duplex"

        print("property_type", property_type)
        print("filter_listing", filter_listing)

        home = get_home_filter(filter_listing)

        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 9 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:

            print("filter_listing", filter_listing)

            return render(
                request,
                "listing/listing_list4.html",
                {
                    "home": home,
                    "filter_form": filter_form,
                    "filter_listing": filter_listing,
                    "property_type": property_type,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "message": message,
                    "filter_form": filter_form,
                    "property_type": property_type,
                },
            )


class GetPlotsListView(APIView):

    template_name = "listing/listing_list3.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        home = []
        filter_form = Filter_listingsForm()
        home = get_plots()
        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 2 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)
        property_type = "Plots"

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:
            return render(
                request,
                "listing/listing_list3.html",
                {
                    "property_type": property_type,
                    "home": home,
                    "filter_form": filter_form,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                    "page": page,
                },
            )
        else:
            message = "NO MATCH FOUND"
            property_type = "Plots"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "property_type": property_type,
                    "message": message,
                    "filter_form": filter_form,
                },
            )

    def post(self, request, *args, **kwargs):

        filter_listing = {}
        myDict = request.data.dict()
        print("myDict", myDict)

        # if filter_form.is_valid():

        filter_listing["location"] = myDict["location"]
        filter_listing["status"] = myDict["status"]
        filter_listing["price_range"] = myDict["price"]
        filter_listing["builder"] = myDict["builder"]
        filter_listing["sort_by"] = myDict["sort"]
        filter_listing["prop_type"] = myDict["type"]

        filter_form = Filter_listingsForm(filter_listing)
        if filter_listing["prop_type"]:

            property_type = filter_listing["prop_type"]
        else:
            property_type = "Plots"

        print("property_type", property_type)
        print("filter_listing", filter_listing)

        home = get_home_filter(filter_listing)

        l = len(home)
        if l < 9:
            page_plus = 0
            page_minus = 0
            pages = 1

        elif l > 9:
            if l % 9 == 0:
                pages = int(l / 9)

            elif l % 9 > 0:
                pages = int(l / 9) + 1

        # 9 items per page
        paginator = Paginator(home, 9)
        page = request.GET.get("page")
        home = paginator.get_page(page)

        if pages > 1:

            page_minus = int(page) - 1
            page_plus = pages - int(page)

        if len(home) > 0:

            print("filter_listing", filter_listing)

            return render(
                request,
                "listing/listing_list4.html",
                {
                    "home": home,
                    "filter_form": filter_form,
                    "filter_listing": filter_listing,
                    "property_type": property_type,
                    "page_minus": page_minus,
                    "page_plus": page_plus,
                },
            )
        else:
            message = "NO MATCH FOUND"
            return render(
                request,
                "listing/no_match_found.html",
                {
                    "message": message,
                    "filter_form": filter_form,
                    "property_type": property_type,
                },
            )


class Submit_listing(APIView):

    template_name = "listing/submit-listing.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request):

        basic_form = Basic_InformationForm()
        gallery_form = GalleryForm()
        location_form = LocationForm()
        feature_form = FeaturesForm()
        detail_form = DetailsForm()

        return render(
            request,
            "listing/submit-listing.html",
            {
                "basic_form": basic_form,
                "gallery_form": gallery_form,
                "location_form": location_form,
                "feature_form": feature_form,
                "detail_form": detail_form,
            },
        )

    def post(self, request):
        b = {}
        g = {}
        l = {}
        f = {}
        d = {}
        property_DATA = {}
        basic = []
        gallery = []
        location = []
        features = []
        details = []

        basic_form = Basic_InformationForm(request.POST)
        gallery_form = GalleryForm(request.POST, request.FILES)
        location_form = LocationForm(request.POST)
        feature_form = FeaturesForm(request.POST)
        detail_form = DetailsForm(request.POST)
        # print("request.data", request.data)
        myDict = request.data.dict()

        if (
            basic_form.is_valid()
            and gallery_form.is_valid()
            and location_form.is_valid()
            and feature_form.is_valid()
            and detail_form.is_valid()
        ):

            # Basic Information
            b["project_area"] = myDict["project_area"]
            b["propertytype"] = myDict["propertytype"]
            b["total_units"] = myDict["total_units"]
            b["available_units"] = myDict["available_units"]
            b["total_no_of_towers"] = myDict["total_no_of_towers"]
            b["total_no_of_floors"] = myDict["total_no_of_floors"]
            b["approved_by"] = myDict["approved_by"]
            b["launch_year"] = myDict["launch_year"]
            b["commencement_certificate"] = myDict["commencement_certificate"]

            # Gallery
            property_name = myDict["name"]
            property_id = myDict["property_id"]

            # Save Gallery Form
            gallery_form.save()

            g = process_gallerydata(property_name, property_id, URL_GALLERY)

            # Location
            l["location"] = myDict["location"]
            l["State"] = myDict["State"]
            l["City"] = myDict["City"]
            l["Longitude"] = myDict["Longitude"]
            l["Latitude"] = myDict["Latitude"]

            # Features
            f["pet_friendly"] = myDict["pet_friendly"]
            f["furnished"] = myDict["furnished"]
            f["cooling"] = myDict["cooling"]
            f["parking"] = myDict["parking"]
            f["mailbox"] = myDict["mailbox"]
            f["city_view"] = myDict["city_view"]
            f["yoga_room"] = myDict["yoga_room"]
            f["swimming_pool"] = myDict["swimming_pool"]
            f["badminton_court"] = myDict["badminton_court"]
            f["squash_court"] = myDict["squash_court"]
            f["snooker_table"] = myDict["snooker_table"]
            f["basketball_court"] = myDict["basketball_court"]
            f["multipurpose_court"] = myDict["multipurpose_court"]
            f["outdoor_gym"] = myDict["outdoor_gym"]
            f["amphitheatre"] = myDict["amphitheatre"]
            f["childs_playarea"] = myDict["childs_playarea"]
            f["srcitizen_area"] = myDict["srcitizen_area"]
            f["cycling_track"] = myDict["cycling_track"]

            # Edit Video Link
            video = myDict["video"]
            video_edited = video.split("=")[1]
            video_link = "https://www.youtube.com/embed/" + video_edited

            # Details
            d["property_id"] = myDict["property_id"]
            d["builder_name"] = myDict["builder_name"]
            d["sold_projects"] = myDict["sold_projects"]
            d["completed_projects"] = myDict["completed_projects"]
            d["ongoing_projects"] = myDict["ongoing_projects"]
            d["name"] = myDict["name"]
            d["status"] = myDict["status"]
            d["propertytype"] = myDict["propertytype"]
            d["price"] = myDict["price"]
            temp = myDict["price"]
            if int(temp) > 100000 and int(temp) < 10000000:

                d["converted_price"] = round(
                    float(int(myDict["price"]) / 100000), 2
                )
                d["price_withunit"] = str(d["converted_price"]) + " " + "Lakhs"
            elif int(temp) > 10000000:
                d["converted_price"] = round(
                    float(int(myDict["price"]) / 10000000), 2
                )
                d["price_withunit"] = str(d["converted_price"]) + " " + "Cr"
            d["mortgage"] = 0.8 * int(myDict["price"])
            d["description"] = myDict["description"]
            d["space"] = myDict["space"]
            d["video"] = video_link
            d["beds"] = myDict["beds"]
            d["bathrooms"] = myDict["bathrooms"]
            d["condition"] = myDict["condition"]
            d["year_built"] = myDict["year_built"]

            # Complete Property Data >> POSTING to API
            basic.append(b)
            gallery.append(g)
            location.append(l)
            features.append(f)
            details.append(d)
            property_DATA["gallery_links"] = gallery
            property_DATA["basic"] = basic
            property_DATA["location"] = location
            property_DATA["features"] = features
            property_DATA["details"] = details
            # print("property_DATA", property_DATA)

            json_data = json.dumps(property_DATA, indent=4)
            print("json_data", json_data)
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            r = requests.post(URL_LISTING, data=json_data, headers=headers)

            return render(
                request,
                "listing/submit-listing.html",
                {
                    "basic_form": Basic_InformationForm(
                        instance=Basic_Information()
                    ),
                    "gallery_form": GalleryForm(instance=Gallery()),
                    "location_form": LocationForm(instance=Location()),
                    "feature_form": FeaturesForm(instance=Features()),
                    "detail_form": DetailsForm(instance=Details()),
                },
            )

        else:

            basic_form = Basic_InformationForm(instance=Basic_Information())
            gallery_form = GalleryForm(instance=Gallery())
            location_form = LocationForm(instance=Location())
            feature_form = FeaturesForm(instance=Features())
            detail_form = DetailsForm(instance=Details())

            return render(
                request,
                "listing/submit-listing.html",
                {
                    "basic_form": basic_form,
                    "gallery_form": gallery_form,
                    "location_form": location_form,
                    "feature_form": feature_form,
                    "detail_form": detail_form,
                },
            )
