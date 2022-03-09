# General Imports
import requests
import json
import math
import random

# Django Imports
from django.shortcuts import render
from django.views.generic import View, DetailView, ListView, TemplateView
from django.shortcuts import redirect

# Rest Framework Imports
from rest_framework.parsers import (
    JSONParser,
    FormParser,
    MultiPartParser,
    FileUploadParser,
)
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

# Application Imports
from interiors.models import Designs, PortfolioBasic, PortfolioGallery, PortfolioGalleryLinks, City, DesignGallery
from interiors.forms import (
    Customer_ReviewForm,
    DesignGalleryForm,
    Online_ConsultationForm,
    PortfolioGalleryForm,
    Pre_ConsultationForm,
)
from interiors.services import cities, designers, designs, filterdesigns, portfolios
from interiors.api.serializers import CitySerializer, DesignsSerializer


URL_BOOKFREECONSULTATION = "http://127.0.0.1:8000/api/interiors/bookfreeconsultation/"
URL_PORTFOLIO = "http://127.0.0.1:8000/api/interiors/portfolio/"
URL_GALLERY = "http://127.0.0.1:8000/api/interiors/gallery/"
BASE_URL = "http://127.0.0.1:8000/"
URL_DESIGN = "http://127.0.0.1:8000/api/interiors/designs/"

# URL_BOOKFREECONSULTATION = "http://propertyplusdecor.com/api/interiors/bookfreeconsultation/"
# URL_PORTFOLIO = "http://propertyplusdecor.com/api/interiors/portfolio/"
# URL_GALLERY = "http://propertyplusdecor.com/api/interiors/gallery/"
# BASE_URL = "http://propertyplusdecor.com/"
# URL_DESIGN = "http://propertyplusdecor.com/api/interiors/designs/"


def generate_Portfolio_id():

    # for alpha numeric OTP
    corpus = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    generate_OTP = ""
    size = 8
    length = len(corpus)
    for i in range(size):
        generate_OTP += corpus[math.floor(random.random() * length)]

    Portfolio_id = "PORT" + generate_OTP

    return Portfolio_id


def generate_Designer_id():

    # for alpha numeric OTP
    corpus = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    generate_OTP = ""
    size = 6
    length = len(corpus)
    for i in range(size):
        generate_OTP += corpus[math.floor(random.random() * length)]

    Designer_id = generate_OTP

    return Designer_id


def randomid():

    # for alpha numeric OTP
    corpus = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    generate_OTP = ""
    size = 8
    length = len(corpus)
    for i in range(size):
        generate_OTP += corpus[math.floor(random.random() * length)]

    random_id = generate_OTP

    return random_id


class KitchenDesignsView(APIView):

    template_name = "listing/designs.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        CITY = cities()
        DESIGNER = designers()
        designtype = "MODULAR KITCHEN"
        DESIGNS = filterdesigns(designtype)

        if DESIGNS:

            return render(request, "listing/designs.html", {"DESIGNER": DESIGNER, "CITY": CITY, "DESIGNS": DESIGNS})

        else:

            CITY = cities()
            DESIGNER = designers()

            MESSAGE = "NO MATCH FOUND"
            return render(request, "listing/designs_nomatch.html", {"DESIGNER": DESIGNER, "CITY": CITY, "MESSAGE": MESSAGE})


class LivingroomDesignsView(APIView):

    template_name = "listing/designs.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        CITY = cities()
        DESIGNER = designers()
        designtype = "LIVING ROOM"
        DESIGNS = filterdesigns(designtype)

        if DESIGNS:

            return render(request, "listing/designs.html", {"DESIGNER": DESIGNER, "CITY": CITY, "DESIGNS": DESIGNS})

        else:

            CITY = cities()
            DESIGNER = designers()

            MESSAGE = "NO MATCH FOUND"
            return render(request, "listing/designs_nomatch.html", {"DESIGNER": DESIGNER, "CITY": CITY, "MESSAGE": MESSAGE})


