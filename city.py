#!/usr/bin/env python3

# Created by : Ahmad
# Created on : Dec 2021
# This program accepts an address and then prints it again but formatted nicely


def city_address(Addressee, Apt_Number, street_number,
                        street_name, city, province, postal_code = None):
# return the city_address

    if Apt_Number != None:
        city_address = Addressee + "\n " + Apt_Number + " " + street_number + " " + street_name + "\n" + city + " " + province + " " + postal_code[0]
    else:
        city_address = Addressee + "\n " + street_number + " " + street_name+ "\n " + 
        city + " " + province + " " + postal_code

    return city_address


def main():
# gets a users information and prints out their address

    print("printing out your address below")
    Apt_Number = None
    Apt = None
    city_add = None

    Addressee = input("Enter your addressee: ")
    Apt = input("Do you have a apartments? (y/n): ")
    if Apt.upper() == "Y" or Apt.upper() == "YES":
        Apt_Number = input("Enter your apartment: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name: ")
    city = input("Enter your city: ")
    province = input("Enter your province: ")
    postal_code = input("Enter your postal code: ")


    city_add = city_address(Addressee, Apt_Number, street_number, street_name, city, province, postal_code)


    print(city_add)

if __name__ == "__main__":
    main()
