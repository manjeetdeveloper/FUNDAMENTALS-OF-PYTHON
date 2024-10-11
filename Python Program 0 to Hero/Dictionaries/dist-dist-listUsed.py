
# students = [
#     {
#         "Name": "Manjeet",
#          "subject":{ "Math": 89, "Ssc": 67, "English": 99 }
#     }
# ]
# # print(students.get("subject"))

# info = students.items()
# print("items")



students = [
    {
        "Name": "Manjeet",
        "subject": { "Math": 89, "Ssc": 67, "English": 99 }
    }
]

    
info = students[0]
for x, y in info.items():
    print(f"{x}: {y}")
