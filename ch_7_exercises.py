"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 7.2 Lists
print("=" * 10, "Section 7.2 lists", "=" * 10)
# 1) Create a list of days of the week, assign it to the variable days, remove """ """ to test
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(days)
# 2) Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )
items = [0] * 5
print(items)
# 3) Print the contents of your days list using the for operator
for day in days:
    print(day)
# 4) Print the list item that holds the value Saturday from the days list by using it's index
index = 6
while index < 7:
    print(days[index])
    index += 1
# 5) Create a variable called size to hold the length of the list days using the len function
size = len(days)
# 6) Concatenate the two following lists together, storing the value in list3 - remove the """ """ to test
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)

# TODO 7.3 List Slicing
print("=" * 10, "Section 7.3 list slicing", "=" * 10)
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# Print work_days
work_days = days[1:6]
print(work_days)

# TODO 7.4 Finding items in Lists with the in Operator
print("=" * 10, "Section 7.4 using the in operator", "=" * 10)
# Test to see if "Tue" is in the list days - display "yes, Tue is in the list" or "no, Tue is not in the list"
if 'Tue' in days:
    print("Yes, 'Tue' in the list.")
else:
    print("No, 'Tue' is not in the list.")

# TODO 7.5 List Methods and Useful Built-in Functions
print("=" * 10, "Section 7.5 list methods and functions", "=" * 10)
# 1) Use append() to append the last three months of the year to the list months.
months = list(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"])
months.append("Oct")
months.append("Nov")
months.append("Dec")
print(months)
# 2) Get the index of "May" from the months list and print it on screen
print(months.index('May'))
# 3) Sort list3 from exercise 7.2 and print the results on screen
print('Original order:', list3)
list3.sort()
print('Sorted order:', list3)
# 4) Reverse the order of list3
list3.reverse()
print('Reversed:', list3)
# 5) Delete the number 5 from list3 and print the list(remember we reversed the list)
list3.remove(5)
print(list3)
# 6) Print the maximum value from list 3
print("The highest value in list 3 is: ", max(list3))

# TODO 7.6 Copying Lists
print("=" * 10, "Section 7.6 copying lists", "=" * 10)
# Copy the list months to the variable months_of_the_year
# Print the values in months_of_the_year
months_of_the_year = []
for month in months:
    months_of_the_year.append(month)
print(months_of_the_year)

# TODO 7.7 Processing lists
print("=" * 10, "Section 7.7 processing lists", "=" * 10)
# 1) Total the values in list3 and print the results
total = 0
for value in list3:
    total += value
print("The total of the elements in list 3 is: ", total)
# 2) Get the average of values in list3 and print the results
average = total / len(list3)
print("The average of the elements is: ", format(average, '.2f'))
# 3) Open the file states.txt in read mode,
infile = open('states.txt', 'r')
# -- read the contents of the file into the list states_list
states = infile.readlines()
infile.close()
# -- print the contents of states_list on screen
index = 0
while index < len(states):
    states[index] = states[index].rstrip('\n')
    index += 1
print(states)

# TODO 7.8 Two-Dimensional Lists
print("=" * 10, "Section 7.8 two-dimensional lists", "=" * 10)
# 1) Create a new two dimensional list that has the months of the year
#     and the days in each month during a non leap year
#     For example, the first entry should be: January, 31

months = [['January, 31'], ['February, 28'], ['March, 31'], ['April, 30'], ['May, 31'], ['June, 30'],
          ['July, 31'], ['August, 31'], ['September, 30'],
          ['October, 31'], ['November, 30'], ['December, 31']]

# 2) Print the contents of the entire list
print(months)
# 3) Print just the values for index 3,0 and 3,1
num_months = 0
month_month = 3
month_day = 0
last_day = 0
while num_months < 2:
    print(months[month_month], months[month_day][last_day])
    month_day += 1
    num_months += 1

# TODO 7.9 Tuples
print("=" * 10, "Section 7.9 tuples", "=" * 10)
# Create a tuple using the months list as its data source
my_tuple = months
print(my_tuple)
