"""You are writing a program to sell tickets to the school play. If the person buying the tickets is a student,
their price is $5.00 per ticket. If the person buying the tickets is a veteran, their price is $7.00 per ticket.
If the person buying the ticket is a sponsor of the play, the price is $2.00 per ticket.

prices by who is purchasing the tickets:

student: $5.00
Veteran: $7.00
Show Sponsor: $2.00
Retiree: $6.00
General public: $10.00

People buying 4 - 8 tickets get a 10% discount.
People buying 9-15 tickets get a 15% discount.
People buying more than 15 tickets get a 20% discount.

Determine who is buying the tickets, how many tickets they want, and display their total cost and average price per
ticket—format as money."""

print("This program will help determine ticket prices based on user input.")
print("Here are the prices based on who is purchasing the tickets:\n")

print("1. Student: $5.00")
print("2. Veteran: $7.00")
print("3. Show Sponsor: $2.00")
print("4. Retiree: $6.00")
print("5. General Public: $10.00 \n")

purchaser = int(input("Please enter the category number that you fit for purchasing tickets: "))
cost = 0

if purchaser == 1:
    cost = 5
elif purchaser == 2:
    cost = 7
elif purchaser == 3:
    cost = 2
elif purchaser == 4:
    cost = 6
elif purchaser == 5:
    cost = 10

tickets_bought = float(input("How many tickets are you buying? "))
discount = 0

if tickets_bought >= 4:
    discount = 0.10
elif tickets_bought <= 15:
    discount = 0.15
elif tickets_bought > 15:
    discount = 0.20
else:
    discount = 0

print("Cost before any discounts were applied: $", format(float(cost * tickets_bought), '.2f'))
print("Your price after all discounts were applied is $",
      format(float(cost * tickets_bought) - (cost * tickets_bought) * discount, '.2f'))
print("Your price per ticket is $",
      format(float((cost * tickets_bought) - (cost * tickets_bought * discount)) / tickets_bought, '.2f'))
