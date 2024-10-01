student = {
  "Name": "MAnjeet",
  "Stream": "BCA",
  "Passing": 2025
}

# Print all keyname 
for students in student:
  print(students)
  


  # Print all values in the dictionary, one by one:
for students in student:
  print(student[students])


# values print by using Values Operations 
  for students in student.values():
     print(students)

#  key Methons 
for students in student.keys():
  print(students)


# both keys and values, by using the items() method: Print
  for x, y in student.items():
    print(x, y)
    