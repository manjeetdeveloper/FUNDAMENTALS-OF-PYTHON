# Create a prog that prints a multiplication table for numbers 1 through 10. Use nested for loops to generate and print the table.

# use krnge multiplcation ko nested for loops se 

# 1 ka table :-
#      1 * 1 = 1
#     1 * 2 = 2
#     1 * 3 = 3
#     ......
#     1 * 10 = 10

# 2 ka table :-
#      2 * 1 = 2
#     2 * 2 = 4
#     2 * 3 = 6
#     ......
#     2 * 10 = 20
# ... like this 
for i in range(1,11):
    print(f" Multiplication table {i}: ")
    # j inner loop  esliye liye hai ki multiplication 2 number ke bich hota hai 
    for j in range(1,11):
        result = i *j
        print(f" {i} * {j} = {result}")

        # har table ke bich empty line ke liye 
        print()
