#   1.  Implement a program that takes a number and prints "Buzz" if it's divisible by 3, "Fizz" if it's divisible by 5, and "FizzBuzz" if it's divisible by both. If none of these conditions are met, print the number itself. Use a for loop to handle numbers from 1 to 100.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

        # yaha ham inside loop check kr rhe hai 
        # if num is divisble by both yani 3 and 5  then we print FizzBuzz

         # agar number only 3 se divisibe hoga to Fizz print krega
    elif number % 3 == 0:
        print("Fizz")
        # agar number only 5 se divisibe hoga to BUzz print krega
    elif number % 5 == 0:
        print ("Buzz")    
    # nahi to num print krega 
    else:
        print(number)    