#!/usr/bin/env python3


# Let's use a while loop to continue collecting student grades until there are no more to enter and a for loop to write the grades line-by-line:
# def create_grade_report(student_grades):
#     with open('lib/reports/grade_report.txt', 'w') as gr:
#         gr.write(student_grades)

# if __name__ == '__main__':
#     student_grades = input("Student name, grade: ")
#     create_grade_report(student_grades)


def create_grade_report(student_grades):
    with open('lib/reports/grade_report.txt', 'w') as gr:
        for grade in student_grades:
            # add '\n' to write grades on separate lines
            gr.write(grade + '\n')

if __name__ == '__main__':
    student_grades = []

    grade = input("Student name, grade: ")
    while grade:
        student_grades.append(grade)
        # end when no grade is entered
        grade = input("Student name, grade: ")

    create_grade_report(student_grades)
