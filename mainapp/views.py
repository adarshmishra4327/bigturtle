from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from mainapp.models import Contact, Propertydata,Property,Propertydetaile
from django.core import serializers
from django.db.models import Q 
import json

# Create your views here.
 

def index(request):
    return render(request, './landing/home.html')


def propertylisting(request):
    return render(request, './landing/propertylisting.html')


@csrf_exempt
def addproperty(request):
    if request.method == 'POST':
        

        
        registerdata = Propertydetaile(
            
            propertyarea = request.POST.get('area'),
            propertyname = request.POST.get('propertyname'),
            propertytype = request.POST.get('propertytype'),
            totalunits = request.POST.get('totalunit'),
            availaleunits = request.POST.get('availableunit'),
            state = request.POST.get('state'),
            possassionate=request.POST.get('possassiondate'),
            
            pincode=request.POST.get('pincode'),
            price = request.POST.get('price'),
            status = request.POST.get('status'),
            buildername = request.POST.get('buildername'),
            propertydescription = request.POST.get('description'),
            propertyvideo =request.POST.get('video'),
            propertycondition =request.POST.get('condition'),
            yearbuilt = request.POST.get('yearbuild'),
            electricity = request.POST.get('electricity'),
            ac = request.POST.get('ac'),
            modularkitchen = request.POST.get('modularkitchen'),
            watersupply =request.POST.get('watersupply'),
            lpgpipesupply =request.POST.get('lpgpipesupply'),
            garbagedisposable = request.POST.get('garbagedisposable'),
            wifi = request.POST.get('wifi'),
            clubhouse = request.POST.get('clubhouse'),
            gym = request.POST.get('gym'),
            sketingground = request.POST.get('sketingground'),
            joggingtrack = request.POST.get('joggingtrack'),
            kidsplayarea = request.POST.get('kidsplayarea'),
            powerbackup = request.POST.get('powerbackup'),
            visitingparking = request.POST.get('visitingparking'),
            guiestsuites = request.POST.get('guiestsuites'),
            accesscardentry = request.POST.get('accesscardentry'),
            railwaystation = request.POST.get('railwaysation'),
            metro =request.POST.get('metro'),
            busstation = request.POST.get('busstation'),
            temple = request.POST.get('temple'),
            highways = request.POST.get('highways'),
            hospitals = request.POST.get('hospitals'),
            mall = request.POST.get('mall'),
            school = request.POST.get('school'),
            college = request.POST.get('college'),
            nurshinghome = request.POST.get('nurshinghome'),
            furnished =request.POST.get('Furnished'),
            cooling = request.POST.get('cooling'),
            swimmingpool = request.POST.get('Swimming'),
            thumbnail  = request.FILES['thumbnail'],
            image1  = request.FILES['image1'],
            image2 = request.FILES['image2'],
            image3  = request.FILES['image3'],
            image4 = request.FILES['image4'],
            playground = request.POST.get('playground'),
            
            cctv = request.POST.get('cctv'),
            email = request.POST.get('email'),
            mobileno = request.POST.get('mobileno'),
            propertyaddress = request.POST.get('propertyaddress'),
            builderaddress = request.POST.get('builderaddress')
        
            
            )

        
        registerdata.save()
        print(request.POST.get('mobileno'))
        return HttpResponse('hi')


@csrf_exempt
def searchproperty(request):
    if request.method == 'GET':
        return render(request, './landing/propertysearch.html')

    if request.method == 'POST':
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        possessiondate=request.POST.get('possessiondate')
        propertytype=request.POST.get('propertytype')
        propertystatus=request.POST.get('propertystatus')
        price=request.POST.get('price')
        swimming=request.POST.get('swimming')
        playground=request.POST.get('playground')
        cctv=request.POST.get('cctv')

        


        

        data = Propertydetaile.objects.all()
       

        if (state != ""):
            print(state)
            data = data.filter(state=state)

        if (pincode != ""):
            print(pincode)
            data = data.filter(pincode=pincode)

        if (possessiondate != ""):
            print(possessiondate)
            data = data.filter(possassionate=possessiondate)
            

        if (propertytype != ""):
            print(propertytype)
            data = data.filter(propertytype=propertytype)
           
        if (price != ""):
            print(price)
            data = data.filter(price=price)

        if (propertystatus != ""):
            print(propertystatus)
            data = data.filter(Status=propertystatus)
            
      

        if (swimming != ""):
            print(swimming)
            data = data.filter(swimmingpool=swimming)

     

     

        if (playground != ""):
            print(playground)
            data = data.filter(playground=playground)


        if (cctv != ""):
            print(cctv)
            data = data.filter(cctv=cctv)


        print(data)
        finallist = serializers.serialize('json',data)

        # print(finallist)
        return render(request, './landing/propertysearch.html',{'data':json.loads(finallist)})
        # return HttpResponse(finallist)
        



@csrf_exempt
def detailproperty(request):
    if request.method == 'GET':
        id=request.GET.get('id')
        data = Propertydetaile.objects.filter(pk=id)
        finallist = serializers.serialize('json',data)

        print(finallist)
        return render(request, './landing/detailproperty.html',{'data':json.loads(finallist)})
        # return HttpResponse(finallist)
