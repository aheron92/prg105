"""Write a program that gathers contact information from people. The program should ask the user how many entries
they are going to make, then ask for the Name, phone number, and email address for each person.

You will be writing this information to a file. Separate each value with a comma, and make sure to
include the new line symbol.

Write this program using a function  - you should just need the main function.

Sample screen:

How many people do you want to add to the file? 2
What is the name of the person? Ollie Bear
What is their phone number? 815-555-1232
What is their email address? olliebear@gmail.com
What is the name of the person? Nessie Monster
What is their phone number? 815-333-1111
What is their email address? nessie_monster@gmail.com

Sample File Output:

Ollie Bear, 815-555-1232, olliebear@gmail.com
Nessie Monster, 815-333-1111, nessie_monster@gmail.com"""


def main():
    entry = int(input("How many people do you want to add to the file? "))
    file_variable = open('AddressBook.txt', 'w')
    for count in range(1, entry + 1):
        print('Enter the data for contact', count, sep=' ')
        person = input("What is the name of the person? ")
        phone_number = input("What is their phone number? ")
        email = input("What is the their email address? ")

        file_variable.write(person + ', ')
        file_variable.write(phone_number + ', ')
        file_variable.write(email + '\n')
    file_variable.close()

    file_data = open('AddressBook.txt', 'r')
    counter = 0
    for line in open('AddressBook.txt'):
        counter += 1
        print(line)
    file_data.close()


main()
