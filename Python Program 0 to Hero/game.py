attempts = 0
print("You like Python(yes/no): ")
correct_answer = "yes"
# print("Are You Join My class")
# correct_answer1 = "Yes":

while True:
    user_input = input("Enter the correct Ans: ")
    
    if user_input == correct_answer :
        print("Congratulations! You  Chhose right .")
        break
    else:
        attempts += 1
        if attempts >= 3:
            print("Sorry, you've used all your attempts. Game over.")
            break
        else:
            print(f"Incorrect! You have {3- attempts} left.")
