# Example list
list = [1, 2, 3, 4, 5]

# yaha se roate krna krna pos = 2 se target
positions = 2

# yaha pe position ke number list ke number se  more hai 
positions = positions % len(list)

# yhaa last postion ke elemt ko get krnge 
# yaha pe hame 4 , 5 dega 
frist = list[-positions:]


# jitna bach gya wo number yani list ka item de do  # 1,2,3

# List-slicing :- 
second = list[:-positions] 

rotated_list = frist + second

# Print the result
print(rotated_list)
