# General Imports
import time
import math
import random
import datetime

# Django Imports
from django.db import models
from django.urls import reverse

STATE_CHOICES = [
    ("Delhi", "Delhi"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
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

PROPERTY_CHOICES = [
    ("APARTMENT_1BHK", "APARTMENT_1BHK"),
    ("APARTMENT_2BHK", "APARTMENT_2BHK"),
    ("APARTMENT_3BHK", "APARTMENT_3BHK"),
    ("APARTMENT_4BHK", "APARTMENT_4BHK"),
    ("APARTMENT_5BHK", "APARTMENT_5BHK"),
    ("VILLA", "VILLA"),
    ("INDEPENDENT HOUSE", "INDEPENDENT HOUSE"),
    ("COMMERCIAL", "COMMERCIAL"),
]

SERVICE_CHOICES = [
    ("MODULAR KITCHEN", "MODULAR KITCHEN"),
    ("COMPLETE HOME DESIGN", "COMPLETE HOME DESIGN"),
    ("RENOVATION COMPLETE HOME", "RENOVATION COMPLETE HOME"),
    ("RENOVATION KITCHEN", "RENOVATION KITCHEN"),
    ("ESSENTIAL FURNITURES", "ESSENTIAL FURNITURES"),
]

DESIGN_CHOICES = [
    ("LIVING ROOM", "LIVING ROOM"),
    ("MODULAR KITCHEN", "MODULAR KITCHEN"),
    ("BATHROOM", "BATHROOM"),
    ("BED ROOM", "BED ROOM"),
    ("KIDS ROOM", "KIDS ROOM"),
]

LANGUAGE_CHOICES = [
    ("HINDI", "HINDI"),
    ("ENGLISH", "ENGLISH"),
    ("TAMIL", "TAMIL"),
    ("KANNADA", "KANNADA"),
    ("BENGALI", "BENGALI"),
    ("GUJRATI", "GUJRATI"),
]

POSSESSION_CHOICES = [
    ("IMMEDIATE", "IMMEDIATE"),
    ("1-3 MONTHS", "1-3 MONTHS"),
    ("4-6 MONTHS", "4-6 MONTHS"),
    ("HAVE POSSESSION-RENOVATION", "HAVE POSSESSION-RENOVATION"),
]


def generate_Portfolio_id():

    # for alpha numeric OTP
    corpus = "0123456789abcdefghijklmnopqrstuvwxyz"
    generate_OTP = ""
    size = 6
    length = len(corpus)
    for i in range(size):
        generate_OTP += corpus[math.floor(random.random() * length)]

    Portfolio_id = "PORT" + generate_OTP

    return Portfolio_id


def generate_Design_id():

    # for alpha numeric OTP
    corpus = "0123456789abcdefghijklmnopqrstuvwxyz"
    generate_OTP = ""
    size = 6
    length = len(corpus)
    for i in range(size):
        generate_OTP += corpus[math.floor(random.random() * length)]

    Design_id = "DESN" + generate_OTP

    return Design_id


def generate_Designer_id():

    # for alpha numeric OTP
    corpus = "0123456789abcdefghijklmnopqrstuvwxyz"
    generate_OTP = ""
    size = 6
    length = len(corpus)
    for i in range(size):
        generate_OTP += corpus[math.floor(random.random() * length)]

    Designer_id = "DEZINER" + generate_OTP

    return Designer_id


def default_id_num():
    return str(int(time.time()))


class Interior(models.Model):

    unique_id = models.CharField(
        "Unique id", primary_key=False, max_length=100, default=None, null=True
    )
    def get_absolute_url(self):
        return reverse("interiors-detail", kwargs={"pk": self.pk})


class City(models.Model):
    name = models.CharField("City Name", max_length=200)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField("State Name", max_length=200)

    def __str__(self):
        return self.name


class Designer(models.Model):

    unique_id = models.CharField(
        "Unique id", primary_key=False, max_length=100, default=None, null=True
    )
    def get_absolute_url(self):
        return reverse("designers-detail", kwargs={"pk": self.pk})


class BasicInformation(models.Model):

    designer_id = models.CharField("Designer Id", max_length=200)
    name = models.CharField("Designer Name", max_length=200)
    aboutyourself = models.CharField("About Designer", max_length=500)
    experience = models.IntegerField("Experience (In Years)")
    projects = models.IntegerField("No of Projects Completed")
    display_projects = models.IntegerField("No of Projects for display?")
    clients = models.IntegerField("No of Satisfied Clients")
    awards = models.IntegerField("No of Awards Won")


def designers():

    DESIGNER = []
    designers = PortfolioBasic.objects.all().values("name")
    designer_list = list(designers)
    for designer in designer_list:
        for key, value in designer.items():

            choice_value = "(" + str(key) + "," + " " + str(value) + ")"
            # print("value", value)

            DESIGNER.append(choice_value)

    # print("DESIGNER", DESIGNER)
    return DESIGNER


class PortfolioBasic(models.Model):

    designer_id = models.CharField("Designer Id", max_length=200)
    name = models.CharField("Designer Name", max_length=200)
    aboutyourself = models.CharField("About Designer", max_length=500)
    # experience = models.IntegerField("Experience (In Years)")
    portfolio_id = models.CharField("Portfolio Id", max_length=200)
    client_name = models.CharField("Customer Name", max_length=200)
    city_name = models.CharField(
        "City Name", max_length=200, choices=CITY_CHOICES
    )
    type_of_property = models.CharField(
        "Property Type", max_length=200, choices=PROPERTY_CHOICES
    )
    service_type = models.CharField(
        "PropertyplusDecor Service", max_length=200, choices=SERVICE_CHOICES
    )
    duration = models.IntegerField("Duration of Project(in Months)")
    budget = models.IntegerField("Budget (in Lakhs)")
    video = models.URLField("Complete Project Video Youtube Url", blank=True)
    thumbnail = models.URLField(max_length=200)
    image_1 = models.URLField(max_length=200)
    image_2 = models.URLField(max_length=200)
    image_3 = models.URLField(max_length=200)
    image_4 = models.URLField(max_length=200)
    image_5 = models.URLField(max_length=200)
    timecreated = models.CharField(max_length=200, default=default_id_num())


class PortfolioGallery(models.Model):
    portfolio_id = models.CharField("Portfolio Id", max_length=200)
    thumbnail = models.ImageField(upload_to="images/thumbnail/")
    image_1 = models.ImageField(upload_to="images/image_1/")
    image_2 = models.ImageField(upload_to="images/image_2/")
    image_3 = models.ImageField(upload_to="images/image_3/")
    image_4 = models.ImageField(upload_to="images/image_4/")
    image_5 = models.ImageField(upload_to="images/image_5/")
    timecreated = models.CharField(max_length=200, default=default_id_num())


class PortfolioGalleryLinks(models.Model):
    
    portfolio_id = models.CharField("Portfolio Id", max_length=200)
    thumbnail = models.URLField(max_length=200)
    image_1 = models.URLField(max_length=200)
    image_2 = models.URLField(max_length=200)
    image_3 = models.URLField(max_length=200)
    image_4 = models.URLField(max_length=200)
    image_5 = models.URLField(max_length=200)
    timecreated = models.CharField(max_length=200, default=default_id_num())
    interior = models.ForeignKey(
        Interior, related_name="portfoliogallerylinks", on_delete=models.CASCADE
    )


class Customer_feedback(models.Model):

    PROPERTY_CHOICES = [
        ("1 BHK", "1 BHK"),
        ("2 BHK", "2 BHK"),
        ("3 BHK", "3 BHK"),
        ("4 BHK", "4 BHK"),
        ("5 BHK", "5 BHK"),
        ("6+ BHK", "6+ BHK"),
        ("INDEPENDENT HOUSE", "INDEPENDENT HOUSE"),
    ]
    name = models.CharField("Customer Name", max_length=200)
    designer_name = models.CharField("Designer Name", max_length=200)
    location = models.CharField("Customer Location", max_length=200)
    city = models.CharField("City", max_length=200)
    project_date = models.CharField("Project Date", max_length=200)
    type_of_property = models.CharField(
        "Type of Property", max_length=200, choices=PROPERTY_CHOICES
    )
    video = models.URLField("House Interiors Video", blank=True)
    thumbnail = models.ImageField(upload_to="images/thumbnail/")
    image_1 = models.ImageField(upload_to="images/image_1/")
    image_2 = models.ImageField(upload_to="images/image_2/")
    image_3 = models.ImageField(upload_to="images/image_3/")
    image_4 = models.ImageField(upload_to="images/image_4/")
    image_5 = models.ImageField(upload_to="images/image_5/")
    feedback = models.CharField("Feedback", max_length=200)


class Designs(models.Model):

    designer_id = models.CharField("Designer Id", max_length=200)
    designer_name = models.CharField("Designer Name", max_length=200)
    design_id = models.CharField("Design Id", max_length=200)
    design_image = models.URLField(max_length=200)
    design_type = models.CharField(
        "Design Type", max_length=200, choices=DESIGN_CHOICES
    )
    price = models.IntegerField("Starting Price(in lakhs)")


class DesignGallery(models.Model):

    designer_id = models.CharField("Designer Id", max_length=200)
    design_image = models.ImageField(upload_to="images/image_1/")
    design_type = models.CharField(
        "Design Type", max_length=200, choices=DESIGN_CHOICES
    )
    price = models.IntegerField("Starting Price(in lakhs)")
    

class Online_Consultation(models.Model):

    name = models.CharField("Full Name", max_length=200)
    email_id = models.CharField("Email id", max_length=200)
    phone = models.CharField("Phone No", max_length=200)
    state = models.CharField("State", max_length=200, choices=STATE_CHOICES)
    city = models.CharField("City", max_length=200, choices=CITY_CHOICES)
    zipcode = models.CharField("Zip Code", max_length=200)
    whatsapp = models.BooleanField("Send WhatsApp Update", default=None, null=True)


class Pre_Consultation(models.Model):

    type_of_property = models.CharField(
        "Property Type", max_length=200, choices=PROPERTY_CHOICES
    )
    size_home = models.CharField("BuiltupArea Home(in sqft.)", max_length=200)
    service_type = models.CharField(
        "PropertyplusDecor Service", max_length=200, choices=SERVICE_CHOICES
    )
    budget = models.IntegerField("Budget(in lakhs)")
    possession = models.CharField(
        "Possession of Home", max_length=200, choices=POSSESSION_CHOICES
    )
    communication = models.CharField(
        "Language of Communication", max_length=200, choices=LANGUAGE_CHOICES
    )


class Customer_Review(models.Model):

    name = models.CharField("Customer Name", max_length=200)
    city = models.CharField("City", max_length=200, choices=CITY_CHOICES)
    date = models.DateTimeField(
        "Project Date", default=datetime.datetime.now()
    )
    duration = models.IntegerField("Duration of Project(in months)")
    type_of_property = models.CharField(
        "Property Type", max_length=200, choices=PROPERTY_CHOICES
    )
    service_type = models.CharField(
        "PropertyplusDecor Service", max_length=200, choices=SERVICE_CHOICES
    )
    price = models.IntegerField("Price charged")
    designer_id = models.CharField("Designer Id", max_length=200)
    quality_service = models.FloatField("Quality of Service(Rate(0-5))")
    quality_material = models.FloatField("Quality of Material(Rate(0-5))")
    timeliness = models.FloatField("Completed within Duration(Rate(0-5))")
    price = models.FloatField("Price Vs Work(Rate(0-5))")
    communication = models.FloatField("Communication(Rate(0-5))")
    innovation = models.FloatField("Innovative Design(Rate(0-5))")
    finishing = models.FloatField("Finishing in Work(Rate(0-5))")
    uniqueness = models.FloatField("Unique Designs(Rate(0-5))")
    diverse = models.FloatField("Diverse Designs(Rate(0-5))")
    warranty = models.FloatField("Warranty(Rate(0-5))")
