student = {
  "Name": "MAnjeet",
  "Stream": "BCA",
  "Passing": 2025
}

# additem
student["CGPA"] = "8.1"
print(student)

#  Remove items From Dictionaries
student.pop("model")
print(student)

# popitems  me last se remove krega 
student.popitem()
print(student)

# delete 
del student["Stream"]
print(student)

