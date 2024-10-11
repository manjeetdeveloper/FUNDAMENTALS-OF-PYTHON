record = [
    
    {'Name':"Manjeet", 'Grade':[45,46,37,34]},
    {'Name':"Anuj", 'Grade':[45,46,37,34]},
    {'Name':"Sashi Verma", 'Grade':[34,44,30,43]},
    {'Name':"Anjali", 'Grade':[4,6,3,3]},
    {'Name':"Anjan", 'Grade':[5,4,7,3]}


]

for students in record:
   
    name=students['Name']
    grade=students['Grade']
    print(f"Name: {name},Grade:{grade}")

