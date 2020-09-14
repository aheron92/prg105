"""Write a program that asks a user to enter a whole number between 20 and 100.  Send that number to a function
that will validate the number, and if it is not a number between 20 and 100, use a while loop to keep asking the
user for a valid number. Return the number to the main function (hint good_number = validate(num) - use a variable
to store the returned value).

You will also program three functions that determine if the number is divisible by two, by three, and by five.

You will have a final function that puts output on the screen - identifying if the number is divisible by
two, three, and five."""


def main():
    num = int(input("Enter a number between 20 and 100:  "))
    good_number = int(validate(num))
    divisible2(good_number)
    divisible3(good_number)
    divisible5(good_number)


def validate(num):
    while num < 20 or num > 100:
        num = int(input("Invalid number.  Enter a number between 20 and 100:  "))

    return num


def divisible2(good_number):
    if good_number % 2 == 0:
        print(good_number, "is divisible by two.")
    else:
        print(good_number, "is not divisible by two.")


def divisible3(good_number):
    if good_number % 3 == 0:
        print(good_number, "is divisible by three.")
    else:
        print(good_number, "is not divisible by three.")


def divisible5(good_number):
    if good_number % 5 == 0:
        print(good_number, "is divisible by five.")
    else:
        print(good_number, "is not divisible by five.")


main()
