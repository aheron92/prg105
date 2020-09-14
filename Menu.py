"""Create a program that presents the user with five choices. The topic could be game characters, food, car packages,
anything you are interest in. You will put a menu on screen, ask the user to enter the number or letter of their
choice, and then call the corresponding function to give the user more information."""


def main():
    print("Select one of the menu options from below to find out more.")
    print("A.  Tacos")
    print("B.  Enchiladas")
    print("C.  Burritos")
    print("D.  Tamales")
    print("E.  Quesadillas")
    choice()


def choice():
    user_choice = input("Please enter the letter of your choice:  ")
    if user_choice == "A":
        print("Tacos.")
        print("We have chicken, shrimp, and beef tacos with various toppings.")
    elif user_choice == "B":
        print("Enchiladas.")
        print("We have chicken and beef enchiladas which comes with our hot or mild sauce.")
    elif user_choice == "C":
        print("Burritos.")
        print("We have grilled steak, chicken, smoked brisket, and 'impossible' burritos.")
    elif user_choice == "D":
        print("Tamales.")
        print("Made with our famous recipe.  Don't eat the husk, please.")
    elif user_choice == "E":
        print("Quesadillas.")
        print("We have cheese, beef, chicken, and egg with sausage quesadillas")
    else:
        print("Invalid, please try again.")


main()
