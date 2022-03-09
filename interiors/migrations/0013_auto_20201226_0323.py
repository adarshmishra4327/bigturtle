# Generated by Django 3.0 on 2020-12-26 03:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0012_auto_20201226_0238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Customer Name')),
                ('city', models.CharField(choices=[('MUMBAI', 'MUMBAI'), ('DELHI', 'DELHI'), ('BENGALURU', 'BENGALURU'), ('HYDERABAD', 'HYDERABAD'), ('AHMEDABAD', 'AHMEDABAD'), ('CHENNAI', 'CHENNAI'), ('KOLKATA', 'KOLKATA'), ('SURAT', 'SURAT'), ('PUNE', 'PUNE'), ('JAIPUR', 'JAIPUR'), ('LUCKNOW', 'LUCKNOW'), ('KANPUR', 'KANPUR'), ('NAGPUR', 'NAGPUR'), ('INDORE', 'INDORE'), ('THANE', 'THANE'), ('BHOPAL', 'BHOPAL'), ('VISAKHAPATNAM', 'VISAKHAPATNAM'), ('CHINCHWAD', 'CHINCHWAD'), ('PATNA', 'PATNA'), ('VADODARA', 'VADODARA'), ('GHAZIABAD', 'GHAZIABAD'), ('LUDHIANA', 'LUDHIANA'), ('AGRA', 'AGRA'), ('NASHIK', 'NASHIK'), ('RANCHI', 'RANCHI'), ('FARIDABAD', 'FARIDABAD'), ('MEERUT', 'MEERUT'), ('RAJKOT', 'RAJKOT'), ('DOMBIVLI', 'DOMBIVLI'), ('VIRAR', 'VIRAR'), ('VARANASI', 'VARANASI'), ('SRINAGAR', 'SRINAGAR'), ('AURANGABAD', 'AURANGABAD'), ('DHANBAD', 'DHANBAD'), ('AMRITSAR', 'AMRITSAR'), ('NAVI MUMBAI', 'NAVI MUMBAI'), ('ALLAHABAD', 'ALLAHABAD'), ('HOWRAH', 'HOWRAH'), ('GWALIOR', 'GWALIOR'), ('JABALPUR', 'JABALPUR'), ('COIMBATORE', 'COIMBATORE'), ('VIJAYAWADA', 'VIJAYAWADA'), ('JODHPUR', 'JODHPUR'), ('MADURAI', 'MADURAI'), ('RAIPUR', 'RAIPUR'), ('KOTA', 'KOTA'), ('CHANDIGARH', 'CHANDIGARH'), ('GUWAHATI', 'GUWAHATI'), ('SOLAPUR', 'SOLAPUR'), ('MYSORE', 'MYSORE'), ('BHUBANESWAR', 'BHUBANESWAR'), ('THIRUVANATHAPURAM', 'THIRUVANATHAPURAM'), ('DEHRADUN', 'DEHRADUN'), ('JAMMU', 'JAMMU'), ('AGARTALA', 'AGARTALA'), ('KURNOOL', 'KURNOOL'), ('AIZAWL', 'AIZAWL'), ('IMPHAL', 'IMPHAL'), ('PONDICHERRY', 'PONDICHERRY'), ('GANDHINAGAR', 'GANDHINAGAR'), ('SHIMLA', 'SHIMLA'), ('HOSUR', 'HOSUR'), ('AMARAVATI', 'AMARAVATI'), ('GANGTOK', 'GANGTOK'), ('KOTTAYAM', 'KOTTAYAM')], max_length=200, verbose_name='City')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 12, 26, 3, 22, 56, 254572), verbose_name='Project Date')),
                ('duration', models.IntegerField(verbose_name='Duration of Project(in months)')),
                ('type_of_property', models.CharField(choices=[('1 BHK', '1 BHK'), ('2 BHK', '2 BHK'), ('3 BHK', '3 BHK'), ('4 BHK', '4 BHK'), ('5 BHK', '5 BHK'), ('6+ BHK', '6+ BHK'), ('INDEPENDENT HOUSE', 'INDEPENDENT HOUSE')], max_length=200, verbose_name='Property Type')),
                ('service_type', models.CharField(choices=[('MODULAR KITCHEN', 'MODULAR KITCHEN'), ('FULL HOME DESIGN', 'FULL HOME DESIGN'), ('RENOVATION FULL HOME', 'RENOVATION FULL HOME'), ('RENOVATION KITCHEN', 'RENOVATION KITCHEN'), ('RENOVATION LIVING ROOM', 'RENOVATION LIVING ROOM'), ('FURNITURE', 'FURNITURE')], max_length=200, verbose_name='PropertyplusDecor Service')),
                ('designer_id', models.CharField(max_length=200, verbose_name='Designer Id')),
                ('quality_service', models.FloatField(verbose_name='Quality of Service(Rate(0-5))')),
                ('quality_material', models.FloatField(verbose_name='Quality of Material(Rate(0-5))')),
                ('timeliness', models.FloatField(verbose_name='Completed within Duration(Rate(0-5))')),
                ('price', models.FloatField(verbose_name='Price Vs Work(Rate(0-5))')),
                ('communication', models.FloatField(verbose_name='Communication(Rate(0-5))')),
                ('innovation', models.FloatField(verbose_name='Innovative Design(Rate(0-5))')),
                ('finishing', models.FloatField(verbose_name='Finishing in Work(Rate(0-5))')),
                ('uniqueness', models.FloatField(verbose_name='Unique Designs(Rate(0-5))')),
                ('diverse', models.FloatField(verbose_name='Diverse Designs(Rate(0-5))')),
                ('warranty', models.FloatField(verbose_name='Warranty(Rate(0-5))')),
            ],
        ),
        migrations.CreateModel(
            name='Online_Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('email_id', models.CharField(max_length=200, verbose_name='Email id')),
                ('phone', models.CharField(max_length=200, verbose_name='Phone No')),
                ('OTP', models.CharField(max_length=200, verbose_name='Verify-Enter OTP')),
                ('city', models.CharField(choices=[('MUMBAI', 'MUMBAI'), ('DELHI', 'DELHI'), ('BENGALURU', 'BENGALURU'), ('HYDERABAD', 'HYDERABAD'), ('AHMEDABAD', 'AHMEDABAD'), ('CHENNAI', 'CHENNAI'), ('KOLKATA', 'KOLKATA'), ('SURAT', 'SURAT'), ('PUNE', 'PUNE'), ('JAIPUR', 'JAIPUR'), ('LUCKNOW', 'LUCKNOW'), ('KANPUR', 'KANPUR'), ('NAGPUR', 'NAGPUR'), ('INDORE', 'INDORE'), ('THANE', 'THANE'), ('BHOPAL', 'BHOPAL'), ('VISAKHAPATNAM', 'VISAKHAPATNAM'), ('CHINCHWAD', 'CHINCHWAD'), ('PATNA', 'PATNA'), ('VADODARA', 'VADODARA'), ('GHAZIABAD', 'GHAZIABAD'), ('LUDHIANA', 'LUDHIANA'), ('AGRA', 'AGRA'), ('NASHIK', 'NASHIK'), ('RANCHI', 'RANCHI'), ('FARIDABAD', 'FARIDABAD'), ('MEERUT', 'MEERUT'), ('RAJKOT', 'RAJKOT'), ('DOMBIVLI', 'DOMBIVLI'), ('VIRAR', 'VIRAR'), ('VARANASI', 'VARANASI'), ('SRINAGAR', 'SRINAGAR'), ('AURANGABAD', 'AURANGABAD'), ('DHANBAD', 'DHANBAD'), ('AMRITSAR', 'AMRITSAR'), ('NAVI MUMBAI', 'NAVI MUMBAI'), ('ALLAHABAD', 'ALLAHABAD'), ('HOWRAH', 'HOWRAH'), ('GWALIOR', 'GWALIOR'), ('JABALPUR', 'JABALPUR'), ('COIMBATORE', 'COIMBATORE'), ('VIJAYAWADA', 'VIJAYAWADA'), ('JODHPUR', 'JODHPUR'), ('MADURAI', 'MADURAI'), ('RAIPUR', 'RAIPUR'), ('KOTA', 'KOTA'), ('CHANDIGARH', 'CHANDIGARH'), ('GUWAHATI', 'GUWAHATI'), ('SOLAPUR', 'SOLAPUR'), ('MYSORE', 'MYSORE'), ('BHUBANESWAR', 'BHUBANESWAR'), ('THIRUVANATHAPURAM', 'THIRUVANATHAPURAM'), ('DEHRADUN', 'DEHRADUN'), ('JAMMU', 'JAMMU'), ('AGARTALA', 'AGARTALA'), ('KURNOOL', 'KURNOOL'), ('AIZAWL', 'AIZAWL'), ('IMPHAL', 'IMPHAL'), ('PONDICHERRY', 'PONDICHERRY'), ('GANDHINAGAR', 'GANDHINAGAR'), ('SHIMLA', 'SHIMLA'), ('HOSUR', 'HOSUR'), ('AMARAVATI', 'AMARAVATI'), ('GANGTOK', 'GANGTOK'), ('KOTTAYAM', 'KOTTAYAM')], max_length=200, verbose_name='City')),
            ],
        ),
        migrations.DeleteModel(
            name='Online_Consultaion',
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='designer_id',
            field=models.CharField(default='DEZINERngvCkB', max_length=200, verbose_name='Designer id'),
        ),
        migrations.AddField(
            model_name='pre_consultation',
            name='service_type',
            field=models.CharField(choices=[('MODULAR KITCHEN', 'MODULAR KITCHEN'), ('FULL HOME DESIGN', 'FULL HOME DESIGN'), ('RENOVATION FULL HOME', 'RENOVATION FULL HOME'), ('RENOVATION KITCHEN', 'RENOVATION KITCHEN'), ('RENOVATION LIVING ROOM', 'RENOVATION LIVING ROOM'), ('FURNITURE', 'FURNITURE')], default=1, max_length=200, verbose_name='PropertyplusDecor Service'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='designs',
            name='design_id',
            field=models.CharField(default='DESNFlu700', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='designs',
            name='price',
            field=models.IntegerField(verbose_name='Starting Price(in lakhs)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 3, 22, 56, 251572), verbose_name='Project Date'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_id',
            field=models.CharField(default='PORT4FAu3q', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='timecreated',
            field=models.CharField(default='1608952976', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='type_of_property',
            field=models.CharField(choices=[('1 BHK', '1 BHK'), ('2 BHK', '2 BHK'), ('3 BHK', '3 BHK'), ('4 BHK', '4 BHK'), ('5 BHK', '5 BHK'), ('6+ BHK', '6+ BHK'), ('INDEPENDENT HOUSE', 'INDEPENDENT HOUSE')], max_length=200, verbose_name='Property Type'),
        ),
        migrations.AlterField(
            model_name='pre_consultation',
            name='budget',
            field=models.IntegerField(verbose_name='Budget(in lakhs)'),
        ),
        migrations.AlterField(
            model_name='pre_consultation',
            name='size_home',
            field=models.CharField(max_length=200, verbose_name='BuiltupArea Home(in sqft.)'),
        ),
    ]
