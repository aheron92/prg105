"""
Lesson Objective(s):
-Write Classes
-Work with class diagrams
-Write get and set methods
-Create instances of a class

Lesson:
Design a class that holds the following personal data: name, address, age, and phone number. Write appropriate accessor
and mutator methods (get and set). Write a program that creates three instances of the class. One instance should hold
your information and the other two should hold your friends or family members' information.  Just add information,
don't get it from the user.  Print the data from each object, make sure to format the output for clarity and ease
of reading.

For this assignment, a class diagram is provided for you. In future assignments, you will have to plan your own
project using class diagrams, do this using word and a single column table. The video also explains what accessors
and mutators are.
"""


class PersonalInformation:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone


names = input("Enter a name:  ")
addresses = input("Enter an address: ")
ages = int(input("Enter an age:  "))
phones = input("Enter a phone number:  ")

information = PersonalInformation(names, addresses, ages, phones)

print("Here is the data you entered:")
print('Name:', information.get_name())
print('Address:', information.get_address())
print('Age:', information.get_age())
print('Phone number:', information.get_phone())



