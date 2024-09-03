# Create empty lists for student names and marks
student_names = ["Manjeet", "Anuj","Shail","Ayush"]
student_marks = [85,92,78,77]

print("Student names:", student_names)
print("Student marks:", student_marks)


# Adding
print("After Adding new Student_name and Student_makes :- Updated Lists")


student_names.append("RAnjit")
student_marks.append("34")
print("Updated student names:", student_names)
print("Updated student marks:", student_marks)


# student_names.insert(3, 'Anjali')
# student_marks.insert(3, 55)   
# print("Updated student names:", student_names)
# print("Updated student marks:", student_marks)

print("After  Removing  Student_name and Student_makes :- Updated Lists")

student_names.remove("Manjeet")
# print(student_names)
student_marks.remove(85)
# print(student_marks)

print("Updated student names:", student_names)
print("Updated student marks:", student_marks)







