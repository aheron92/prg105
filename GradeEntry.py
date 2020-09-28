"""Ask the user how many students are in their class. Get the student's name and final grade.
Store the answers in a two-dimensional list, then write the list to the grades.txt file.

Note: the tough part of this assignment is to break the list down to the output file."""


def main():
    line = []
    student_grades = []
    count = int(input("How many students do you need to enter grades for? "))
    for student in range(0, count):
        student_name = input("Enter the name of the student " + str(student + 1))
        grade = input("Enter the student's final letter grade: ")
        line.append(student_name)
        line.append(grade)
        student_grades.append(line)
        line = []
    print(student_grades)

    outfile = open("grades.txt", "w")
    for line in student_grades:
        lineout = "'" + line[0] + "', '" + line[1] + "'\n"
        outfile.writelines(lineout)
    outfile.close()


main()
