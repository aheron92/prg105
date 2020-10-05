"""
Lesson Objective(s):
-Import a file into a list
-Break apart list items into individual components by splitting strings
-Split strings on a symbol
-Check to see if data is numeric

Assignment:
Download your start file for rainfall:
Import the data from the file. Check to see if the data is valid, if it is not valid, indicate to the user what the
bad data is. Total and average the data, and display formatted results on screen.
"""


def main():
    total = 0.0
    entry = 0
    rainfall = open('rainfall-totals.txt', 'r')
    for line in rainfall:
        line = line.rstrip('\n')
        rain = line.split()
        rain_month = rain[0]
        rain_amount = rain[1].split('.')

        if rain_amount[0].isdigit() and rain_amount[1].isdigit():
            amount = float(rain_amount[0] + "." + rain_amount[1])
            total += float(amount)
            entry += 1
        else:
            print(rain_month, "does not have valid data because")
            print(str(rain[1]), "is not a number")
    rainfall.close()
    print("The total rainfall for", str(entry), "months is", format(total, ',.2f'))
    print("The average rainfall was", format((total/entry), ',.2f'))


main()
