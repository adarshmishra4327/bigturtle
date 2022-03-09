import requests
from numpy import mod
from listing.models import Listing


def get_recent_listings(URL_LISTING):

    home = []
    r = requests.get(URL_LISTING)
    jsondata = r.json()
    datalength = len(jsondata)
    if datalength > 5:

        start = datalength - 5

        for i in range(start, datalength):

            home.append(jsondata[i])

    else:
        for i in range(0, datalength):

            home.append(jsondata[i])

    return home


def get_home_details(pk):

    home = []
    datalength = 0

    home = Listing.objects.filter(id=pk).values(
        "id",
        "gallery_links__thumbnail",
        "gallery_links__status",
        "gallery_links__property_name",
        "gallery_links__property_id",
        "gallery_links__image_1",
        "gallery_links__image_2",
        "gallery_links__image_3",
        "gallery_links__image_4",
        "gallery_links__image_5",
        "basic__project_area",
        "basic__total_units",
        "basic__available_units",
        "basic__total_no_of_towers",
        "basic__total_no_of_floors",
        "basic__approved_by",
        "basic__launch_year",
        "basic__commencement_certificate",
        "basic__name",
        "basic__status",
        "basic__propertytype",
        "location__location",
        "location__State",
        "location__City",
        "location__Longitude",
        "location__Latitude",
        "features__pet_friendly",
        "features__furnished",
        "features__cooling",
        "features__parking",
        "features__mailbox",
        "features__city_view",
        "features__yoga_room",
        "features__swimming_pool",
        "features__badminton_court",
        "features__squash_court",
        "features__snooker_table",
        "features__basketball_court",
        "features__multipurpose_court",
        "features__outdoor_gym",
        "features__amphitheatre",
        "features__childs_playarea",
        "features__srcitizen_area",
        "features__cycling_track",
        "details__property_id",
        "details__builder_name",
        "details__sold_projects",
        "details__completed_projects",
        "details__ongoing_projects",
        "details__name",
        "details__status",
        "details__propertytype",
        "details__price",
        "details__price_withunit",
        "details__converted_price",
        "details__mortgage",
        "details__description",
        "details__space",
        "details__video",
        "details__beds",
        "details__bathrooms",
        "details__condition",
        "details__year_built",
    )

    return home


def process_gallerydata(property_name, property_id, URL_GALLERY):
    gallery = {}
    inputdata = requests.get(URL_GALLERY)
    inputdata_json = inputdata.json()
    dataset_length = len(inputdata_json)

    for i in range(0, dataset_length):

        if (
            inputdata_json[i]["property_name"] == property_name
            and inputdata_json[i]["property_id"] == property_id
        ):

            gallery["property_name"] = inputdata_json[i]["property_name"]
            gallery["property_id"] = inputdata_json[i]["property_id"]
            gallery["status"] = inputdata_json[i]["status"]
            gallery["thumbnail"] = inputdata_json[i]["thumbnail"]
            gallery["image_1"] = inputdata_json[i]["image_1"]
            gallery["image_2"] = inputdata_json[i]["image_2"]
            gallery["image_3"] = inputdata_json[i]["image_3"]
            gallery["image_4"] = inputdata_json[i]["image_4"]
            gallery["image_5"] = inputdata_json[i]["image_5"]

    return gallery


def get_commercial():

    home = []
    datalength = Listing.objects.all().order_by("-id").count()

    for i in range(0, datalength):

        temp = (
            Listing.objects.filter(details__propertytype="COMMERCIAL")
            .order_by("-id")[i : (i + 1)]
            .values(
                "id",
                "gallery_links__thumbnail",
                "gallery_links__status",
                "gallery_links__property_name",
                "gallery_links__property_id",
                "gallery_links__image_1",
                "gallery_links__image_2",
                "gallery_links__image_3",
                "gallery_links__image_4",
                "gallery_links__image_5",
                "basic__project_area",
                "basic__total_units",
                "basic__available_units",
                "basic__total_no_of_towers",
                "basic__total_no_of_floors",
                "basic__approved_by",
                "basic__launch_year",
                "basic__commencement_certificate",
                "basic__name",
                "basic__status",
                "basic__propertytype",
                "location__location",
                "location__State",
                "location__City",
                "location__Longitude",
                "location__Latitude",
                "features__pet_friendly",
                "features__furnished",
                "features__cooling",
                "features__parking",
                "features__mailbox",
                "features__city_view",
                "features__yoga_room",
                "features__swimming_pool",
                "features__badminton_court",
                "features__squash_court",
                "features__snooker_table",
                "features__basketball_court",
                "features__multipurpose_court",
                "features__outdoor_gym",
                "features__amphitheatre",
                "features__childs_playarea",
                "features__srcitizen_area",
                "features__cycling_track",
                "details__property_id",
                "details__builder_name",
                "details__sold_projects",
                "details__completed_projects",
                "details__ongoing_projects",
                "details__name",
                "details__status",
                "details__propertytype",
                "details__price",
                "details__price_withunit",
                "details__converted_price",
                "details__mortgage",
                "details__description",
                "details__space",
                "details__video",
                "details__beds",
                "details__bathrooms",
                "details__condition",
                "details__year_built",
            )
        )
        print("datalength", datalength)
        if len(temp):
            home.append(temp)

    return home


