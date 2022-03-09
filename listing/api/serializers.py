# Rest Framework Imports
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    RelatedField,
    CharField,
)
from rest_framework import fields
from listing.models import (
    Basic_Information,
    Gallery_links,
    Gallery,
    Location,
    Features,
    Details,
    Listing,
    Register,
)


class RegisterSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = Register
        fields = [
            "id",
            "full_name",
            "phone_number",
            "date",
        ]


class Basic_InformationSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = Basic_Information
        fields = [
            "id",
            "project_area",
            "propertytype",
            "total_units",
            "available_units",
            "total_no_of_towers",
            "total_no_of_floors",
            "approved_by",
            "launch_year",
            "commencement_certificate",
        ]


class Gallery_linksSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = Gallery_links
        fields = [
            "id",
            "property_name",
            "property_id",
            "status",
            "thumbnail",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
        ]


class GallerySerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = Gallery
        fields = [
            "id",
            "property_name",
            "property_id",
            "status",
            "thumbnail",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
        ]


class LocationSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = Location
        fields = ["id", "location", "State", "City", "Longitude", "Latitude"]


class FeaturesSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = Features
        fields = [
            "id",
            "pet_friendly",
            "furnished",
            "cooling",
            "parking",
            "mailbox",
            "city_view",
            "yoga_room",
            "swimming_pool",
            "badminton_court",
            "squash_court",
            "snooker_table",
            "basketball_court",
            "multipurpose_court",
            "outdoor_gym",
            "amphitheatre",
            "childs_playarea",
            "srcitizen_area",
            "cycling_track",
        ]


class DetailsSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)

    class Meta:
        model = Details
        fields = [
            "id",
            "property_id",
            "builder_name",
            "sold_projects",
            "completed_projects",
            "ongoing_projects",
            "name",
            "status",
            "propertytype",
            "price",
            "price_withunit",
            "mortgage",
            "converted_price",
            "description",
            "space",
            "video",
            "beds",
            "bathrooms",
            "condition",
            "year_built",
        ]


class ListingSerializer(ModelSerializer):
    id = CharField(source="pk", read_only=True)
    basic = Basic_InformationSerializer(many=True)
    gallery_links = Gallery_linksSerializer(many=True)
    location = LocationSerializer(many=True)
    features = FeaturesSerializer(many=True)
    details = DetailsSerializer(many=True)

    class Meta:
        model = Listing
        fields = [
            "id",
            "gallery_links",
            "basic",
            "location",
            "features",
            "details",
        ]

    def create(self, validated_data):

        Gallery_validated_data = validated_data.pop("gallery_links", None)
        BasicInfo_validated_data = validated_data.pop("basic", None)
        Location_validated_data = validated_data.pop("location", None)
        Features_validated_data = validated_data.pop("features", None)
        Details_validated_data = validated_data.pop("details", None)

        listing = Listing.objects.create(**validated_data)

        for g_data in Gallery_validated_data:
            Gallery_links.objects.create(listing=listing, **g_data)

        for bi_data in BasicInfo_validated_data:
            Basic_Information.objects.create(listing=listing, **bi_data)

        for l_data in Location_validated_data:
            Location.objects.create(listing=listing, **l_data)

        for f_data in Features_validated_data:
            Features.objects.create(listing=listing, **f_data)

        for d_data in Details_validated_data:
            Details.objects.create(listing=listing, **d_data)

        return listing