class BedroomDesignsView(APIView):

    template_name = "listing/designs.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        CITY = cities()
        DESIGNER = designers()
        designtype = "BED ROOM"
        DESIGNS = filterdesigns(designtype)

        if DESIGNS:

            return render(request, "listing/designs.html", {"DESIGNER": DESIGNER, "CITY": CITY, "DESIGNS": DESIGNS})

        else:

            CITY = cities()
            DESIGNER = designers()

            MESSAGE = "NO MATCH FOUND"
            return render(request, "listing/designs_nomatch.html", {"DESIGNER": DESIGNER, "CITY": CITY, "MESSAGE": MESSAGE})


class BathroomDesignsView(APIView):

    template_name = "listing/designs.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        CITY = cities()
        DESIGNER = designers()
        designtype = "BATHROOM"
        DESIGNS = filterdesigns(designtype)

        if DESIGNS:

            return render(request, "listing/designs.html", {"DESIGNER": DESIGNER, "CITY": CITY, "DESIGNS": DESIGNS})

        else:

            CITY = cities()
            DESIGNER = designers()

            MESSAGE = "NO MATCH FOUND"
            return render(request, "listing/designs_nomatch.html", {"DESIGNER": DESIGNER, "CITY": CITY, "MESSAGE": MESSAGE})


class KidsroomDesignsView(APIView):

    template_name = "listing/designs.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        CITY = cities()
        DESIGNER = designers()
        designtype = "KIDS ROOM"
        DESIGNS = filterdesigns(designtype)

        if DESIGNS:

            return render(request, "listing/designs.html", {"DESIGNER": DESIGNER, "CITY": CITY, "DESIGNS": DESIGNS})

        else:

            CITY = cities()
            DESIGNER = designers()

            MESSAGE = "NO MATCH FOUND"
            return render(request, "listing/designs_nomatch.html", {"DESIGNER": DESIGNER, "CITY": CITY, "MESSAGE": MESSAGE})


class DesignsView(APIView):

    template_name = "listing/designs.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request, *args, **kwargs):

        CITY = cities()
        DESIGNER = designers()
        DESIGNS = designs(myDict=None)

        print("DESIGNS", DESIGNS)

        return render(request, "listing/designs.html", {"DESIGNER": DESIGNER, "CITY": CITY, "DESIGNS": DESIGNS})

    def post(self, request, *args, **kwargs):

        myDict = request.data.dict()
        print("myDict", myDict)

        DESIGNS = designs(myDict)
        CITY = cities()
        DESIGNER = designers()

        print("DESIGNS", DESIGNS)

        if DESIGNS:

            return render(request, "listing/designs.html", {"DESIGNER": DESIGNER, "CITY": CITY, "DESIGNS": DESIGNS})

        else:

            CITY = cities()
            DESIGNER = designers()

            MESSAGE = "NO MATCH FOUND"
            return render(request, "listing/designs_nomatch.html", {"DESIGNER": DESIGNER, "CITY": CITY, "MESSAGE": MESSAGE})


class DesignerIntroView(View):
    def get(self, request, *args, **kwargs):

        pk = self.kwargs["pk"]

        # PORTFOLIO DETAILS ############################################################
        portfolios = PortfolioBasic.objects.filter(id=pk).values(
                "id", "designer_id", "name", "portfolio_id", "client_name", "city_name", "type_of_property", "service_type", "duration", "budget", "video", "thumbnail", "image_1", "image_2", "image_3", "image_4", "image_5")
        portfolios_list = list(portfolios)
        PORTFOLIOS = portfolios_list[0]
        designer_name = PORTFOLIOS["name"]

        # ALL DESIGNER PORTFOLIOS ############################################################
        portfolios = PortfolioBasic.objects.filter(name=designer_name).values(
                "id", "designer_id", "name", "portfolio_id", "client_name", "city_name", "type_of_property", "service_type", "duration", "budget", "video", "thumbnail", "image_1", "image_2", "image_3", "image_4", "image_5")
        portfolios_list = list(portfolios)
        PORTFOLIOS_ALL = portfolios_list

        # DESIGNS ######################################################################
        designs = Designs.objects.filter(designer_name=designer_name).values(
            "design_id", "design_image", "design_type", "designer_name", "price")
        DESIGNS = list(designs)

        return render(request, "listing/designerintro.html", {"PORTFOLIOS": PORTFOLIOS, "pk": pk, "DESIGNS": DESIGNS, "PORTFOLIOS_ALL": PORTFOLIOS_ALL})