def get_home():

    home = []
    datalength = Listing.objects.all().order_by("-id").count()
    print("datalength", datalength)

    for i in range(0, datalength):

        temp = (
            Listing.objects.all()
            .order_by("-id")[i : (i + 1)]
            .values(
                "id",
                "gallery_links__thumbnail",
                "gallery_links__status",
                "gallery_links__property_name",
                "gallery_links__property_id",
                "gallery_links__image_1",
                "gallery_links__image_2",
                "gallery_links__image_3",
                "gallery_links__image_4",
                "gallery_links__image_5",
                "basic__project_area",
                "basic__total_units",
                "basic__available_units",
                "basic__total_no_of_towers",
                "basic__total_no_of_floors",
                "basic__approved_by",
                "basic__launch_year",
                "basic__commencement_certificate",
                "basic__name",
                "basic__status",
                "basic__propertytype",
                "location__location",
                "location__State",
                "location__City",
                "location__Longitude",
                "location__Latitude",
                "features__pet_friendly",
                "features__furnished",
                "features__cooling",
                "features__parking",
                "features__mailbox",
                "features__city_view",
                "features__yoga_room",
                "features__swimming_pool",
                "features__badminton_court",
                "features__squash_court",
                "features__snooker_table",
                "features__basketball_court",
                "features__multipurpose_court",
                "features__outdoor_gym",
                "features__amphitheatre",
                "features__childs_playarea",
                "features__srcitizen_area",
                "features__cycling_track",
                "details__property_id",
                "details__builder_name",
                "details__sold_projects",
                "details__completed_projects",
                "details__ongoing_projects",
                "details__name",
                "details__status",
                "details__propertytype",
                "details__price",
                "details__price_withunit",
                "details__mortgage",
                "details__converted_price",
                "details__description",
                "details__space",
                "details__video",
                "details__beds",
                "details__bathrooms",
                "details__condition",
                "details__year_built",
            )
        )
        print("temp", len(temp))
        if len(temp) > 0:
            home.append(temp)

    return home


def get_apartments():

    home = []
    datalength = Listing.objects.all().order_by("-id").count()
    print("datalength", datalength)

    for i in range(0, datalength):

        temp = (
            Listing.objects.filter(details__propertytype="APARTMENT")
            .order_by("-id")[i : (i + 1)]
            .values(
                "id",
                "gallery_links__thumbnail",
                "gallery_links__status",
                "gallery_links__property_name",
                "gallery_links__property_id",
                "gallery_links__image_1",
                "gallery_links__image_2",
                "gallery_links__image_3",
                "gallery_links__image_4",
                "gallery_links__image_5",
                "basic__project_area",
                "basic__total_units",
                "basic__available_units",
                "basic__total_no_of_towers",
                "basic__total_no_of_floors",
                "basic__approved_by",
                "basic__launch_year",
                "basic__commencement_certificate",
                "basic__name",
                "basic__status",
                "basic__propertytype",
                "location__location",
                "location__State",
                "location__City",
                "location__Longitude",
                "location__Latitude",
                "features__pet_friendly",
                "features__furnished",
                "features__cooling",
                "features__parking",
                "features__mailbox",
                "features__city_view",
                "features__yoga_room",
                "features__swimming_pool",
                "features__badminton_court",
                "features__squash_court",
                "features__snooker_table",
                "features__basketball_court",
                "features__multipurpose_court",
                "features__outdoor_gym",
                "features__amphitheatre",
                "features__childs_playarea",
                "features__srcitizen_area",
                "features__cycling_track",
                "details__property_id",
                "details__builder_name",
                "details__sold_projects",
                "details__completed_projects",
                "details__ongoing_projects",
                "details__name",
                "details__status",
                "details__propertytype",
                "details__price",
                "details__price_withunit",
                "details__mortgage",
                "details__converted_price",
                "details__description",
                "details__space",
                "details__video",
                "details__beds",
                "details__bathrooms",
                "details__condition",
                "details__year_built",
            )
        )
        print("temp", len(temp))
        if len(temp) > 0:
            home.append(temp)

    return home


