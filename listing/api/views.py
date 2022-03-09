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
from listing.models import Listing, Gallery, Register
from .serializers import (
    ListingSerializer,
    GallerySerializer,
    RegisterSerializer,
)


class ListingView(ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def post(self, request, *args, **kwargs):

        serializer = ListingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class GalleryListView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class RegisterView(ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):

        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
