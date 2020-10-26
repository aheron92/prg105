import desk
import OfficeFurniture


def main():
    chair = OfficeFurniture.OfficeFurniture('Chair', 'Oak', '30 inches', '30 inches', '30 inches', '$250.00')
    print(chair)

    desks = desk.Desk('Desk', 'Oak', '30 inches', '30 inches', '30 inches', '$700.00', 'left', '6 drawers')
    print(desks)


main()