def get_villas():

    home = []
    datalength = Listing.objects.all().order_by("-id").count()
    print("datalength", datalength)

    for i in range(0, datalength):

        temp = (
            Listing.objects.filter(details__propertytype="VILLA")
            .order_by("-id")[i : (i + 1)]
            .values(
                "id",
                "gallery_links__thumbnail",
                "gallery_links__status",
                "gallery_links__property_name",
                "gallery_links__property_id",
                "gallery_links__image_1",
                "gallery_links__image_2",
                "gallery_links__image_3",
                "gallery_links__image_4",
                "gallery_links__image_5",
                "basic__project_area",
                "basic__total_units",
                "basic__available_units",
                "basic__total_no_of_towers",
                "basic__total_no_of_floors",
                "basic__approved_by",
                "basic__launch_year",
                "basic__commencement_certificate",
                "basic__name",
                "basic__status",
                "basic__propertytype",
                "location__location",
                "location__State",
                "location__City",
                "location__Longitude",
                "location__Latitude",
                "features__pet_friendly",
                "features__furnished",
                "features__cooling",
                "features__parking",
                "features__mailbox",
                "features__city_view",
                "features__yoga_room",
                "features__swimming_pool",
                "features__badminton_court",
                "features__squash_court",
                "features__snooker_table",
                "features__basketball_court",
                "features__multipurpose_court",
                "features__outdoor_gym",
                "features__amphitheatre",
                "features__childs_playarea",
                "features__srcitizen_area",
                "features__cycling_track",
                "details__property_id",
                "details__builder_name",
                "details__sold_projects",
                "details__completed_projects",
                "details__ongoing_projects",
                "details__name",
                "details__status",
                "details__propertytype",
                "details__price",
                "details__price_withunit",
                "details__mortgage",
                "details__converted_price",
                "details__description",
                "details__space",
                "details__video",
                "details__beds",
                "details__bathrooms",
                "details__condition",
                "details__year_built",
            )
        )
        print("temp", len(temp))
        if len(temp) > 0:
            home.append(temp)

    return home


def get_residential():

    home = []
    datalength = Listing.objects.all().order_by("-id").count()
    print("datalength", datalength)

    for i in range(0, datalength):

        temp = (
            Listing.objects.filter(details__propertytype="RESIDENTIAL")
            .order_by("-id")[i : (i + 1)]
            .values(
                "id",
                "gallery_links__thumbnail",
                "gallery_links__status",
                "gallery_links__property_name",
                "gallery_links__property_id",
                "gallery_links__image_1",
                "gallery_links__image_2",
                "gallery_links__image_3",
                "gallery_links__image_4",
                "gallery_links__image_5",
                "basic__project_area",
                "basic__total_units",
                "basic__available_units",
                "basic__total_no_of_towers",
                "basic__total_no_of_floors",
                "basic__approved_by",
                "basic__launch_year",
                "basic__commencement_certificate",
                "basic__name",
                "basic__status",
                "basic__propertytype",
                "location__location",
                "location__State",
                "location__City",
                "location__Longitude",
                "location__Latitude",
                "features__pet_friendly",
                "features__furnished",
                "features__cooling",
                "features__parking",
                "features__mailbox",
                "features__city_view",
                "features__yoga_room",
                "features__swimming_pool",
                "features__badminton_court",
                "features__squash_court",
                "features__snooker_table",
                "features__basketball_court",
                "features__multipurpose_court",
                "features__outdoor_gym",
                "features__amphitheatre",
                "features__childs_playarea",
                "features__srcitizen_area",
                "features__cycling_track",
                "details__property_id",
                "details__builder_name",
                "details__sold_projects",
                "details__completed_projects",
                "details__ongoing_projects",
                "details__name",
                "details__status",
                "details__propertytype",
                "details__price",
                "details__price_withunit",
                "details__converted_price",
                "details__mortgage",
                "details__description",
                "details__space",
                "details__video",
                "details__beds",
                "details__bathrooms",
                "details__condition",
                "details__year_built",
            )
        )
        print("temp", len(temp))
        if len(temp) > 0:
            home.append(temp)

    return home


