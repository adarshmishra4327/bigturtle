from django.db import models
from multiselectfield import MultiSelectField
import time
from django.urls import reverse


def default_id_num():
    return str(int(time.time()))


class Register(models.Model):

    full_name = models.CharField("Full Name", max_length=200)
    email = models.CharField(
        "Email Address", max_length=200, default=None, null=True
    )
    phone_number = models.CharField("Phone Number", max_length=200)
    date = models.CharField("Date & Time", max_length=200)
    comment = models.CharField(
        "Comment", max_length=200, default=None, null=True
    )

    def __str__(self):
        return self.full_name


class Listing(models.Model):

    unique_id = models.CharField(
        "Unique id", primary_key=False, max_length=100, default=None, null=True
    )

    def get_absolute_url(self):
        return reverse("properties-detail", kwargs={"pk": self.pk})


class Basic_Information(models.Model):

    STATUS_CHOICES = [
        ("FOR SALE", "For Sale"),
        ("READY TO MOVE", "Ready to Move"),
        ("UNDERCONSTRUCTION", "Underconstruction"),
        ("LEASED", "Leased"),
        ("SOLD", "Sold"),
        ("SPECIAL OFFER", "Special Offer"),
        ("NEW ADDITION", "New Addition"),
        ("RENTAL", "Rental"),
        ("REDUCED", "Reduced"),
    ]
    TYPE_CHOICES = [
        ("COMMERCIAL", "Commercial"),
        ("RESIDENTIAL", "Residential"),
        ("APARTMENT", "Apartment"),
        ("PLOTS", "Plots"),
        ("VILLA", "Villa"),
        ("DUPLEX", "Duplex"),
    ]

    CC_CHOICES = [
        ("YES", "Yes"),
        ("NO", "No"),
    ]

    project_area = models.CharField(
        "Property Area (In Acres)", max_length=100, default=None, null=True
    )

    total_units = models.IntegerField("Total Units")

    available_units = models.IntegerField("Available Units")

    total_no_of_towers = models.IntegerField("Total No of Towers")

    total_no_of_floors = models.IntegerField("Total No of Floors")

    approved_by = models.CharField(
        "Approved by", max_length=100, default=None, null=True
    )

    launch_year = models.IntegerField("Launch Year")

    commencement_certificate = models.CharField(
        "Commencement Certificate", max_length=20, choices=CC_CHOICES
    )

    name = models.CharField(
        "Property Name", max_length=100, default=None, null=True
    )
    status = models.CharField(
        "Property Status", max_length=20, choices=STATUS_CHOICES
    )
    propertytype = models.CharField(
        "PropertyType", max_length=20, choices=TYPE_CHOICES
    )
    listing = models.ForeignKey(
        Listing, related_name="basic", on_delete=models.CASCADE, default=8
    )


class Gallery(models.Model):

    STATUS_CHOICES = [
        ("FOR SALE", "For Sale"),
        ("READY TO MOVE", "Ready to Move"),
        ("UNDERCONSTRUCTION", "Underconstruction"),
        ("LEASED", "Leased"),
        ("SOLD", "Sold"),
        ("SPECIAL OFFER", "Special Offer"),
        ("NEW ADDITION", "New Addition"),
        ("RENTAL", "Rental"),
        ("REDUCED", "Reduced"),
    ]

    property_name = models.CharField("Property Name", max_length=200)
    property_id = models.CharField("RERA Id", max_length=200)
    status = models.CharField("Status", max_length=50, choices=STATUS_CHOICES)
    thumbnail = models.ImageField(upload_to="images/thumbnail/")
    image_1 = models.ImageField(upload_to="images/image_1/")
    image_2 = models.ImageField(upload_to="images/image_2/")
    image_3 = models.ImageField(upload_to="images/image_3/")
    image_4 = models.ImageField(upload_to="images/image_4/")
    image_5 = models.ImageField(upload_to="images/image_5/")
    timecreated = models.CharField(max_length=200, default=default_id_num())

    def __str__(self):
        return self.property_name


