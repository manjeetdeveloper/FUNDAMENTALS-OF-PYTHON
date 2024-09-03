age = int(input("Enter your age: "))

while age <= 0:
    print("Invalid input! Please enter a positive age.")
    age = int(input("Enter your age: "))

print(f"Your age is: {age}")