def get_duplex():

    home = []
    datalength = Listing.objects.all().order_by("-id").count()
    print("datalength", datalength)

    for i in range(0, datalength):

        temp = (
            Listing.objects.filter(details__propertytype="DUPLEX")
            .order_by("-id")[i : (i + 1)]
            .values(
                "id",
                "gallery_links__thumbnail",
                "gallery_links__status",
                "gallery_links__property_name",
                "gallery_links__property_id",
                "gallery_links__image_1",
                "gallery_links__image_2",
                "gallery_links__image_3",
                "gallery_links__image_4",
                "gallery_links__image_5",
                "basic__project_area",
                "basic__total_units",
                "basic__available_units",
                "basic__total_no_of_towers",
                "basic__total_no_of_floors",
                "basic__approved_by",
                "basic__launch_year",
                "basic__commencement_certificate",
                "basic__name",
                "basic__status",
                "basic__propertytype",
                "location__location",
                "location__State",
                "location__City",
                "location__Longitude",
                "location__Latitude",
                "features__pet_friendly",
                "features__furnished",
                "features__cooling",
                "features__parking",
                "features__mailbox",
                "features__city_view",
                "features__yoga_room",
                "features__swimming_pool",
                "features__badminton_court",
                "features__squash_court",
                "features__snooker_table",
                "features__basketball_court",
                "features__multipurpose_court",
                "features__outdoor_gym",
                "features__amphitheatre",
                "features__childs_playarea",
                "features__srcitizen_area",
                "features__cycling_track",
                "details__property_id",
                "details__builder_name",
                "details__sold_projects",
                "details__completed_projects",
                "details__ongoing_projects",
                "details__name",
                "details__status",
                "details__propertytype",
                "details__price",
                "details__price_withunit",
                "details__converted_price",
                "details__mortgage",
                "details__description",
                "details__space",
                "details__video",
                "details__beds",
                "details__bathrooms",
                "details__condition",
                "details__year_built",
            )
        )
        print("temp", len(temp))
        if len(temp) > 0:
            home.append(temp)

    return home


def get_plots():

    home = []
    datalength = Listing.objects.all().order_by("-id").count()
    print("datalength", datalength)

    for i in range(0, datalength):

        temp = (
            Listing.objects.filter(details__propertytype="PLOTS")
            .order_by("-id")[i : (i + 1)]
            .values(
                "id",
                "gallery_links__thumbnail",
                "gallery_links__status",
                "gallery_links__property_name",
                "gallery_links__property_id",
                "gallery_links__image_1",
                "gallery_links__image_2",
                "gallery_links__image_3",
                "gallery_links__image_4",
                "gallery_links__image_5",
                "basic__project_area",
                "basic__total_units",
                "basic__available_units",
                "basic__total_no_of_towers",
                "basic__total_no_of_floors",
                "basic__approved_by",
                "basic__launch_year",
                "basic__commencement_certificate",
                "basic__name",
                "basic__status",
                "basic__propertytype",
                "location__location",
                "location__State",
                "location__City",
                "location__Longitude",
                "location__Latitude",
                "features__pet_friendly",
                "features__furnished",
                "features__cooling",
                "features__parking",
                "features__mailbox",
                "features__city_view",
                "features__yoga_room",
                "features__swimming_pool",
                "features__badminton_court",
                "features__squash_court",
                "features__snooker_table",
                "features__basketball_court",
                "features__multipurpose_court",
                "features__outdoor_gym",
                "features__amphitheatre",
                "features__childs_playarea",
                "features__srcitizen_area",
                "features__cycling_track",
                "details__property_id",
                "details__builder_name",
                "details__sold_projects",
                "details__completed_projects",
                "details__ongoing_projects",
                "details__name",
                "details__status",
                "details__propertytype",
                "details__price",
                "details__price_withunit",
                "details__mortgage",
                "details__converted_price",
                "details__description",
                "details__space",
                "details__video",
                "details__beds",
                "details__bathrooms",
                "details__condition",
                "details__year_built",
            )
        )
        print("temp", len(temp))
        if len(temp) > 0:
            home.append(temp)

    return home


