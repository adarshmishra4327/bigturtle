from django.contrib import admin
from interiors.models import (
    Interior,
    BasicInformation,
    PortfolioBasic,
    Designs,
    Online_Consultation,
    Pre_Consultation,
    Customer_Review,
    Customer_feedback,
    PortfolioGallery,
    State,
    City,
    DesignGallery,
    PortfolioGalleryLinks,
)


admin.site.register(BasicInformation)
admin.site.register(PortfolioBasic)
admin.site.register(Interior)
admin.site.register(Customer_feedback)
admin.site.register(Designs)
admin.site.register(Online_Consultation)
admin.site.register(Pre_Consultation)
admin.site.register(Customer_Review)
admin.site.register(PortfolioGallery)
admin.site.register(PortfolioGalleryLinks)
admin.site.register(State)
admin.site.register(City)
admin.site.register(DesignGallery)
