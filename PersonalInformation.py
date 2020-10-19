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
    def __init__(self, name_in, address_in, age_in, phone_in):
        self.__name = name_in
        self.__address = address_in
        self.__age = age_in
        self.__phone = phone_in

    def set_name(self, name_in):
        self.__name = name_in

    def set_address(self, address):
        self.__address = address

    def set_age(self, age_in):
        self.__age = age_in

    def set_phone(self, phone_in):
        self.__phone = phone_in

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def __str__(self):
        return 'Name: ' + self.__name + "\nAddress: " + self.__address + "\nAge: " + self.__age + "\nPhone: "\
               + self.__phone


def main():
    person1 = PersonalInformation('Meri', '8900 Route 14, Crystal Lake', '48', '815-555-5555')
    person2 = PersonalInformation('Fred', '8900 Route 14, Crystal Lake', '75', '123-456-7891')
    person3 = PersonalInformation('Barney', '123 Main Street, Richmond', '28', '111-222-3333')
    print(person1)
    print("------------------------------")
    print(person2)
    print("------------------------------")
    print(person3)
    print("------------------------------")

    person3.set_name("Adam")
    print(person3.get_name())
    print(person3)


main()


