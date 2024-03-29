"""Using parallel arrays, create a secret code creator.
Ask the user for text to enter, convert it to the code and write the code to a text file.
 Include punctuation (. , !), space, upper, and lower case letters"""


"""Using parallel arrays, create a secret code creator.
Ask the user for text to enter, convert it to the code and write the code to a text file.
 Include punctuation (. , !), space, upper, and lower case letters"""


def main():
    code = ['Z', 'y', 'X', 'w', 'V', 'u', 'T', '$', 'R', 'q', '%', 'o', '&', 'm', 'L', 'k', 'J', 'i', 'H', 'g',
            'F', 'e', 'D', 'c', 'B', '@', ' ', ',', '.', '!', '?', "'"]

    standard = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', ',', '.', '!', '?', "'"]
    phrase = input("Please enter a phrase to translate into a code: ")
    code_final = ""
    for letter in phrase:
        for item in range(0, len(standard)):
            if letter.upper() == standard[item]:
                code_final += (code[item] + "")
    print(code_final)

    file_variable = open("CodeCreator.txt", "w")
    for item in code_final:
        file_variable.write(str(item) + '\n')
    file_variable.close()


main()
