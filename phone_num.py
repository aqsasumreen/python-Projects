# PK is the Region code
# +92 is country code
import phonenumbers
from phonenumbers import timezone , geocoder, carrier
from phonenumbers.phonenumberutil import (
    region_code_for_country_code,
    # region_code_for_number,
    country_code_for_region,
)
num  =input("Enter your phoneNumber with +__ :")
# genertate phone number
phone = phonenumbers.parse(num)
print(phone)
# generate regioncode
rg = region_code_for_country_code(phone.country_code)
# tell  the TimeZone
time = timezone.time_zones_for_number(phone)
print("TimeZone is : ",time)
# TELL the REGION
reg = geocoder.description_for_number(phone , "en")
print("Region is : ",reg)
# tell the CArrier NAME
car = carrier.name_for_number(phone ,"en")
print("Carrier name is : ",car)
print("Region Code is :",rg)
# tell the COUNTRY code for region
print("Country Code is","+",country_code_for_region(rg))