def get_recent_123():

    lastone = (
        Listing.objects.all()
        .order_by("-id")[0:1]
        .values(
            "id",
            "gallery_links__thumbnail",
            "gallery_links__status",
            "gallery_links__property_name",
            "gallery_links__property_id",
            "gallery_links__image_1",
            "gallery_links__image_2",
            "gallery_links__image_3",
            "gallery_links__image_4",
            "gallery_links__image_5",
            "basic__project_area",
            "basic__total_units",
            "basic__available_units",
            "basic__total_no_of_towers",
            "basic__total_no_of_floors",
            "basic__approved_by",
            "basic__launch_year",
            "basic__commencement_certificate",
            "basic__name",
            "basic__status",
            "basic__propertytype",
            "location__location",
            "location__State",
            "location__City",
            "location__Longitude",
            "location__Latitude",
            "features__pet_friendly",
            "features__furnished",
            "features__cooling",
            "features__parking",
            "features__mailbox",
            "features__city_view",
            "features__yoga_room",
            "features__swimming_pool",
            "features__badminton_court",
            "features__squash_court",
            "features__snooker_table",
            "features__basketball_court",
            "features__multipurpose_court",
            "features__outdoor_gym",
            "features__amphitheatre",
            "features__childs_playarea",
            "features__srcitizen_area",
            "features__cycling_track",
            "details__property_id",
            "details__builder_name",
            "details__sold_projects",
            "details__completed_projects",
            "details__ongoing_projects",
            "details__name",
            "details__status",
            "details__propertytype",
            "details__price",
            "details__price_withunit",
            "details__converted_price",
            "details__mortgage",
            "details__description",
            "details__space",
            "details__video",
            "details__beds",
            "details__bathrooms",
            "details__condition",
            "details__year_built",
        )
    )

    lastsecondone = (
        Listing.objects.all()
        .order_by("-id")[2:3]
        .values(
            "id",
            "gallery_links__thumbnail",
            "gallery_links__status",
            "gallery_links__property_name",
            "gallery_links__property_id",
            "gallery_links__image_1",
            "gallery_links__image_2",
            "gallery_links__image_3",
            "gallery_links__image_4",
            "gallery_links__image_5",
            "basic__project_area",
            "basic__total_units",
            "basic__available_units",
            "basic__total_no_of_towers",
            "basic__total_no_of_floors",
            "basic__approved_by",
            "basic__launch_year",
            "basic__commencement_certificate",
            "basic__name",
            "basic__status",
            "basic__propertytype",
            "location__location",
            "location__State",
            "location__City",
            "location__Longitude",
            "location__Latitude",
            "features__pet_friendly",
            "features__furnished",
            "features__cooling",
            "features__parking",
            "features__mailbox",
            "features__city_view",
            "features__yoga_room",
            "features__swimming_pool",
            "features__badminton_court",
            "features__squash_court",
            "features__snooker_table",
            "features__basketball_court",
            "features__multipurpose_court",
            "features__outdoor_gym",
            "features__amphitheatre",
            "features__childs_playarea",
            "features__srcitizen_area",
            "features__cycling_track",
            "details__property_id",
            "details__builder_name",
            "details__sold_projects",
            "details__completed_projects",
            "details__ongoing_projects",
            "details__name",
            "details__status",
            "details__propertytype",
            "details__price",
            "details__price_withunit",
            "details__mortgage",
            "details__converted_price",
            "details__description",
            "details__space",
            "details__video",
            "details__beds",
            "details__bathrooms",
            "details__condition",
            "details__year_built",
        )
    )
    lastthirdone = (
        Listing.objects.all()
        .order_by("-id")[3:4]
        .values(
            "id",
            "gallery_links__thumbnail",
            "gallery_links__status",
            "gallery_links__property_name",
            "gallery_links__property_id",
            "gallery_links__image_1",
            "gallery_links__image_2",
            "gallery_links__image_3",
            "gallery_links__image_4",
            "gallery_links__image_5",
            "basic__project_area",
            "basic__total_units",
            "basic__available_units",
            "basic__total_no_of_towers",
            "basic__total_no_of_floors",
            "basic__approved_by",
            "basic__launch_year",
            "basic__commencement_certificate",
            "basic__name",
            "basic__status",
            "basic__propertytype",
            "location__location",
            "location__State",
            "location__City",
            "location__Longitude",
            "location__Latitude",
            "features__pet_friendly",
            "features__furnished",
            "features__cooling",
            "features__parking",
            "features__mailbox",
            "features__city_view",
            "features__yoga_room",
            "features__swimming_pool",
            "features__badminton_court",
            "features__squash_court",
            "features__snooker_table",
            "features__basketball_court",
            "features__multipurpose_court",
            "features__outdoor_gym",
            "features__amphitheatre",
            "features__childs_playarea",
            "features__srcitizen_area",
            "features__cycling_track",
            "details__property_id",
            "details__builder_name",
            "details__sold_projects",
            "details__completed_projects",
            "details__ongoing_projects",
            "details__name",
            "details__status",
            "details__propertytype",
            "details__price",
            "details__price_withunit",
            "details__converted_price",
            "details__mortgage",
            "details__description",
            "details__space",
            "details__video",
            "details__beds",
            "details__bathrooms",
            "details__condition",
            "details__year_built",
        )
    )

    return lastone, lastsecondone, lastthirdone


