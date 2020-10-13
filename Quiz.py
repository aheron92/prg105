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
    print("Congratulations, you got " + str(correct), "out of 11 correct!")
    if correct == 11 or correct == 10:
        print("You earned an A! Excellent job!")
    elif correct == 9:
        print("You earned a B! Great work!")
    elif correct == 8:
        print("You earned a C! Keep trying!")
    elif correct == 7:
        print("You earned a D, time to practice some more!")
    else:
        print("You earned a F.  Everyone fails at least once in life, just keep practicing and you can succeed!")


main()