class Gallery_links(models.Model):

    STATUS_CHOICES = [
        ("FOR SALE", "For Sale"),
        ("READY TO MOVE", "Ready to Move"),
        ("UNDERCONSTRUCTION", "Underconstruction"),
        ("LEASED", "Leased"),
        ("SOLD", "Sold"),
        ("SPECIAL OFFER", "Special Offer"),
        ("NEW ADDITION", "New Addition"),
        ("RENTAL", "Rental"),
        ("REDUCED", "Reduced"),
    ]

    property_name = models.CharField(max_length=200)
    property_id = models.CharField(max_length=200)
    status = models.CharField("Status", max_length=50, choices=STATUS_CHOICES)
    thumbnail = models.URLField(max_length=200)
    image_1 = models.URLField(max_length=200)
    image_2 = models.URLField(max_length=200)
    image_3 = models.URLField(max_length=200)
    image_4 = models.URLField(max_length=200)
    image_5 = models.URLField(max_length=200)
    listing = models.ForeignKey(
        Listing,
        related_name="gallery_links",
        on_delete=models.CASCADE,
        default=8,
    )

    def __str__(self):
        return self.property_name


class Location(models.Model):

    STATE_CHOICES = [
        ("KARNATAKA", "KARNATAKA"),
        ("MAHARASHTRA", "MAHARASHTRA"),
        ("DELHI", "DELHI"),
        ("TELANGANA", "TELANGANA"),
        ("GUJARAT", "GUJARAT"),
        ("TAMIL NADU", "TAMIL NADU"),
        ("WEST BENGAL", "WEST BENGAL"),
        ("RAJASTHAN", "RAJASTHAN"),
        ("UTTAR PRADESH", "UTTAR PRADESH"),
        ("MADHYA PRADESH", "MADHYA PRADESH"),
        ("ANDHRA PRADESH", "ANDHRA PRADESH"),
        ("BIHAR", "BIHAR"),
        ("PUNJAB", "PUNJAB"),
        ("JHARKHAND", "JHARKHAND"),
        ("JAMMU AND KASHMIR", "JAMMU AND KASHMIR"),
        ("CHHATTISGARH", "CHHATTISGARH"),
        ("CHANDIGARH", "CHANDIGARH"),
        ("ASSAM", "ASSAM"),
        ("ODISHA", "ODISHA"),
        ("KERALA", "KERALA"),
        ("TRIPURA", "TRIPURA"),
        ("MANIPUR", "MANIPUR"),
        ("PUDUCHERRY", "PUDUCHERRY"),
        ("HIMACHAL PRADESH", "HIMACHAL PRADESH"),
        ("SIKKIM", "SIKKIM"),
    ]

    CITY_CHOICES = [
        ("MUMBAI", "MUMBAI"),
        ("DELHI", "DELHI"),
        ("BENGALURU", "BENGALURU"),
        ("HYDERABAD", "HYDERABAD"),
        ("AHMEDABAD", "AHMEDABAD"),
        ("CHENNAI", "CHENNAI"),
        ("KOLKATA", "KOLKATA"),
        ("SURAT", "SURAT"),
        ("PUNE", "PUNE"),
        ("JAIPUR", "JAIPUR"),
        ("LUCKNOW", "LUCKNOW"),
        ("KANPUR", "KANPUR"),
        ("NAGPUR", "NAGPUR"),
        ("INDORE", "INDORE"),
        ("THANE", "THANE"),
        ("BHOPAL", "BHOPAL"),
        ("VISAKHAPATNAM", "VISAKHAPATNAM"),
        ("CHINCHWAD", "CHINCHWAD"),
        ("PATNA", "PATNA"),
        ("VADODARA", "VADODARA"),
        ("GHAZIABAD", "GHAZIABAD"),
        ("LUDHIANA", "LUDHIANA"),
        ("AGRA", "AGRA"),
        ("NASHIK", "NASHIK"),
        ("RANCHI", "RANCHI"),
        ("FARIDABAD", "FARIDABAD"),
        ("MEERUT", "MEERUT"),
        ("RAJKOT", "RAJKOT"),
        ("DOMBIVLI", "DOMBIVLI"),
        ("VIRAR", "VIRAR"),
        ("VARANASI", "VARANASI"),
        ("SRINAGAR", "SRINAGAR"),
        ("AURANGABAD", "AURANGABAD"),
        ("DHANBAD", "DHANBAD"),
        ("AMRITSAR", "AMRITSAR"),
        ("NAVI MUMBAI", "NAVI MUMBAI"),
        ("ALLAHABAD", "ALLAHABAD"),
        ("HOWRAH", "HOWRAH"),
        ("GWALIOR", "GWALIOR"),
        ("JABALPUR", "JABALPUR"),
        ("COIMBATORE", "COIMBATORE"),
        ("VIJAYAWADA", "VIJAYAWADA"),
        ("JODHPUR", "JODHPUR"),
        ("MADURAI", "MADURAI"),
        ("RAIPUR", "RAIPUR"),
        ("KOTA", "KOTA"),
        ("CHANDIGARH", "CHANDIGARH"),
        ("GUWAHATI", "GUWAHATI"),
        ("SOLAPUR", "SOLAPUR"),
        ("MYSORE", "MYSORE"),
        ("BHUBANESWAR", "BHUBANESWAR"),
        ("THIRUVANATHAPURAM", "THIRUVANATHAPURAM"),
        ("DEHRADUN", "DEHRADUN"),
        ("JAMMU", "JAMMU"),
        ("AGARTALA", "AGARTALA"),
        ("KURNOOL", "KURNOOL"),
        ("AIZAWL", "AIZAWL"),
        ("IMPHAL", "IMPHAL"),
        ("PONDICHERRY", "PONDICHERRY"),
        ("GANDHINAGAR", "GANDHINAGAR"),
        ("SHIMLA", "SHIMLA"),
        ("HOSUR", "HOSUR"),
        ("AMARAVATI", "AMARAVATI"),
        ("GANGTOK", "GANGTOK"),
        ("KOTTAYAM", "KOTTAYAM"),
    ]

    location = models.CharField(
        "Property Location", max_length=100, default=None, null=True
    )
    State = models.CharField("State", max_length=20, choices=STATE_CHOICES)
    City = models.CharField("City", max_length=20, choices=CITY_CHOICES)
    Longitude = models.CharField(
        "Longitude", max_length=100, default=None, null=True
    )
    Latitude = models.CharField(
        "Latitude", max_length=100, default=None, null=True
    )
    listing = models.ForeignKey(
        Listing, related_name="location", on_delete=models.CASCADE, default=8
    )

    def __str__(self):
        return self.location


