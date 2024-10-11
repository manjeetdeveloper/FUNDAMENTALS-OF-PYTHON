# # Dictionaries
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 20, 'c': 30, 'd': 40}

# # Dist convert into list 
# newlist = list(dict1.keys())

# common_keys_list = []

# for key in newlist:
#     if key in dict2:
#         common_keys_list.append(key)


# print("Common keys:", common_keys_list)


data = {
'a': 1,
'b': 2,
'c': 1,
'd': 3,
'e': 2
}

to_remove = 1

keys_to_remove = [key for key, value in data.items() if value == to_remove]

for key in keys_to_remove:
    del data[key]


print(data)