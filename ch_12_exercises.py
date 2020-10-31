"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 12.1 simple recursion
print("=" * 10, "Section 12.1 simple recursion", "=" * 10)
# 1) Using program 12-2 as an example, create a recursive function.
#    The function should print "Hooray!" the number of times requested
#    by the parameter times_requested


def main():
    message(5)


def message(times):
    if times > 0:
        print('Hooray!')
        message(times - 1)
# 2) Call the function with a parameter value of 5.


main()
# TODO 12.2-12.3 problem solving with recursion
print("=" * 10, "Section 12.2-12.3 problem solving with recursion", "=" * 10)
# 1) Create a function that uses recursion to sum the numbers in a list.
#    The function should have one parameter, the list of numbers
#    and it should return the sum of the list values.
# Hint: Each iteration should remove one item from the list.
# The recursion should end when all items have been removed from the list.


def math_stuff(my_numbers):
    if len(my_numbers) > 1:
        my_numbers[0] = my_numbers[0] + my_numbers[1]
        my_numbers.pop(1)
        print(my_numbers)
        math_stuff(my_numbers)
    else:
        print(my_numbers[0])


# 2) Call the function using the numbers list as a parameter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
math_stuff(numbers)