class InteriorsListView(APIView):
    def get(self, request, *args, **kwargs):

        CITY = cities()
        DESIGNER = designers()
        PORTFOLIOS = portfolios(myDict=None)
        PORTFOLIO_1 = PORTFOLIOS[0]
        PORTFOLIO_2 = PORTFOLIOS[1]
        PORTFOLIO_3 = PORTFOLIOS[2]

        return render(request, "listing/designers.html", {"CITY": CITY, "DESIGNER": DESIGNER, "PORTFOLIO_1": PORTFOLIO_1, "PORTFOLIO_2": PORTFOLIO_2, "PORTFOLIO_3": PORTFOLIO_3})

    def post(self, request, *args, **kwargs):

        myDict = request.data.dict()
        print("myDict", myDict)

        DESIGNS = designs(myDict=None)
        CITY = cities()
        DESIGNER = designers()

        print("DESIGNS", DESIGNS)

        if myDict['filterby'] == "Designs":

            return redirect("designs/", {"DESIGNER": DESIGNER, "CITY": CITY, "DESIGNS": DESIGNS})

        elif myDict['filterby'] == "Portfolios":

            return redirect("portfolios/", {"DESIGNER": DESIGNER, "CITY": CITY, "DESIGNS": DESIGNS})

        else:

            CITY = cities()
            DESIGNER = designers()

            MESSAGE = "NO MATCH FOUND"
            return render(request, "listing/designs_nomatch.html", {"DESIGNER": DESIGNER, "CITY": CITY, "MESSAGE": MESSAGE})


class PortfoliosView(APIView):
    def get(self, request, *args, **kwargs):

        CITY = cities()
        DESIGNER = designers()
        PORTFOLIOS = portfolios(myDict=None)

        return render(request, "listing/portfolios.html", {"CITY": CITY, "DESIGNER": DESIGNER, "PORTFOLIOS": PORTFOLIOS})

    def post(self, request, *args, **kwargs):

        myDict = request.data.dict()
        print("myDict", myDict)

        PORTFOLIOS = portfolios(myDict)
        CITY = cities()
        DESIGNER = designers()

        print("PORTFOLIOS", PORTFOLIOS)

        if PORTFOLIOS:

            return render(request, "listing/portfolios.html", {"DESIGNER": DESIGNER, "CITY": CITY, "PORTFOLIOS": PORTFOLIOS})

        else:

            CITY = cities()
            DESIGNER = designers()

            MESSAGE = "NO MATCH FOUND"
            return render(request, "listing/portfolios_nomatch.html", {"DESIGNER": DESIGNER, "CITY": CITY, "MESSAGE": MESSAGE})


class DesignsListing(APIView):

    template_name = "listing/design.html"
    parser_classes = (
        FormParser,
        MultiPartParser,
    )

    def get(self, request):

        design_form = DesignGalleryForm()
        DESIGNER = designers()

        return render(
            request, "listing/design.html", {
                "design_form": design_form, "DESIGNER": DESIGNER},
        )

    def post(self, request, *args, **kwargs):

        design_DATA = {}
        myDict = request.data.dict()
        print("myDict", myDict)
        design_form = DesignGalleryForm(request.POST, request.FILES)

        # Save Design Form
        if design_form.is_valid():
            design_form.save()

        designgallery = DesignGallery.objects.filter(
            designer_id=str(myDict["designer_id"]), design_type=str(myDict["design_type"])).values("design_image")

        print("designgallery", designgallery)
        l = len(designgallery)

        if designgallery:

            design_DATA['design_image'] = BASE_URL + \
                "media/" + str(designgallery[l-1]['design_image'])

            design_DATA['design_type'] = myDict['design_type']
            design_DATA['designer_name'] = myDict['name']
            design_DATA['price'] = myDict['price']
            design_DATA['designer_id'] = myDict['designer_id']
            design_DATA['design_id'] = myDict['name'].replace(" ", "") + "#" + str(myDict['design_type'].replace(" ", "")) + str(generate_Designer_id())

            json_data=json.dumps(design_DATA, indent=4)
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            r=requests.post(URL_DESIGN, data=json_data, headers=headers)
            status=r.status_code
            if status == 201:

                message="Successfully Posted Design"
                return render(request, "listing/design.html", {"design_form": design_form, "message": message})

            else:
                return render(request, "listing/design.html", {"design_form": design_form})


