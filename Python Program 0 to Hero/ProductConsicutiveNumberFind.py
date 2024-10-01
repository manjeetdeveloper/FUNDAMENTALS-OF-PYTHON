# You are given a list of integers. Write a program that finds
#  the maximum product of any two consecutive numbers in the list.

# ye ky kr rha hai ki jo largest number hai usko jaise  1 "17"  5  so,, ye 
# 1 or 5 me select krega ki kon largest hai so. 5 largest hai  to 17 * 5 kr dega 


numbers = [1, 17, 5 ,6 ,12, 5, 1 , 8]

max_number = numbers[0] * numbers[1]
# max_number ko 0 se 1 tak chck then chenk all list so preform for loop 
for i in range(len(numbers) -1 ):

    max_number = max(max_number, numbers[i] * numbers[i + 1])

print ("Max_Number", max_number)


