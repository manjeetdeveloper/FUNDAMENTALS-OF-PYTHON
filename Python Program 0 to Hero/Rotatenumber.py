# Example list
list = [1, 2, 3, 4, 5]

# jaha se rotate krna hai 
positions = 2

positions = positions % len(list)

# Create an empty list for the rotated list
rotated_list = []

# last pos elemt to new empty list me add kro 
for i in range(len(list) - positions, len(list)):
    rotated_list.append(list[i])


# Add the remaining elements to the new list
for i in range(0, len(list) - positions):
    rotated_list.append(list[i])

# Print the result
print(rotated_list)
