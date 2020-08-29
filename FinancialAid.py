"""Assignment:
You are writing a program to determine if a student is eligible for financial aid for the next semester. To qualify,
the student must either be a new student or a current student with a GPA of 2.0 or higher.  Additionally, the student
may not have a criminal record for drugs, must enroll in a minimum of six credit hours of classes, and must have a
gross yearly income of less than $50,000.  You will gather information from the student, and you will let them know
if they are eligible for financial aid or not.

Hint: this is a bunch of different types of if statements, not an if-elif-else chain

Assignment Requirements:
Complete and test the program
Upload the program to GitHub
Hand in the link to the GitHub program
View the solution video
Fix and resubmit if necessary"""

print("This program will determine whether you are eligible for financial aid. \n")
print("Please answer the following questions:\n")

msg = "Sorry, you are ineligible to apply for financial aid."

student = input("Are you a new or current student, yes/no? ")
if student == "yes":
    GPA = float(input("What is your current GPA? "))
    if GPA >= 2.00:
        criminal_record = input("Do you have a criminal record involving drugs, yes/no? ")
        if criminal_record == "no":
            credit_hours = int(input("How many credit hours of classes are you taking? "))
            if credit_hours >= 6:
                yearly_income = float(input("What is your gross yearly income? "))
                if yearly_income < 50000:
                    print("You are eligible to apply for financial aid.")
                else:
                    print(msg)
            else:
                print(msg)
        else:
            print(msg)
    else:
        print(msg)
else:
    print(msg)
