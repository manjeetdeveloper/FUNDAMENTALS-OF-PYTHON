list = [1, 2, 3, 4, 2, 2, 5, 2, 4, 6, 8, 4]

target_number = 4


count = 0


for number in list:
    # chek kr rhe hai ki  current number is equal to the target
    if number == target_number:

        # agar number target se match kr gay to +1 incremwnt kr denge 
        count +=1
        print(f"The number {target_number} repeat in {count} times in the list.")
        

