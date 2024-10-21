# How to add two dictionaries

def listdict(list1, dict1):
    list = [i**2 for i in list1]  
    dict = {key: value+1 for key, value in dict1.items()} 
    return list, dict 

list2 = [1, 3, 4, 5]
dict2 = {"a": 1, "b": 2, "c": 3}
print(listdict(list2, dict2))