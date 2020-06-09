import phonenumbers
from phonenumbers import carrier

mobileNo = input("Enter the mobile number with country code: ")
service_provider = phonenumbers.parse(mobileNo)
print("This number belongs to " + carrier.name_for_number(service_provider,'en') + " network.")
