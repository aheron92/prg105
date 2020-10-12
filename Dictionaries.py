"""
Lesson Objective(s):
-Create dictionaries
-Use for loops with dictionaries

Assignment:
You will be tracking the number of steps someone takes each day for a week. Using a loop, ask them to enter
the date and the number of steps. At the end of the program, you will display the total number of steps taken,
the day with the most steps and the day with the least steps. Print multiple days if they are tied.
"""


def main():
    print("You will be entering the date and the number of steps taken for each day in a week.")
    sunday = int(input("Please enter the number of steps taken on Sunday:  "))
    monday = int(input("Please enter the number of steps taken on Monday:  "))
    tuesday = int(input("Please enter the number of steps taken on Tuesday:  "))
    wednesday = int(input("Please enter the number of steps taken on Wednesday:  "))
    thursday = int(input("Please enter the number of steps taken on Thursday:  "))
    friday = int(input("Please enter the number of steps taken on Friday:  "))
    saturday = int(input("Please enter the number of steps taken on Saturday:  "))
    print("\n")

    steps = {'Sunday': sunday, 'Monday': monday, 'Tuesday': tuesday, 'Wednesday': wednesday, 'Thursday': thursday,
             'Friday': friday, 'Saturday': saturday}

    total = sunday + monday + tuesday + wednesday + thursday + friday + saturday
    average = total / 7
    print("Here is the total amount of steps you made for this week:", format(total, ','))
    print("Here is the average amount of steps you made for this week:", format(average, ',.2f'))
    all_values = steps.values()
    max_values = max(all_values)
    min_values = min(all_values)
    maximum = max(steps, key=steps.get)
    minimum = min(steps, key=steps.get)
    print("The maximum amount of steps made was on", maximum, "which was", format(max_values, ','), "steps.")
    print("The minimum amount of steps made was on", minimum, "which was", format(min_values, ','), "steps.")


main()
