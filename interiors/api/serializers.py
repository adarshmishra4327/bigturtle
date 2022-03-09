# Rest Framework Imports
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    RelatedField,
    CharField,
)
from rest_framework import fields
from interiors.models import (
    BasicInformation,
    PortfolioBasic,
    Interior,
    Customer_feedback,
    Designs,
    Online_Consultation,
    Pre_Consultation,
    Customer_Review,
    PortfolioGalleryLinks,
    PortfolioGallery,
    City,
    DesignGallery,
)


class CitySerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = City
        fields = [
            "id",
            "name",
        ]


class Online_ConsultationSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = Online_Consultation
        fields = [
            "id",
            "name",
            "email_id",
            "state",
            "city",
            "zipcode",
            "whatsapp",
        ]
        

class DesignsSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = Designs
        fields = [
            "id",
            "design_id",
            "design_image",
            "design_type",
            "designer_name",
            "price",
            "designer_id",
        ]


class DesignGallerySerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = DesignGallery
        fields = [
            "id",
            "designer_id",
            "design_image",
            "design_type",
            "price",
        ]


class BasicInformationSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = BasicInformation
        fields = [
            "id",
            "name",
            "aboutyourself",
            "experience",
            "projects",
            "display_projects",
            "clients",
            "awards",
        ]


class PortfolioBasicSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = PortfolioBasic
        fields = [
            "id",
            "aboutyourself",
            "designer_id",
            "name",
            "portfolio_id",
            "client_name",
            "city_name",
            "type_of_property",
            "service_type",
            "duration",
            "budget",
            "video",
            "thumbnail",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
        ]


class PortfolioGallerySerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = PortfolioGallery
        fields = [
            "id",
            "portfolio_id",
            "thumbnail",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
            "timecreated",
        ]


class PortfolioGalleryLinksSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = PortfolioGalleryLinks
        fields = [
            "id",
            "portfolio_id",
            "thumbnail",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
        ]


class Customer_feedbackSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = Customer_feedback
        fields = [
            "id",
            "name",
            "designer_name",
            "location",
            "city",
            "project_date",
            "type_of_property",
            "video",
            "thumbnail",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
            "feedback",
        ]


# class InteriorSerializer(ModelSerializer):
#     id = CharField(source="pk", read_only=True)
#     portfoliobasic = PortfolioBasicSerializer(many=True)
#     portfoliogallerylinks = PortfolioGalleryLinksSerializer(many=True)

#     class Meta:
#         model = Interior
#         fields = [
#             "id",
#             "portfoliobasic",
#             "portfoliogallerylinks",
#         ]

#     def create(self, validated_data):

#         PortfolioBasic_validated_data = validated_data.pop("portfoliobasic", None)
#         PortfolioGallery_validated_data = validated_data.pop("portfoliogallerylinks", None)

#         interiors = Interior.objects.create(**validated_data)

#         for pb_data in PortfolioBasic_validated_data:
#             PortfolioBasic.objects.create(interior=interiors, **pb_data)

#         for pg_data in PortfolioGallery_validated_data:
#             PortfolioGalleryLinks.objects.create(interior=interiors, **pg_data)

#         return interiors
