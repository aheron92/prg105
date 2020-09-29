
# - Ask the user for the name of the file to import (this should be the file you created in the last program)
# - Use try and except statements to ensure the file is there
# - read the file into python
# - Step through the list (strip the \n!)
# - Convert the coded message to English and display the message on screen


def main():
    print("This program will decode a coded text file.")
    filename = input("Which text file would you like to decode? ")

    code = ['Z', 'y', 'X', 'w', 'V', 'u', 'T', '$', 'R', 'q', '%', 'o', '&', 'm', 'L', 'k', 'J', 'i', 'H', 'g',
            'F', 'e', 'D', 'c', 'B', '@', ' ', ',', '.', '!', '?', "'"]
    standard = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', ',', '.', '!', '?', "'"]
    decode = ""

    try:
        infile = open(filename, 'r')
        for line in infile:
            file_line = line.rstrip()
            for letter in file_line:
                for item in range(0, len(code)):
                    if letter.upper() == code[item] or letter.lower() == code[item]:
                        decode += (standard[item] + "")
        print(decode)
        infile.close()

    except IOError:
        print("An error occurred trying to read the file", filename)
        print("Unfortunately, the file does not exist.")


main()
