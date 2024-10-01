
# Dictionaries
dict1 = {'Alice': 85, 'Bob': 75, 'Charlie': 95}
dict2 = {'Bob': 80, 'David': 90, 'Alice': 95}

# here new dist created
merged_dict = {}

# Add all elements from dict1
for key, value in dict1.items():
    merged_dict[key] = value

# Add elements from dict2, applying the logic for averaging scores
for key, value in dict2.items():
    if key in merged_dict:
        # If the key exists in both, average the values
        merged_dict[key] = (merged_dict[key] + value) / 2
    else:
        # If the key only exists in dict2, add it directly
        merged_dict[key] = value

# Print the merged dictionary
print(merged_dict)
