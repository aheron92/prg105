"""You need to create a program that will have the user enter in the total sales
amount for the day at a coffee shop. The program should ask the user for the total amount of sales,
and include the day in the request. At the end of data entry, tell the user the total sales for the week,
and the average sales per day. You must create a list of the days of the week for the user to step through,
see the example output. """

print("This program will calculate the total amount of sales per week and the average amount of sales per "
      "day of the week. \n")

total = 0
for day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
    day_sale = float(input(f"What were the total sales for {day}? "))
    total += day_sale

print("The total amount of sales per week was ", format(total, '.2f'))
avg = total / 7
print("Your average amount of sales per day was ", format(avg, '.2f'))