class PortfolioListing(APIView):

    template_name="listing/portfolio.html"
    parser_classes=(
        FormParser,
        MultiPartParser,
    )

    def get(self, request):

        portfolioform=PortfolioGalleryForm()
        CITY=cities()
        return render(request, "listing/portfolio.html", {"portfolioform": portfolioform, "CITY": CITY})

    def post(self, request, *args, **kwargs):

        portfolio_dict={}
        myDict=request.data.dict()
        print("myDict", myDict)
        portfolioform=PortfolioGalleryForm(request.POST, request.FILES)

        # Save Portfolio Form
        if portfolioform.is_valid():
            portfolioform.save()

        portfolio_dict["aboutyourself"]=myDict["aboutyourself"]
        portfolio_dict["designer_id"]=myDict["designerid"]
        portfolio_dict["name"]=myDict["designername"].replace(" ", "_")
        designername=myDict["designername"].replace(" ", "")
        portfolio_dict["portfolio_id"]=designername.upper() + \
                                                          "#" + generate_Portfolio_id()
        portfolio_dict["client_name"]=myDict["customername"]
        portfolio_dict["city_name"]=myDict["location"]
        portfolio_dict["type_of_property"]=myDict["propertytype"]
        portfolio_dict["service_type"]=myDict["service"]
        portfolio_dict["duration"]=myDict["duration"]
        portfolio_dict["budget"]=myDict["price"]
        video = myDict["video"]
        video_edited = video.split("=")[1]
        video_link = "https://www.youtube.com/embed/" + video_edited
        portfolio_dict["video"] = video_link

        # Gallery details
        portfolio_id=str(myDict["portfolio_id"])
        portfoliogallery=PortfolioGallery.objects.filter(portfolio_id=str(myDict["portfolio_id"])).values(
            "thumbnail", "image_1", "image_2", "image_3", "image_4", "image_5")

        l=len(portfoliogallery)
        if portfoliogallery:
            portfolio_dict["thumbnail"]=BASE_URL + \
                "media/" + str(portfoliogallery[l-1]["thumbnail"])
            portfolio_dict["image_1"]=BASE_URL + \
                "media/" + str(portfoliogallery[l-1]["image_1"])
            portfolio_dict["image_2"]=BASE_URL + \
                "media/" + str(portfoliogallery[l-1]["image_2"])
            portfolio_dict["image_3"]=BASE_URL + \
                "media/" + str(portfoliogallery[l-1]["image_3"])
            portfolio_dict["image_4"]=BASE_URL + \
                "media/" + str(portfoliogallery[l-1]["image_4"])
            portfolio_dict["image_5"]=BASE_URL + \
                "media/" + str(portfoliogallery[l-1]["image_5"])

            json_data=json.dumps(portfolio_dict, indent=4)
            print("json_data", json_data)
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            r=requests.post(URL_PORTFOLIO, data=json_data, headers=headers)
            status=r.status_code
            if status == 201:

                message="Successfully Posted Portfolio"
                return render(request, "listing/portfolio.html", {"portfolioform": portfolioform, "message": message})

            else:
                return render(request, "listing/portfolio.html", {"portfolioform": portfolioform})



