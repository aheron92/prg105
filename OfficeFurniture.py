"""
Lesson Objective(s):
-You will learn how to demonstrate inheritance.

Lesson:
In the first step, you will create a parent class. Create a parent class for Office Furniture. Set the class variables
to be a category (desk, chair, filing cabinet would be examples), material, length, width, height, and price. Include a
method that returns a string about the object. Implement the __str__ method (refer to section 10.2 in your book for
details).

In the second step create a subclass for Desk that includes location_of_drawers (left, right both are options)
and number_drawers. Override the parents __str__ method to include drawer location and count.
Implement each class in a separate file. Import these into your main program. Your main program should implement
and display an instance of each, the parent class and the child class.
"""


class OfficeFurniture(object):

    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def get_category(self):
        return

    def get_material(self):
        return

    def get_length(self):
        return

    def get_width(self):
        return

    def get_height(self):
        return

    def get_price(self):
        return

    def __str__(self):
        line_item = self.__category + self.__material + self.__price
        return line_item


class Desk(OfficeFurniture):

    def __init__(self, location_of_drawers, number_of_drawers, category, material, length, width, height, price):
        super().__init__(category, material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_of_drawers = number_of_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers

    def __str(self):
        line_item2 = self.__category + self.__material + self.__location_of_drawers + self.__number_of_drawers\
                     + self.__price
        return line_item2
