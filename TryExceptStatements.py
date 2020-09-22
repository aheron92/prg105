"""Use the program from 6.2 as a start
Open the sales_error.txtPreview the document file as the infile
One of the numbers has an error - use the try and except statement to make it ignore the line with the error,
report it to the screen
Also detect if there is a bad file name, test that by looking for bad file name"""


def main():
    total = 0.0
    try:
        sales_error = open('sales_error.txt', 'r')
        for line in sales_error:
            file_line = float(line.rstrip())
            amount = float(line)
            total += amount
            print(format(file_line, ',.2f'))
        sales_error.close()
        print(format(total, ',.2f'))
    except Exception as err:
        print(err)
        pass

    filename = input("Enter a file name. ")

    try:
        infile = open(filename, 'r')
        contents = infile.read()
        print(contents)
        infile.close()

    except IOError:
        print("An error occurred trying to read the file", filename)
        print("Unfortunately, the file does not exist.")


main()
