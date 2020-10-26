import OfficeFurniture


def main():
    cedar = OfficeFurniture.Desk("cedar desk", 12, 250, 3000)
    spruce = OfficeFurniture.Desk("spruce desk", 2, 1500, 3000)
    oak = OfficeFurniture.Desk("oak desk", 5, 450.00, 2, 250)

    print("Item: ", cedar.get_material())
    print("Product: ", cedar.get_category())
    print("Price: ", cedar.get_price())

    print("Item: ", spruce.get_material())
    print("Product: ", spruce.get_category())
    print("Price: ", spruce.get_price())

    print("Item: ", oak.get_material())
    print("Product: ", oak.get_category())
    print("Price: ", oak.get_price())


main()
