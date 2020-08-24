# A program to help the user create a budget

print("This program will help create a budget for you. First, please answer the following questions: \n")

monthly_income = float(input("\t" "What is your total net monthly income? "))
housing = float(input("\t" "How much do you spend per month on housing? "))
food = float(input("\t" "How much do you spend per month on food? "))
transportation = float(input("\t" "How much do you spend per month on transportation? "))
phone = float(input("\t" "How much do you spend per month on phone bills? "))
utilities = float(input("\t" "How much do you spend per month on utilities? "))
clothing = float(input("\t" "How much do you spend on clothing per month? "))
print("\n")

total_month_spending = float(format(housing + food + transportation + phone + utilities + clothing, '.2f'))

print("Your total monthly spending is: $", format(total_month_spending, '.2f'))

print("\t" "Monthly housing costs take up", format(housing / monthly_income, '.2%'), "of your monthly income.")
print("\t" "Monthly food costs take up", format(food / monthly_income, '.2%'), "of your monthly income.")
print("\t" "Monthly transportation costs take up", format(transportation / monthly_income, '.2%'), "of your monthly income.")
print("\t" "Monthly phone payments take up", format(phone / monthly_income, '.2%'), "of your monthly income.")
print("\t" "Monthly utility costs take up", format(utilities / monthly_income, '.2%'), "of your monthly income.")
print("\t" "Monthly clothing costs take up", format(clothing / monthly_income, '.2%'), "of your monthly income.\n")
money_left_over = format(monthly_income - total_month_spending, '.2f')

print("Based on your answers, you will have $", money_left_over, "in your bank account after your total monthly spending.")
