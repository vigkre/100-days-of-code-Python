student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

# Create an empty dictionary to collect the new values.
student_grades = {}

# Loop through each key in the student_scores dictionary
for name in student_scores:
    # Check what grade the score would get, then add it to student_grades
    if student_scores[name] <= 70:
        student_grades[name] = "Fail"
    elif student_scores[name] > 70 and student_scores[name] <= 80:
        student_grades[name] = "Acceptable"
    elif student_scores[name] > 80 and student_scores[name] <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif student_scores[name] > 90 and student_scores[name] <= 100:
        student_grades[name] = "Outstanding"

print(student_grades)
