# Take inputs from the user

section = str(input("Enter Your Section: "))
name = str(input("Enter Your Name: "))
age = int(input("Enter Your Age: "))
marks = int(input("Enter Your Marks: "))

# Print the inputs
print("Your section is: -", section)
print("Your Name is: -", name)
print("Your Age is: -", age)
print("Your Marks is: -", marks)

# Check  conditions
if age < 25:
    print("You are not eligible for enrollment due to age.")
    
if marks < 50:
    print("You have too few marks to be eligible for enrollment.")