class BookFreeConsultation(APIView):

    template_name="listing/bookfreeconsultation.html"
    parser_classes=(
        FormParser,
        MultiPartParser,
    )

    def get(self, request):
        return render(request, "listing/bookfreeconsultation.html",)

    def post(self, request, *args, **kwargs):

        bookfreeconsultation={}
        myDict=request.data.dict()
        print("myDict", myDict)

        bookfreeconsultation["name"]=myDict["name"]
        bookfreeconsultation["email_id"]=myDict["emailid"]
        bookfreeconsultation["phone"]=myDict["phonenumber"]
        bookfreeconsultation["state"]=myDict["state"]
        bookfreeconsultation["city"]=myDict["city"]
        bookfreeconsultation["zipcode"]=myDict["zipcode"]
        bookfreeconsultation["whatsapp"]='False'

        json_data=json.dumps(bookfreeconsultation, indent=4)
        print("json_data", json_data)
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        r=requests.post(URL_BOOKFREECONSULTATION,
                          data=json_data, headers=headers)
        return render(request, "listing/bookfreeconsultation.html",)


class PreConsultation(APIView):

    template_name="listing/preconsultation.html"
    parser_classes=(
        FormParser,
        MultiPartParser,
    )

    def get(self, request):
        return render(request, "listing/preconsultation.html",)


