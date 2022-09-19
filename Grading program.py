# setting up dictionary
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


# an empty dictionary called student_grades.
student_grades = {}

#  code below to add the grades to student_grades.👇
for key in student_scores:
    if 100 >= student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif 90 >= student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif 80 >= student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# print student grades
print(student_grades)
