import OfficeFurniture


class Desk(OfficeFurniture.OfficeFurniture):

    def __init__(self, category, material, length, width, height, price, location, number):
        self.__location_of_drawers = location
        self.__number_of_drawers = number

        OfficeFurniture.OfficeFurniture.__init__(self, category, material, length, width, height, price)

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def get_number_of_drawers(self):
        return self.__number_of_drawers

    def __str__(self):
        return "\nCategory: " + self.get_category() + "\nMaterial: " + self.get_material()\
               + "\nLength: " + self.get_length() + "\nWidth: " + self.get_width()\
               + "\nHeight: " + self.get_height() + "\nPrice: " + self.get_price()\
               + "\nLocation of drawers: " + self.__location_of_drawers\
               + "\nNumber of drawers: " + self.__number_of_drawers


