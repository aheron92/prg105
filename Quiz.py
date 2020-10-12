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
    correct = 0
    print("Enter the number in English which corresponds to the number in Russian.")
    numbers = {'ноль': 'zero', 'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four', 'пять': 'five',
               'шесть': 'six', 'семь': 'seven', 'восемь': 'eight', 'девять': 'nine', 'десять': 'ten'}

    for num in numbers:
        answer = input("What is the equivalent of " + num + " : ")
        answer = answer.lower()
        if numbers[num] == answer:
            print("Correct \n")
            correct += 1
        else:
            print("Incorrect.")
    print("You got " + str(correct))
    if correct == 10 or 9:
        print("A")
    elif correct == 8:
        print("B")
    elif correct == 7:
        print("C")
    elif correct == 6:
        print("D")
    else:
        print("F")


main()
