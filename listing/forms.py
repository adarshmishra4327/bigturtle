from django import forms

from .models import (
    Basic_Information,
    Gallery,
    Location,
    Features,
    Details,
    Filter_listings,
    Register,
)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = [
            "full_name",
            "phone_number",
            "date",
        ]


class Basic_InformationForm(forms.ModelForm):
    class Meta:
        model = Basic_Information
        fields = [
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


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [
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


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["location", "State", "City", "Longitude", "Latitude"]


class FeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = [
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


class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = [
            "property_id",
            "builder_name",
            "sold_projects",
            "completed_projects",
            "ongoing_projects",
            "name",
            "status",
            "propertytype",
            "price",
            "description",
            "space",
            "video",
            "beds",
            "bathrooms",
            "condition",
            "year_built",
        ]


class Filter_listingsForm(forms.ModelForm):
    class Meta:
        model = Filter_listings
        fields = [
            "location",
            "status",
            "price_range",
            "beds",
            "bathrooms",
            "prop_type",
            "space",
            "sort_by",
            "builder",
        ]