class Features(models.Model):

    pet_friendly = models.BooleanField("Pet Friendly", default=None, null=True)
    furnished = models.BooleanField("Furnished", default=None, null=True)
    cooling = models.BooleanField("Cooling", default=None, null=True)
    parking = models.BooleanField("Parking", default=None, null=True)
    mailbox = models.BooleanField("Mailbox", default=None, null=True)
    city_view = models.BooleanField("City View", default=None, null=True)
    yoga_room = models.BooleanField("Yoga Room", default=None, null=True)
    swimming_pool = models.BooleanField(
        "Swimming Pool", default=None, null=True
    )
    badminton_court = models.BooleanField(
        "Badminton Court", default=None, null=True
    )
    squash_court = models.BooleanField("Squash Court", default=None, null=True)
    snooker_table = models.BooleanField(
        "Snooker Table", default=None, null=True
    )
    basketball_court = models.BooleanField(
        "Basketball Court", default=None, null=True
    )
    multipurpose_court = models.BooleanField(
        "Multipurpose Court", default=None, null=True
    )
    outdoor_gym = models.BooleanField("Outdoor Gym", default=None, null=True)
    amphitheatre = models.BooleanField("Amphitheatre", default=None, null=True)
    childs_playarea = models.BooleanField(
        "Child's Play Area", default=None, null=True
    )
    srcitizen_area = models.BooleanField(
        "Sr. Citizen Area", default=None, null=True
    )
    cycling_track = models.BooleanField(
        "Cycling Track", default=None, null=True
    )
    listing = models.ForeignKey(
        Listing, related_name="features", on_delete=models.CASCADE, default=8
    )


