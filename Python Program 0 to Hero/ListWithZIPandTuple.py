# Program of using lists in addition to "for" loop
student_names = ["Manjeet", "Ritesh", "Anuj"]
student_grades = [85, 102, 78]

print("Initial list of students:")
for name, grade in zip(student_names, student_grades):
    print(f"{name}: {grade}")


new_name = "Manjeet"
new_grade = 88
student_names. append(new_name)
student_grades.append(new_grade)

print("\nAdding a new student 'Manjeet' with grade 85:")
for name, grade in zip(student_names, student_grades):
    print(f"{name}: {grade}")