def get_similar_listings(pk):

    home_similar_1 = []
    home_similar_2 = []
    propertytype = Listing.objects.filter(id=pk).values(
        "details__propertytype"
    )
    propertytype = propertytype[0]["details__propertytype"]

    l = len(
        Listing.objects.filter(details__propertytype=propertytype).order_by(
            "-id"
        )
    )

    if l > 2:

        home_similar_1 = Listing.objects.filter(
            details__propertytype=propertytype
        )[0:1].values(
            "id",
            "gallery_links__thumbnail",
            "gallery_links__status",
            "gallery_links__property_name",
            "gallery_links__property_id",
            "gallery_links__image_1",
            "gallery_links__image_2",
            "gallery_links__image_3",
            "gallery_links__image_4",
            "gallery_links__image_5",
            "basic__project_area",
            "basic__total_units",
            "basic__available_units",
            "basic__total_no_of_towers",
            "basic__total_no_of_floors",
            "basic__approved_by",
            "basic__launch_year",
            "basic__commencement_certificate",
            "basic__name",
            "basic__status",
            "basic__propertytype",
            "location__location",
            "location__State",
            "location__City",
            "location__Longitude",
            "location__Latitude",
            "features__pet_friendly",
            "features__furnished",
            "features__cooling",
            "features__parking",
            "features__mailbox",
            "features__city_view",
            "features__yoga_room",
            "features__swimming_pool",
            "features__badminton_court",
            "features__squash_court",
            "features__snooker_table",
            "features__basketball_court",
            "features__multipurpose_court",
            "features__outdoor_gym",
            "features__amphitheatre",
            "features__childs_playarea",
            "features__srcitizen_area",
            "features__cycling_track",
            "details__property_id",
            "details__builder_name",
            "details__sold_projects",
            "details__completed_projects",
            "details__ongoing_projects",
            "details__name",
            "details__status",
            "details__propertytype",
            "details__price",
            "details__price_withunit",
            "details__converted_price",
            "details__mortgage",
            "details__description",
            "details__space",
            "details__video",
            "details__beds",
            "details__bathrooms",
            "details__condition",
            "details__year_built",
        )

        home_similar_2 = Listing.objects.filter(
            details__propertytype=propertytype
        )[l - 1 : l].values(
            "id",
            "gallery_links__thumbnail",
            "gallery_links__status",
            "gallery_links__property_name",
            "gallery_links__property_id",
            "gallery_links__image_1",
            "gallery_links__image_2",
            "gallery_links__image_3",
            "gallery_links__image_4",
            "gallery_links__image_5",
            "basic__project_area",
            "basic__total_units",
            "basic__available_units",
            "basic__total_no_of_towers",
            "basic__total_no_of_floors",
            "basic__approved_by",
            "basic__launch_year",
            "basic__commencement_certificate",
            "basic__name",
            "basic__status",
            "basic__propertytype",
            "location__location",
            "location__State",
            "location__City",
            "location__Longitude",
            "location__Latitude",
            "features__pet_friendly",
            "features__furnished",
            "features__cooling",
            "features__parking",
            "features__mailbox",
            "features__city_view",
            "features__yoga_room",
            "features__swimming_pool",
            "features__badminton_court",
            "features__squash_court",
            "features__snooker_table",
            "features__basketball_court",
            "features__multipurpose_court",
            "features__outdoor_gym",
            "features__amphitheatre",
            "features__childs_playarea",
            "features__srcitizen_area",
            "features__cycling_track",
            "details__property_id",
            "details__builder_name",
            "details__sold_projects",
            "details__completed_projects",
            "details__ongoing_projects",
            "details__name",
            "details__status",
            "details__propertytype",
            "details__price",
            "details__price_withunit",
            "details__converted_price",
            "details__mortgage",
            "details__description",
            "details__space",
            "details__video",
            "details__beds",
            "details__bathrooms",
            "details__condition",
            "details__year_built",
        )

    return home_similar_1, home_similar_2