class Details(models.Model):

    CONDITION = [("NEW", "New"), ("OLD", "Old")]

    STATUS_CHOICES = [
        ("FOR SALE", "For Sale"),
        ("READY TO MOVE", "Ready to Move"),
        ("UNDERCONSTRUCTION", "Underconstruction"),
        ("LEASED", "Leased"),
        ("SOLD", "Sold"),
        ("SPECIAL OFFER", "Special Offer"),
        ("NEW ADDITION", "New Addition"),
        ("RENTAL", "Rental"),
        ("REDUCED", "Reduced"),
    ]
    TYPE_CHOICES = [
        ("COMMERCIAL", "Commercial"),
        ("RESIDENTIAL", "Residential"),
        ("APARTMENT", "Apartment"),
        ("PLOTS", "Plots"),
        ("VILLA", "Villa"),
        ("DUPLEX", "Duplex"),
    ]

    UNIT_CHOICES = [
        ("Lakhs", "Lakhs"),
        ("Cr", "Cr"),
    ]

    builder_name = models.CharField(
        "Builder Name", max_length=100, default=None, null=True
    )
    sold_projects = models.IntegerField("Sold Projects")
    completed_projects = models.IntegerField("Completed Projects")
    ongoing_projects = models.IntegerField("Ongoing Projects")
    name = models.CharField(
        "Property Name", max_length=100, default=None, null=True
    )
    status = models.CharField(
        "Property Status", max_length=20, choices=STATUS_CHOICES
    )
    propertytype = models.CharField(
        "Property Type", max_length=20, choices=TYPE_CHOICES
    )
    price_withunit = models.CharField("Display Price", max_length=20)
    price = models.IntegerField("Property Price")
    converted_price = models.IntegerField("Price in Lakhs")
    mortgage = models.IntegerField(
        "Estimated Mortgage", default=None, null=True
    )
    description = models.CharField(
        "Property Description", max_length=500, default=None, null=True
    )
    space = models.IntegerField("Property Space(Sqft)")
    video = models.URLField("Property Video", blank=True)
    property_id = models.CharField(
        "Property Id", max_length=100, default=None, null=True
    )
    beds = models.IntegerField("No of Beds", default=None)
    bathrooms = models.IntegerField("No of Bathrooms", default=None)
    condition = models.CharField(
        "Property Condition", max_length=20, choices=CONDITION
    )
    year_built = models.IntegerField("Year Built", default=None)
    listing = models.ForeignKey(
        Listing, related_name="details", on_delete=models.CASCADE, default=8
    )


