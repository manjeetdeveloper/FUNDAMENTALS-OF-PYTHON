def game():
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))
        print(f"The sum of a and b  is :", (a +b))
   

def main():
    if input("Do you like Python? (yes/no): ") == "yes":
        while input("Do you want to continue? (y/n): ") == 'y':
            choice = input("\nMenu:\n1: Play\n2: Exit\nEnter your choice (1/2): ")
            if choice == '1':
                print("You chose to play!")
                game()
            
            elif choice == '2':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please select 1 or 2.")
    else:
        print("Oh, No🫡🫡🫡! Exiting the program.")

main()
