# //FIND THE MISSING NUMBER 

# jab v hma lenth se count ya missing number find krte hai to len +1 krna hot ahai 
# agar yaha ham 2 number miss krte hai to jha ase miss kr rhe hai number se woha uske plhe ka numbre dega 

list= [1,2,3,4,5,6,8]

# n = 6
# here len + 1
n=len(list)+1  
# print(n)

total_sum = n * (n + 1) // 2

list_sum = sum(list)

missing_number = total_sum - list_sum

print("The missing number is:",missing_number)
