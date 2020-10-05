"""
Slice strings
Select specific letters from strings
Use string modification methods

Assignment:
Get a phrase from the user
Split the phrase into a list
Use the first letter of each word to create the acronym
Change the acronym to all caps
Display the acronym on screen
"""


def main():
    print("This program accepts a phrase and returns the acronym.")
    phrase = input("Please enter a phrase to convert:  ")
    phrase_list = phrase.split()
    acronym = ""
    for word in phrase_list:
        acronym += word[0]
    acronym = acronym.upper()
    print(acronym)


main()
