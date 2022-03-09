# Rest Framework Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)

# Application Imports
from interiors.models import (
    BasicInformation,
    Interior,
    PortfolioBasic,
    PortfolioGallery,
    Customer_feedback,
    Designs,
    Online_Consultation,
    DesignGallery,
)
from .serializers import (
    BasicInformationSerializer,
    PortfolioBasicSerializer,
    Customer_feedbackSerializer,
    DesignsSerializer,
    Online_ConsultationSerializer,
    PortfolioGallerySerializer,
    DesignGallerySerializer,
)
from rest_framework.permissions import IsAuthenticated


class PortfolioGalleryView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = PortfolioGallery.objects.all()
    serializer_class = PortfolioGallerySerializer


class PortfolioView(ListCreateAPIView):
    queryset = PortfolioBasic.objects.all()
    serializer_class = PortfolioBasicSerializer

    def post(self, request, *args, **kwargs):

        serializer = PortfolioBasicSerializer(data=request.data)
        print("serializer", serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class BookfreeconsultationView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Online_Consultation.objects.all()
    serializer_class = Online_ConsultationSerializer

    def post(self, request, *args, **kwargs):

        serializer = Online_ConsultationSerializer(data=request.data)
        print("serializer", serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class DesignGalleryView(ListCreateAPIView):
    queryset = DesignGallery.objects.all()
    serializer_class = DesignGallerySerializer

    def post(self, request, *args, **kwargs):

        serializer = DesignGallerySerializer(data=request.data)
        print("serializer", serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class DesignsView(ListCreateAPIView):
    queryset = Designs.objects.all()
    serializer_class = DesignsSerializer

    def post(self, request, *args, **kwargs):

        serializer = DesignsSerializer(data=request.data)
        print("serializer", serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


# class DesignsListView(ListAPIView):
#     # queryset = Designs.objects.all()
#     serializer_class = DesignsSerializer


# class InteriorView(ListCreateAPIView):
#     queryset = Interior.objects.all()
#     serializer_class = InteriorSerializer

#     def post(self, request, *args, **kwargs):

#         serializer = InteriorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED)


class Customer_feedbackView(ListCreateAPIView):
    queryset = Customer_feedback.objects.all()
    serializer_class = Customer_feedbackSerializer

    def post(self, request, *args, **kwargs):

        serializer = Customer_feedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
