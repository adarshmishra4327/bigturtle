from django import forms

from .models import (
    Interior,
    BasicInformation,
    PortfolioBasic,
    Designs,
    Online_Consultation,
    Pre_Consultation,
    Customer_Review,
    Customer_feedback,
    PortfolioGallery,
    DesignGallery,
)


class DesignGalleryForm(forms.ModelForm):
    class Meta:
        model = DesignGallery
        fields = [
            "designer_id",
            "design_image",
            "design_type",
            "price",
        ]


class PortfolioGalleryForm(forms.ModelForm):
    class Meta:
        model = PortfolioGallery
        fields = [
            "portfolio_id",
            "thumbnail",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
        ]


class Online_ConsultationForm(forms.ModelForm):
    class Meta:
        model = Online_Consultation
        fields = [
            "name",
            "email_id",
            "phone",
            "city",
        ]


class Pre_ConsultationForm(forms.ModelForm):
    class Meta:
        model = Pre_Consultation
        fields = [
            "type_of_property",
            "size_home",
            "service_type",
            "budget",
            "possession",
            "communication",
        ]


class Customer_ReviewForm(forms.ModelForm):
    class Meta:
        model = Customer_Review
        fields = [
            "name",
            "city",
            "date",
            "duration",
            "type_of_property",
            "service_type",
            "price",
            "designer_id",
            "quality_service",
            "quality_material",
            "timeliness",
            "price",
            "communication",
            "finishing",
            "uniqueness",
            "diverse",
            "warranty",
        ]
