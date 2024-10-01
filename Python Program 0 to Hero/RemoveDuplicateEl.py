list = [1, 3, 2, 3, 4, 1, 5]
Checker_Box = []

for number in list:
    #  check krnge ki if element is not already in Checker_Box 
    if number not in Checker_Box:
        Checker_Box.append(number)

print(Checker_Box)
