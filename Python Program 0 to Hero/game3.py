# manjeet_response = input("Do you like Python? (yes/no): ")

# if manjeet_response == "yes":
#     attempts = 0
#     max_attempts = 3
    
#     while attempts < max_attempts:
#         # Menu is here 
#         choice = input("\nMenu:\n1: Play\n2: Exit\nEnter your choice (1/2): ")
        
#         if choice == '1':
#             print("You chose to play!")
            
#             # Get two numbers from the user and calculate their sum
#             a = float(input("Enter the first number (a): "))
#             b = float(input("Enter the second number (b): "))
#             print("The sum of a and b is: ", (a + b))
            
#             # Reset the attempts counter after a successful play
#             attempts = 0
        
#         elif choice == '2':
#             print("Goodbye!")
#             break
        
#         else:
#             print("Invalid choice, please select 1 or 2.")
#             attempts += 1
        
#         if attempts == max_attempts:
#             print("You have exceeded the maximum number of attempts. Exiting the program.")
# else:
#     print("Oh, No🫡🫡🫡! Exiting the program.")

manjeet_response = input("Do you like Python? (yes/no): ")

if manjeet_response == "yes":
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        choice = input("\nMenu:\n1: Play\n2: Exit\nEnter your choice (1/2): ")
        if attempts == 0:
            print("\nAttempt 1: Addition")
            a = float(input("Enter the first number (a): "))
            b = float(input("Enter the second number (b): "))
            print("The sum of a and b is: ", (a + b))
        
        elif attempts == 1:
            print("\nAttempt 2: Subtraction")
            a = float(input("Enter the first number (a): "))
            b = float(input("Enter the second number (b): "))
            print("The difference between a and b is: ", (a - b))
        
        elif attempts == 2:
            print("\nAttempt 3: Multiplication")
            a = float(input("Enter the first number (a): "))
            b = float(input("Enter the second number (b): "))
            print("The product of a and b is: ", (a * b))
            break  # Exit after the third attempt
        
        attempts += 1

    if attempts == max_attempts:
        print("You have used all your attempts. Exiting the program.")
else:
    print("Oh, No🫡🫡🫡! Exiting the program.")
