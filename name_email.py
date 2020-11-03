"""
Lesson Objective(s):
-Write a CRUD - Create, Read, Update, Delete application
-Pickle files and save them
-Unpickle and save into data structures

Lesson:
Write a program that keeps names and email addresses in a dictionary as key-value pairs. The program should display a
menu that lets the user look up a person's email address, add a new name and email address, change an existing email
address, and delete an existing name and email address. The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts, it should retrieve the dictionary from the file and
unpickle it.
"""
import pickle
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    try:
        input_file = open("customer_file.dat", 'rb')
        customers = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        print("File not found, please add a customer then quit to create the file")
        customers = {}

    choice = 0

    while choice != QUIT:
        choice = menu()
        if choice == LOOK_UP:
            look_up(customers)
        elif choice == ADD:
            add(customers)
        elif choice == CHANGE:
            change(customers)
        elif choice == DELETE:
            delete(customers)
        elif choice == QUIT:
            save(customers)


def menu():
    print()
    print("Customer phone lookup")
    print("----------------------")
    print("1.  Look up a customer")
    print("2.  Add a new customer")
    print("3.  Change a phone number")
    print("4.  Delete a customer")
    print("5.  Quit the program\n")

    choice = int(input("Enter the number of your choice: "))
    while choice < 1 or choice > 5:
        choice = int(input("Enter a valid choice: "))
    return choice


def look_up(customers):
    name = input("Enter a customer name: ")
    print(customers.get(name, 'was not found.'))


def add(customers):
    name = input("Enter a customer name: ")
    phone = input("Enter customer phone number: ")
    if name not in customers:
        customers[name] = phone
    else:
        print("That entry already exists.")


def change(customers):
    name = input("Enter a customer name: ")
    if name in customers:
        phone = input("Enter the customer's new phone number: ")
        customers[name] = phone
    else:
        print("That customer was not found.")


def delete(customers):
    name = input("Enter a customer name: ")
    if name in customers:
        del customers[name]
    else:
        print("That customer was not found.")


def save(customers):
    print("The data file has been updated with your changes.")
    save_file = open('customer_file.dat', 'wb')
    pickle.dump(customers, save_file)
    save_file.close()


main()
