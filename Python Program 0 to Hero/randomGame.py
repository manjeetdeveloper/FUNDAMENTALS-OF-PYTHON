# import random
   
# number_to_guess = random.randint(1, 100)
# attempts = 0

# print("Welcome to 'Guess the Number'!")
# print("I have selected a number between 1 and 100.")
# print("Try to guess it!")

# while True:
#             user_guess = int(input("Enter your guess: "))
#             attempts += 1

            
#             if user_guess < number_to_guess:
#                 print("Too low! Try again.")
#             elif user_guess > number_to_guess:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
#                 break



import random

number_to_guess = random.randint(1, 100)
min_attempts = 0
max_attempts = 3

print("Welcome to 'Guess the Number'!")
print("I have selected a number between 1 and 100.")
print(f"Try to guess it! You have attempts.", (max_attempts))

while min_attempts < max_attempts:
    user_guess = int(input("Enter your guess: "))
    min_attempts += 1

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} in {min_attempts} attempts.")
        break
else:
    print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}.")
