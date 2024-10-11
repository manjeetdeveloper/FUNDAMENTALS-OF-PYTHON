# Two dictionaries with the same keys but different values
dist1 = {"Name": "Manjeet", "Reg": 12200996}
dist2 = {"Name": "Abhishek", "Reg": 12200123}

# Dictionary Comprehension Syntax

combined_dict = {key: [dist1[key], dist2[key]] for key in dist1}


print(combined_dict)
