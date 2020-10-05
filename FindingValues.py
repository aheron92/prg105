"""
Lesson Objective(s):
-Match strings in a list
-Error Checking

Assignment:
Read both files into lists. Print the complete customer information on the screen if they are on both lists.
Do error checking for file names to make sure the files exist (try and except statements.)
"""


def main():
    print("The following accounts are at least 90 days overdue:\n")

    try:
        accounts = open('accounts.txt', 'r')
        for account in accounts:
            account = account.rstrip('\n')
            account.split()
            over = open('over90.txt', 'r')
            for overdue in over:
                overdue = overdue.rstrip('\n')
                overdue.split()
                if account[0] == overdue[0] and account[1] == overdue[1] and account[2] == overdue[2]\
                        and account[3] == overdue[3]:
                    print(account)
            over.close()
        accounts.close()

    except Exception as err:
        print(err)


main()