class CustomerReview(APIView):

    template_name="listing/customerreview.html"
    parser_classes=(
        FormParser,
        MultiPartParser,
    )

    def get(self, request):
        return render(request, "listing/customerreview.html",)

    # def post(self, request):
    #     b = {}
    #     g = {}
    #     l = {}
    #     f = {}
    #     d = {}
    #     property_DATA = {}
    #     basic = []
    #     gallery = []
    #     location = []
    #     features = []
    #     details = []

    #     basic_form = Basic_InformationForm(request.POST)
    #     gallery_form = GalleryForm(request.POST, request.FILES)
    #     location_form = LocationForm(request.POST)
    #     feature_form = FeaturesForm(request.POST)
    #     detail_form = DetailsForm(request.POST)
    #     # print("request.data", request.data)
    #     myDict = request.data.dict()

    #     if (
    #         basic_form.is_valid()
    #         and gallery_form.is_valid()
    #         and location_form.is_valid()
    #         and feature_form.is_valid()
    #         and detail_form.is_valid()
    #     ):

    #         # Basic Information
    #         b["project_area"] = myDict["project_area"]
    #         b["propertytype"] = myDict["propertytype"]
    #         b["total_units"] = myDict["total_units"]
    #         b["available_units"] = myDict["available_units"]
    #         b["total_no_of_towers"] = myDict["total_no_of_towers"]
    #         b["total_no_of_floors"] = myDict["total_no_of_floors"]
    #         b["approved_by"] = myDict["approved_by"]
    #         b["launch_year"] = myDict["launch_year"]
    #         b["commencement_certificate"] = myDict["commencement_certificate"]

    #         # Gallery
    #         property_name = myDict["name"]
    #         property_id = myDict["property_id"]

    #         # Save Gallery Form
    #         gallery_form.save()

    #         g = process_gallerydata(property_name, property_id, URL_GALLERY)

    #         # Location
    #         l["location"] = myDict["location"]
    #         l["State"] = myDict["State"]
    #         l["City"] = myDict["City"]
    #         l["Longitude"] = myDict["Longitude"]
    #         l["Latitude"] = myDict["Latitude"]

    #         # Features
    #         f["pet_friendly"] = myDict["pet_friendly"]
    #         f["furnished"] = myDict["furnished"]
    #         f["cooling"] = myDict["cooling"]
    #         f["parking"] = myDict["parking"]
    #         f["mailbox"] = myDict["mailbox"]
    #         f["city_view"] = myDict["city_view"]
    #         f["yoga_room"] = myDict["yoga_room"]
    #         f["swimming_pool"] = myDict["swimming_pool"]
    #         f["badminton_court"] = myDict["badminton_court"]
    #         f["squash_court"] = myDict["squash_court"]
    #         f["snooker_table"] = myDict["snooker_table"]
    #         f["basketball_court"] = myDict["basketball_court"]
    #         f["multipurpose_court"] = myDict["multipurpose_court"]
    #         f["outdoor_gym"] = myDict["outdoor_gym"]
    #         f["amphitheatre"] = myDict["amphitheatre"]
    #         f["childs_playarea"] = myDict["childs_playarea"]
    #         f["srcitizen_area"] = myDict["srcitizen_area"]
    #         f["cycling_track"] = myDict["cycling_track"]

    #         # Edit Video Link
    #         video = myDict["video"]
    #         video_edited = video.split("=")[1]
    #         video_link = "https://www.youtube.com/embed/" + video_edited

    #         # Details
    #         d["property_id"] = myDict["property_id"]
    #         d["builder_name"] = myDict["builder_name"]
    #         d["sold_projects"] = myDict["sold_projects"]
    #         d["completed_projects"] = myDict["completed_projects"]
    #         d["ongoing_projects"] = myDict["ongoing_projects"]
    #         d["name"] = myDict["name"]
    #         d["status"] = myDict["status"]
    #         d["propertytype"] = myDict["propertytype"]
    #         d["price"] = myDict["price"]
    #         temp = myDict["price"]
    #         if int(temp) > 100000 and int(temp) < 10000000:

    #             d["converted_price"] = round(
    #                 float(int(myDict["price"]) / 100000), 2
    #             )
    #             d["price_withunit"] = str(d["converted_price"]) + " " + "Lakhs"
    #         elif int(temp) > 10000000:
    #             d["converted_price"] = round(
    #                 float(int(myDict["price"]) / 10000000), 2
    #             )
    #             d["price_withunit"] = str(d["converted_price"]) + " " + "Cr"
    #         d["mortgage"] = 0.8 * int(myDict["price"])
    #         d["description"] = myDict["description"]
    #         d["space"] = myDict["space"]
    #         d["video"] = video_link
    #         d["beds"] = myDict["beds"]
    #         d["bathrooms"] = myDict["bathrooms"]
    #         d["condition"] = myDict["condition"]
    #         d["year_built"] = myDict["year_built"]

    #         # Complete Property Data >> POSTING to API
    #         basic.append(b)
    #         gallery.append(g)
    #         location.append(l)
    #         features.append(f)
    #         details.append(d)
    #         property_DATA["gallery_links"] = gallery
    #         property_DATA["basic"] = basic
    #         property_DATA["location"] = location
    #         property_DATA["features"] = features
    #         property_DATA["details"] = details
    #         # print("property_DATA", property_DATA)

    #         json_data = json.dumps(property_DATA, indent=4)
    #         print("json_data", json_data)
    #         headers = {
    #             "Accept": "application/json",
    #             "Content-Type": "application/json",
    #         }
    #         r = requests.post(URL_LISTING, data=json_data, headers=headers)

    #         return render(
    #             request,
    #             "listing/submit-listing.html",
    #             {
    #                 "basic_form": Basic_InformationForm(
    #                     instance=Basic_Information()
    #                 ),
    #                 "gallery_form": GalleryForm(instance=Gallery()),
    #                 "location_form": LocationForm(instance=Location()),
    #                 "feature_form": FeaturesForm(instance=Features()),
    #                 "detail_form": DetailsForm(instance=Details()),
    #             },
    #         )

    #     else:

    #         basic_form = Basic_InformationForm(instance=Basic_Information())
    #         gallery_form = GalleryForm(instance=Gallery())
    #         location_form = LocationForm(instance=Location())
    #         feature_form = FeaturesForm(instance=Features())
    #         detail_form = DetailsForm(instance=Details())

    #         return render(
    #             request,
    #             "listing/submit-listing.html",
    #             {
    #                 "basic_form": basic_form,
    #                 "gallery_form": gallery_form,
    #                 "location_form": location_form,
    #                 "feature_form": feature_form,
    #                 "detail_form": detail_form,
    #             },
    #         )

# class AboutusInteriors(APIView):

#     template_name = "listing/aboutus.html"
#     parser_classes = (
#         FormParser,
#         MultiPartParser,
#     )

# def get(self, request):

#     return render(
#         request, "listing/aboutus.html"
#     )
