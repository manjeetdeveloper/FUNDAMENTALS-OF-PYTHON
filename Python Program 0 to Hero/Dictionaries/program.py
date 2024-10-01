# Dictionary definition
student = {
    "Name": "Manjeet",
    "Stream": "BCA",
    "Section": "D2201"
}

# Asking the user for input: Key or Value
search_type = input("Do you want to search for a 'key' or 'value'? ").strip().lower()

if search_type == "key":
    
    key = input("Enter the key you want to check: ").strip()
    
    # Check if the key exists in the dictionary
    if key in student:
        print(f"Key '{key}' exists, and its value is: {student[key]}")
    else:
        print(f"Key '{key}' does not exist in the dictionary.")
    
elif search_type == "value":
   
    value = input("Enter the value you want to check: ").strip()
    
    #
    if value in student.values():
        print(f"Value '{value}' exists in the dictionary.")
    else:
        print(f"Value '{value}' does not exist in the dictionary.")
else:
    print("Invalid input. Please enter either 'key' or 'value'.")
