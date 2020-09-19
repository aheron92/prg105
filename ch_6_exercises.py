"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 6.1 Introduction to File Input and Output
print("=" * 10, "Section 6.1 file input and output", "=" * 10)


def main():
    file_variable = open('states.txt', 'r')
    file_variable.close()

    state_capitals = open('capitals.txt', 'w')
    state_capitals.write("Illinois, Springfield\n")
    state_capitals.write("Alaska, Juneau\n")
    state_capitals.write("California, Sacramento\n")
    state_capitals.close()

    states_data = open('states.txt', 'r')
    line1 = states_data.readline()
    line2 = states_data.readline()
    line3 = states_data.readline()
    states_data.close()

    print(line1)
    print(line2)
    print(line3)


main()


# TODO 6.2 Using loops to process files
print("=" * 10, "Section 6.2 use loops to process files", "=" * 10)


def main():
    states_file = open('states.txt', 'r')
    counter = 0
    for line in open('states.txt'):
        counter += 1
        print(line)
    states_file.close()


main()


# TODO 6.3 Processing records
print("=" * 10, "Section 6.3 processing records", "=" * 10)
# You are going to finish the program below to write book information to a file
books = 3      # use this as the number of books to enter


def main():
    books_file = open('books.txt', 'w', 1)
    for count in range(1, books + 1):
        book = input("Enter a title and author of a book: ")
        books_file.write(book + '\n')
        print('Data written to books.txt')
    books_file.close()


main()


# TODO 6.4 Exceptions
print("=" * 10, "Section 6.4 exceptions", "=" * 10)


def main():
    try:
        input("Please enter choose a file. ")

        hero_file = open('superheros.txt', 'r')
        hero_file.close()

    except IOError:
        print("ERROR:  That file doesn't exist.")
        print("Choose a valid file.")


main()
