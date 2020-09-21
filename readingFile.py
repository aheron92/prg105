"""Open the file sales_totals
Preview the document in read mode
Read in all the lines using a loop
Strip the newline symbol and convert each line to a float
Add each number to the running total
Count the number of lines
Format and display each number
Outside of the loop format and display the total, the count, and the average
Do this in functions"""


def main():
    total = 0
    entry = 0
    sales_totals = open('sales_totals-1.txt', 'r')
    for line in open('sales_totals-1.txt'):
        file_line = float(line.rstrip())
        total += file_line
        entry = entry + 1
        print(format(file_line, ',.2f'))
    sales_totals.close()

    average = total / entry
    print("Total: ", format(total, ',.2f'))
    print("Number of entries: ", format(entry))
    print("Average: ", format(average, ',.2f'))


main()
