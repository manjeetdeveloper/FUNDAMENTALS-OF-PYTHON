dict = {'apple': 1, 'banana': 2, 'cherry': 1, 'date': 3}
new = {}

for key in dict:
    value = dict[key]  #dict['apple'] == 1  yani key apple hai to value ia 1
    if value in new:
        new[value].append(key)
    else:
        new[value] = [key]

print(new)
