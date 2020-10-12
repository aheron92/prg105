"""
Lesson Objective(s):
Create a quiz based on learning the numbers from 1-10 in another language.

Assignment:
Create a dictionary based on the language of your choice with the numbers from 1-10 paired
with the numbers from 1-10 in English. Create a quiz based on this dictionary.
Display the number in a foreign language and ask for the number in English.
Score the test and give the user a letter grade.
"""


def main():
    print("Enter the number in English which corresponds to the number in Russian.")
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    grade_letter = {'A': 10 or 11, 'B': 9, 'C': 8, 'D': 7, 'F': 6 or 5 or 4 or 3 or 2 or 1 or 0}

    zero = input("What is the equivalent of ноль: ")
    if 'zero' in numbers:
        print("Correct")
    else:
        print("Incorrect")
    one = input("What is the equivalent of один: ")
    if 'one' in numbers:
        print("Correct")
    else:
        print("Incorrect")
    two = input("What is the equivalent of два: ")
    if 'two' in numbers:
        print("Correct")
    else:
        print("Incorrect")
    three = input("What is the equivalent of три: ")
    if 'three' in numbers:
        print("Correct")
    else:
        print("Incorrect")
    four = input("What is the equivalent of четыре: ")
    if 'four' in numbers:
        print("Correct")
    else:
        print("Incorrect")
    five = input("What is the equivalent of пять: ")
    if 'five' in numbers:
        print("Correct")
    else:
        print("Incorrect")
    six = input("What is the equivalent of шесть: ")
    if 'six' in numbers:
        print("Correct")
    else:
        print("Incorrect")
    seven = input("What is the equivalent of семь: ")
    if 'seven' in numbers:
        print("Correct")
    else:
        print("Incorrect")
    eight = input("What is the equivalent of восемь: ")
    if 'eight' in numbers:
        print("Correct")
    else:
        print("Incorrect")
    nine = input("What is the equivalent of девять: ")
    if 'nine' in numbers:
        print("Correct")
    else:
        print("Incorrect")
    ten = input("What is the equivalent of десять: ")
    if 'ten' in numbers:
        print("Correct")
    else:
        print("Incorrect")


main()
