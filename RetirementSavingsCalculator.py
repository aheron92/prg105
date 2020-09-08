"""Write a program that projects yearly income, amount saved towards retirement each year,
and total retirement savings.Assume a 3 percent raise on the starting income each year,
and a 6% yearly return on investment. You will need to ask the user their current age,
at what age they want to retire, what their current income is, what percent of their income they save each year,
and how much they currently have in savings. You will calculate how many years until retirement,
and display the projected income, savings contribution, and total savings each year.

Hints: Assume they will enter a whole number for the percent of income saved and divide it by 100
( for 8 percent - 8/100 = .08).

Sample input with correct results is displayed below.  You will need to use the field size in the format settings to
get everything to line up nicely in table form."""

current_age = int(input("How old are you currently? "))
retirement_age = int(input("At what age do you want to retire? "))
income = float(input("What is your yearly income? $"))
retirement_percent = float(input("What your percent of your income do you want to save? %"))
retirement_savings = float(input("How much money do you currently have in savings? $"))

print("This projection assumes a 3% raise each year and a 6% yearly return on investment.\n")

year = 0

print("Year                 Income                      Savings Contribution                         Total Savings")

while current_age < retirement_age:
    income *= 1.03
    retirement_savings *= 1.06
    contribution = income + (income * (retirement_percent / 100))
    retirement_savings += contribution
    current_age = current_age + 1
    year += 1

    print(format(year, "2,.0f") + format(income, "26,.2f") + format(contribution, "34,.2f")
          + format(retirement_savings, "44,.2f"))
