from interiors.models import City, PortfolioBasic, Designs
from django.conf import settings


def portfolio_gallerydata(portfolio_id, property_id, URL_PORTFOLIOGALLERY):
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


def cities():

    CITY = []
    city = City.objects.all().values("name")
    city_list = list(city)
    for city in city_list:
        for key, value in city.items():
            # print("value", value)
            CITY.append(value)

    # print("CITY", CITY)
    return CITY


# def createjsonfile(data):

#     data_json = json.dumps(data, indent=4)

#     filename = settings.DESIGNERS_JSON_PATH + "designers.json"

#     with open(filename, "w") as f:
#         json.dump(data_json, f, indent=2)
#         print("designers.json file is updated")


def designers():

    DESIGNER = []
    designers = PortfolioBasic.objects.all().values("name")
    designer_list = list(designers)
    for designer in designer_list:
        for key, value in designer.items():
            # print("value", value)
            DESIGNER.append(value)

    # print("DESIGNER", DESIGNER)
    return DESIGNER


def designs(myDict):
    if myDict:
        # Filtering Designs
        design_type = myDict['designs']
        designer_name = myDict['designers']

        if myDict['designers'] and myDict['designs'] == "ALL":
            designs = Designs.objects.filter(designer_name=designer_name).values(
                "design_id", "design_image", "design_type", "designer_name", "price")
            designs_list = list(designs)

            print("designs_list", designs_list)
            return designs_list

        elif myDict['designers'] and myDict['designs'] != "ALL":
            designs = Designs.objects.filter(design_type=design_type, designer_name=designer_name).values(
                "design_id", "design_image", "design_type", "designer_name", "price")
            designs_list = list(designs)

            print("designs_list", designs_list)
            return designs_list
        
    else:

        designs = Designs.objects.all().values("design_id", "design_image",
                                               "design_type", "designer_name", "price")
        designs_list = list(designs)

        print("designs_list", designs_list)
        return designs_list


def portfolios(myDict):
    if myDict:
        # Filtering Designs
        propertytype = myDict['property']
        designer = myDict['designers']
        print(designer)
        if propertytype == "ANY TYPE" and designer == "ANY":

            portfolios = PortfolioBasic.objects.all().values(
                "id", "designer_id", "name", "portfolio_id", "client_name", "city_name", "type_of_property", "service_type", "duration", "budget", "video", "thumbnail", "image_1", "image_2", "image_3", "image_4", "image_5")
            portfolios_list = list(portfolios)

            print("portfolios_list", portfolios_list)
            return portfolios_list

        elif propertytype != "ANY TYPE" and designer == "ANY":

            portfolios = PortfolioBasic.objects.filter(type_of_property=propertytype).values(
                "id", "designer_id", "name", "portfolio_id", "client_name", "city_name", "type_of_property", "service_type", "duration", "budget", "video", "thumbnail", "image_1", "image_2", "image_3", "image_4", "image_5")
            portfolios_list = list(portfolios)
            print("portfolios_list", portfolios_list)
            return portfolios_list

        elif designer != "ANY" and propertytype == "ANY TYPE":

            portfolios = PortfolioBasic.objects.filter(name=designer).values(
                "id", "designer_id", "name", "portfolio_id", "client_name", "city_name", "type_of_property", "service_type", "duration", "budget", "video", "thumbnail", "image_1", "image_2", "image_3", "image_4", "image_5")
            portfolios_list = list(portfolios)
            print("portfolios_list", portfolios_list)
            return portfolios_list

        elif designer != "ANY" and propertytype != "ANY TYPE":

            portfolios = PortfolioBasic.objects.filter(name=designer, type_of_property=propertytype).values(
                "id", "designer_id", "name", "portfolio_id", "client_name", "city_name", "type_of_property", "service_type", "duration", "budget", "video", "thumbnail", "image_1", "image_2", "image_3", "image_4", "image_5")
            portfolios_list = list(portfolios)
            print("portfolios_list", portfolios_list)
            return portfolios_list

    else:

        portfolios = PortfolioBasic.objects.all().values(
            "id", "designer_id", "name", "portfolio_id", "client_name", "city_name", "type_of_property", "service_type", "duration", "budget", "video", "thumbnail", "image_1", "image_2", "image_3", "image_4", "image_5")
        portfolios_list = list(portfolios)

        print("portfolios_list", portfolios_list)
        return portfolios_list


def filterdesigns(designtype):
    if designtype:
        #DESIGNS = []
        design_type = str(designtype)
        designs = Designs.objects.filter(design_type=design_type).values(
            "id", "design_id", "design_image", "design_type", "designer_name", "price")
        designs_list = list(designs)

        print("designs_list", designs_list)
        return designs_list