def get_recent_propertytype(pk):

    home_recent = []

    propertytype = Listing.objects.filter(id=pk).values(
        "details__propertytype"
    )
    propertytype = propertytype[0]["details__propertytype"]

    l = len(
        Listing.objects.filter(details__propertytype=propertytype).order_by(
            "-id"
        )
    )

    if l < 6:

        for i in range(0, l):

            home_recent.append(
                Listing.objects.filter(details__propertytype=propertytype)[
                    i : i + 1
                ].values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

    elif l > 6:

        x = l - 6

        for i in range(x, l):

            home_recent = Listing.objects.filter(
                details__propertytype=propertytype
            )[i : i + 1].values(
                "id",
                "gallery_links__thumbnail",
                "gallery_links__status",
                "gallery_links__property_name",
                "gallery_links__property_id",
                "gallery_links__image_1",
                "gallery_links__image_2",
                "gallery_links__image_3",
                "gallery_links__image_4",
                "gallery_links__image_5",
                "basic__project_area",
                "basic__total_units",
                "basic__available_units",
                "basic__total_no_of_towers",
                "basic__total_no_of_floors",
                "basic__approved_by",
                "basic__launch_year",
                "basic__commencement_certificate",
                "basic__name",
                "basic__status",
                "basic__propertytype",
                "location__location",
                "location__State",
                "location__City",
                "location__Longitude",
                "location__Latitude",
                "features__pet_friendly",
                "features__furnished",
                "features__cooling",
                "features__parking",
                "features__mailbox",
                "features__city_view",
                "features__yoga_room",
                "features__swimming_pool",
                "features__badminton_court",
                "features__squash_court",
                "features__snooker_table",
                "features__basketball_court",
                "features__multipurpose_court",
                "features__outdoor_gym",
                "features__amphitheatre",
                "features__childs_playarea",
                "features__srcitizen_area",
                "features__cycling_track",
                "details__property_id",
                "details__builder_name",
                "details__sold_projects",
                "details__completed_projects",
                "details__ongoing_projects",
                "details__name",
                "details__status",
                "details__propertytype",
                "details__price",
                "details__price_withunit",
                "details__converted_price",
                "details__mortgage",
                "details__description",
                "details__space",
                "details__video",
                "details__beds",
                "details__bathrooms",
                "details__condition",
                "details__year_built",
            )

    return home_recent


def get_home_filter(filter_listing):

    home = []
    home1 = []

    if (
        filter_listing["sort_by"] == ""
        or filter_listing["sort_by"] == "Price: Low to High"
    ):

        # Condition 1

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] != ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__status=filter_listing["status"],
                    details__builder_name=filter_listing["builder"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 2

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] == ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__status=filter_listing["status"],
                    details__builder_name=filter_listing["builder"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 3

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] != ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    details__status=filter_listing["status"],
                    details__builder_name=filter_listing["builder"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 4

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] != ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__builder_name=filter_listing["builder"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 5

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] != ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__status=filter_listing["status"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 6

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] == ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__status=filter_listing["status"],
                    details__builder_name=filter_listing["builder"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 7

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] != ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    details__builder_name=filter_listing["builder"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 8

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] != ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    details__status=filter_listing["status"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 9

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] == ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    details__status=filter_listing["status"],
                    details__builder_name=filter_listing["builder"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 10

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] != ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 11

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] == ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__builder_name=filter_listing["builder"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 12

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] == ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__status=filter_listing["status"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 13

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] != ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 14

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] == ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 15

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] == ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    details__status=filter_listing["status"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 16

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] == ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    details__builder_name=filter_listing["builder"],
                )
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 17

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] == ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.all()
                .order_by("details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

    # #####################################################
    # ############ SORT PRICE: HIGH - LOW #################
    # #####################################################

    elif (
        filter_listing["sort_by"] == ""
        or filter_listing["sort_by"] == "Price: High to Low"
    ):

        # Condition 1

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] != ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__status=filter_listing["status"],
                    details__builder_name=filter_listing["builder"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 2

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] != ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__status=filter_listing["status"],
                    details__builder_name=filter_listing["builder"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 3

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] != ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    details__status=filter_listing["status"],
                    details__builder_name=filter_listing["builder"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 4

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] != ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__builder_name=filter_listing["builder"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 5

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] != ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__status=filter_listing["status"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 6

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] == ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__status=filter_listing["status"],
                    details__builder_name=filter_listing["builder"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 7

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] != ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    details__builder_name=filter_listing["builder"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 8

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] != ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    details__status=filter_listing["status"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 9

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] == ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    details__status=filter_listing["status"],
                    details__builder_name=filter_listing["builder"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 10

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] != ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 11

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] == ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__builder_name=filter_listing["builder"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 12

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] == ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                    details__status=filter_listing["status"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 13

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] != ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    details__propertytype=filter_listing["prop_type"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 14

        if (
            filter_listing["location"] != ""
            and filter_listing["location"] != "Any_Location"
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] == ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    location__City=filter_listing["location"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 15

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and filter_listing["status"] != ""
            and filter_listing["status"] != "Any Status"
            and filter_listing["prop_type"] == ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.filter(
                    details__status=filter_listing["status"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 16

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] == ""
            and filter_listing["builder"] != ""
        ):

            home = (
                Listing.objects.filter(
                    details__builder_name=filter_listing["builder"],
                )
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

        # Condition 17

        if (
            (
                filter_listing["location"] == ""
                or filter_listing["location"] == "Any_Location"
            )
            and (
                filter_listing["status"] == ""
                or filter_listing["status"] == "Any Status"
            )
            and filter_listing["prop_type"] == ""
            and (
                filter_listing["builder"] == ""
                or filter_listing["builder"] == "Any Builder"
            )
        ):

            home = (
                Listing.objects.all()
                .order_by("-details__price")
                .values(
                    "id",
                    "gallery_links__thumbnail",
                    "gallery_links__status",
                    "gallery_links__property_name",
                    "gallery_links__property_id",
                    "gallery_links__image_1",
                    "gallery_links__image_2",
                    "gallery_links__image_3",
                    "gallery_links__image_4",
                    "gallery_links__image_5",
                    "basic__project_area",
                    "basic__total_units",
                    "basic__available_units",
                    "basic__total_no_of_towers",
                    "basic__total_no_of_floors",
                    "basic__approved_by",
                    "basic__launch_year",
                    "basic__commencement_certificate",
                    "basic__name",
                    "basic__status",
                    "basic__propertytype",
                    "location__location",
                    "location__State",
                    "location__City",
                    "location__Longitude",
                    "location__Latitude",
                    "features__pet_friendly",
                    "features__furnished",
                    "features__cooling",
                    "features__parking",
                    "features__mailbox",
                    "features__city_view",
                    "features__yoga_room",
                    "features__swimming_pool",
                    "features__badminton_court",
                    "features__squash_court",
                    "features__snooker_table",
                    "features__basketball_court",
                    "features__multipurpose_court",
                    "features__outdoor_gym",
                    "features__amphitheatre",
                    "features__childs_playarea",
                    "features__srcitizen_area",
                    "features__cycling_track",
                    "details__property_id",
                    "details__builder_name",
                    "details__sold_projects",
                    "details__completed_projects",
                    "details__ongoing_projects",
                    "details__name",
                    "details__status",
                    "details__propertytype",
                    "details__price",
                    "details__price_withunit",
                    "details__converted_price",
                    "details__mortgage",
                    "details__description",
                    "details__space",
                    "details__video",
                    "details__beds",
                    "details__bathrooms",
                    "details__condition",
                    "details__year_built",
                )
            )

    return home
