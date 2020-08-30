"""Ask your user for their credit score. Tell them if they have Bad, Fair, Good, or Excellent credit.

Assignment Requirements:
Complete and test code, make sure you are getting the green checkmark
Upload the completed program to GitHub
Hand in the link to your first attempt
View the solution
Fix and resubmit your program if necessary"""

print("This program will tell you what your credit score rating is. \n")

credit_score = int(input("What is your credit score? "))

if credit_score >= 720:
    print("Your credit score is excellent!")
elif credit_score >= 690:
    print("Your credit score is good.")
elif credit_score >= 630:
    print("Your credit score is fair.")
else:
    print("Your credit score is bad.")
