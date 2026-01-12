Economy_class = 200
Business_class = 100
First_class = 50
print("Welcome to Flight Booking System")
_Name_ = input("Enter your name: ")
from datetime import datetime
import sys

try:
    _DOB_ = input("Enter your Date of Birth (DD-MM-YYYY): ")
    date_of_birth = datetime.strptime(_DOB_, "%d-%m-%Y").date()
    print("Your Date of Birth is:", date_of_birth)
except ValueError:
    print("Invalid date format. Please enter in DD-MM-YYYY format.")
    sys.exit(1)

_Contact_num = input("Enter your Number: ")
if len(_Contact_num) == 10:

    _Travel_class = int(input("Please choice the option: \n1. Economy \n2. Business \n3. First Class: "))
    if _Travel_class == 1:
        _Departure_airport = input("Enter your Departure airport: ")
        _Destination_airport = input("Enter your Destination airport: ")
        _departure_date = input("Enter your Date of Birth (DD-MM-YYYY): ")
        _returning_tickets = int(input("Please choice the option: \n1.Yes \n2. No" ))
        if _returning_tickets == 1:
            _returning_date = input("Enter your Date of Birth (DD-MM-YYYY): ")
            try:
                departure_date_obj = datetime.strptime(_departure_date, "%d-%m-%Y").date()
                print("Departure Date: ", departure_date_obj)
                print("_returning_date: ", _returning_date)
            except ValueError:
                print("Invalid departure date. Please enter a valid date.")

        else:
            pass
    elif _Travel_class == 2:
        _Departure_airport = input("Enter your Departure airport: ")
        _Destination_airport = input("Enter your Destination airport: ")
        _departure_date = input("Enter your Date of Birth (DD-MM-YYYY): ")
        _returning_tickets = int(input("Please choice the option: \n1.Yes \n2. No"))
        if _returning_tickets == 1:
            _returning_date = input("Enter your Date of Birth (DD-MM-YYYY): ")
            try:
                departure_date_obj = datetime.strptime(_departure_date, "%d-%m-%Y").date()
                print("Departure Date: ", departure_date_obj)
                print("_returning_date: ", _returning_date)
            except ValueError:
                print("Invalid departure date. Please enter a valid date.")
    else:
        _Departure_airport = input("Enter your Departure airport: ")
        _Destination_airport = input("Enter your Destination airport: ")
        _departure_date = input("Enter your Date of Birth (DD-MM-YYYY): ")
        _returning_tickets = int(input("Please choice the option: \n1.Yes \n2. No"))
        if _returning_tickets == 1:
            _returning_date = input("Enter your Date of Birth (DD-MM-YYYY): ")
            try:
                departure_date_obj = datetime.strptime(_departure_date, "%d-%m-%Y").date()
                print("Departure Date: ", departure_date_obj)
                print("_returning_date: ", _returning_date)
            except ValueError:
                print("Invalid departure date. Please enter a valid date.")

else:
    print("Please enter 10 digits contact number")
