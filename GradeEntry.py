"""Ask the user how many students are in their class. Get the student's name and final grade.
Store the answers in a two-dimensional list, then write the list to the grades.txt file.

Note: the tough part of this assignment is to break the list down to the output file."""
students = int(input("Please enter the number of students you would like to grade:  "))


def main():
    number = []
    outfile = open('grades.txt', 'w')
    for count in range(1, students + 1):
        grades = []
        student = input('Enter the name of the student: ')
        number.append(student)
        number.append(grades)
        grade = input("Enter the final grade of the student: ")
        grades.append(grade)

    for line in number:
        lineout = "'" + line[0] + "', '" + line[1] + "'\n"
        outfile.writelines(lineout)

        outfile.close()


main()
