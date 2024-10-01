# student_record ={
#     "Name": "Manjeet",
#     "Subject": ["Maths", "Programming", "Web Development","Oops"]
# }

# {
#     "Name": "Anuj",
#     "Subject": ["Maths","Oops"]
# }

# {
#     "Name": "Ritesh",
#     "Subject": ["CA", "Accountent", "Web","C++"]
# }



# print("Name:", student_record["Name"])

# print("Subjects:")
# for  subject in student_record["Subject"]:
#     print(subject)


# List of student records
students = [
    {
        "Name": "Manjeet",
        "Subject": ["Maths", "Programming", "Web Development", "Oops"]
    },
    {
        "Name": "Anuj",
        "Subject": ["Maths", "Oops"]
    },
    {
        "Name": "Ritesh",
        "Subject": ["CA", "Accountant", "Web", "C++"]
    }
]


# here nested loop 
for student in students:
    print("Name:", student["Name"])
    print("Subjects:")

    for subject in student["Subject"]:
        print(subject)
    print()


# second way 
for student in students:
    name = student["Name"]
    Subject = student["Subject"]
    print(f"Name:{name} Subject: {Subject}")