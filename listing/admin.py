from django.contrib import admin

from listing.models import (
    Basic_Information,
    Gallery,
    Gallery_links,
    Location,
    Features,
    Details,
    Listing,
    Filter_listings,
    Consolidated_tables,
    Register,
)

# Register your models here.
admin.site.register(Basic_Information)
admin.site.register(Gallery)
admin.site.register(Location)
admin.site.register(Features)
admin.site.register(Details)
admin.site.register(Listing)
admin.site.register(Gallery_links)
admin.site.register(Filter_listings)
admin.site.register(Consolidated_tables)
admin.site.register(Register)
