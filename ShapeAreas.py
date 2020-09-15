"""Create a menu function called from main that will present the user with the following menu.
This program will find the area of a shape for you.
1. Rectangle
2. Triangle
3. Square
4. Circle
5. Quit
Call a validation function from the main function to validate user input, use a while loop to validate data.
Return the validated number to the main function. Depending on the number selected, ask the user for the appropriate
measurements to calculate area of the specified shape (see the sample output) (Ask the user in the menu and pass
the values to the called function) Call the appropriate function, pass the required values to the function
Return the area to the main function and print it on screen from the main function
The menu should re-display until the user selects quit. Use a while loop in the main
method with a flag to accomplish this. Create a global variable for pi and use it when
calculating the area of a circle."""
PI = 3.14


def main():
    menu_choice = 0
    print("This program will find the area of a shape.")
    while menu_choice != 5:
        display_menu()
        menu_choice = int(input("Please enter the number of your selection: "))
        while menu_choice < 1 or menu_choice > 5:
            menu_choice = int(input("Invalid choice, enter another number: "))
        menu(menu_choice)

    print("\n* * * * * Thank you for using Area Calculator * * * * *")


def display_menu():
    print("\n 1. Rectangle\n 2. Triangle\n 3. Square\n 4. Circle\n 5. Quit \n")


def menu(menu_choice):
    if menu_choice == 1:
        width = int(input("Please enter the width of the rectangle in cm: "))
        length = int(input("Please enter the length of the rectangle in cm: "))
        rectangle_area = width * length
        print("The area of the rectangle is", format(rectangle_area, '.2f'), "square cm.")
    elif menu_choice == 2:
        base = int(input("Please enter the base of the triangle in cm: "))
        height = int(input("Please enter the height of the triangle in cm: "))
        triangle_area = 0.5 * (base * height)
        print("The area of the triangle is", format(triangle_area, '.2f'), "square cm.")
    elif menu_choice == 3:
        square_length = int(input("Please enter the length of one side of the square in cm: "))
        square_area = (square_length * square_length)
        print("The area of the square is", format(square_area, '.2f'), "square cm.")
    elif menu_choice == 4:
        radius = int(input("Please enter the length of the radius of the circle in cm: "))
        circle_area = (PI * radius ** 2)
        print("The area of the circle is", format(circle_area, '.2f'), "square cm")


main()