class Filter_listings(models.Model):

    CITY_CHOICES = [
        ("Any Location", "Any Location"),
        ("MUMBAI", "MUMBAI"),
        ("DELHI", "DELHI"),
        ("BENGALURU", "BENGALURU"),
        ("HYDERABAD", "HYDERABAD"),
        ("AHMEDABAD", "AHMEDABAD"),
        ("CHENNAI", "CHENNAI"),
        ("KOLKATA", "KOLKATA"),
        ("SURAT", "SURAT"),
        ("PUNE", "PUNE"),
        ("JAIPUR", "JAIPUR"),
        ("LUCKNOW", "LUCKNOW"),
        ("KANPUR", "KANPUR"),
        ("NAGPUR", "NAGPUR"),
        ("INDORE", "INDORE"),
        ("THANE", "THANE"),
        ("BHOPAL", "BHOPAL"),
        ("VISAKHAPATNAM", "VISAKHAPATNAM"),
        ("CHINCHWAD", "CHINCHWAD"),
        ("PATNA", "PATNA"),
        ("VADODARA", "VADODARA"),
        ("GHAZIABAD", "GHAZIABAD"),
        ("LUDHIANA", "LUDHIANA"),
        ("AGRA", "AGRA"),
        ("NASHIK", "NASHIK"),
        ("RANCHI", "RANCHI"),
        ("FARIDABAD", "FARIDABAD"),
        ("MEERUT", "MEERUT"),
        ("RAJKOT", "RAJKOT"),
        ("DOMBIVLI", "DOMBIVLI"),
        ("VIRAR", "VIRAR"),
        ("VARANASI", "VARANASI"),
        ("SRINAGAR", "SRINAGAR"),
        ("AURANGABAD", "AURANGABAD"),
        ("DHANBAD", "DHANBAD"),
        ("AMRITSAR", "AMRITSAR"),
        ("NAVI MUMBAI", "NAVI MUMBAI"),
        ("ALLAHABAD", "ALLAHABAD"),
        ("HOWRAH", "HOWRAH"),
        ("GWALIOR", "GWALIOR"),
        ("JABALPUR", "JABALPUR"),
        ("COIMBATORE", "COIMBATORE"),
        ("VIJAYAWADA", "VIJAYAWADA"),
        ("JODHPUR", "JODHPUR"),
        ("MADURAI", "MADURAI"),
        ("RAIPUR", "RAIPUR"),
        ("KOTA", "KOTA"),
        ("CHANDIGARH", "CHANDIGARH"),
        ("GUWAHATI", "GUWAHATI"),
        ("SOLAPUR", "SOLAPUR"),
        ("MYSORE", "MYSORE"),
        ("BHUBANESWAR", "BHUBANESWAR"),
        ("THIRUVANATHAPURAM", "THIRUVANATHAPURAM"),
        ("DEHRADUN", "DEHRADUN"),
        ("JAMMU", "JAMMU"),
        ("AGARTALA", "AGARTALA"),
        ("KURNOOL", "KURNOOL"),
        ("AIZAWL", "AIZAWL"),
        ("IMPHAL", "IMPHAL"),
        ("PONDICHERRY", "PONDICHERRY"),
        ("GANDHINAGAR", "GANDHINAGAR"),
        ("SHIMLA", "SHIMLA"),
        ("HOSUR", "HOSUR"),
        ("AMARAVATI", "AMARAVATI"),
        ("GANGTOK", "GANGTOK"),
        ("KOTTAYAM", "KOTTAYAM"),
    ]
    STATUS_CHOICES = [
        ("Any Status", "Any Status"),
        ("FOR SALE", "For Sale"),
        ("UNDERCONSTRUCTION", "Underconstruction"),
        ("LEASED", "Leased"),
        ("SOLD", "Sold"),
        ("SPECIAL OFFER", "Special Offer"),
        ("NEW ADDITION", "New Addition"),
        ("RENTAL", "Rental"),
        ("REDUCED", "Reduced"),
    ]
    PRICE_RANGE = [
        ("Any Price", "Any Price"),
        ("< 20 lakhs", "< 20 Lakhs"),
        ("20 - 40 Lakhs", "20 - 40 Lakhs"),
        ("40 - 60 Lakhs", "40 - 60 Lakhs"),
        ("60 - 80 Lakhs", "60 - 80 Lakhs"),
        ("< 1 Crore", "< 1 Crore"),
        ("> 1 Crore", "> 1 Crore"),
    ]
    TYPE_CHOICES = [
        ("COMMERCIAL", "COMMERCIAL"),
        ("RESIDENTIAL", "RESIDENTIAL"),
        ("APARTMENT", "APARTMENT"),
        ("PLOTS", "PLOTS"),
        ("VILLA", "VILLA"),
        ("DUPLEX", "DUPLEX"),
    ]
    BEDS = [
        ("Any", "Any"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    ]
    BATHROOMS = [
        ("Any", "Any"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    ]

    SPACE_CHOICES = [
        ("Any Size", "Any Size"),
        ("< 500 Sqft", "< 500 Sqft"),
        ("500 - 1000 Sqft", "500 - 1000 Sqft"),
        ("1000 - 1500 Sqft", "1000 - 1500 Sqft"),
        ("1500 - 2000 Sqft", "1500 - 2000 Sqft"),
        ("> 2000 Sqft", "> 2000 Sqft"),
    ]

    SORT_CHOICES = [
        ("Price: High to Low", "Price: High to Low"),
        ("Price: Low to High", "Price: Low to High"),
    ]

    BUILDER_CHOICES = [
        ("Any Builder", "Any Builder"),
        ("Amsa", "Amsa"),
        ("Shobha", "Shobha"),
        ("Sarita", "Sarita"),
    ]

    location = models.CharField(
        "Location", max_length=50, choices=CITY_CHOICES
    )
    status = models.CharField("Status", max_length=50, choices=STATUS_CHOICES)
    price_range = models.CharField(
        "Price Range", max_length=50, choices=PRICE_RANGE
    )
    beds = models.CharField("Beds", max_length=50, choices=BEDS)
    bathrooms = models.CharField("Bathrooms", max_length=50, choices=BATHROOMS)
    prop_type = models.CharField(
        "Property Type", max_length=50, choices=TYPE_CHOICES
    )
    space = models.CharField("Space", max_length=50, choices=SPACE_CHOICES)
    sort_by = models.CharField("Sort By", max_length=50, choices=SORT_CHOICES)
    builder = models.CharField(
        "Builder", max_length=50, choices=BUILDER_CHOICES
    )


class Consolidated_tables(models.Model):
    basic_information = models.ForeignKey(
        Basic_Information, on_delete=models.CASCADE, default=8,
    )
    gallery_links = models.ForeignKey(
        Gallery_links, on_delete=models.CASCADE, default=8,
    )
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, default=8,
    )
    features = models.ForeignKey(
        Features, on_delete=models.CASCADE, default=8,
    )
    details = models.ForeignKey(Details, on_delete=models.CASCADE, default=8,)
