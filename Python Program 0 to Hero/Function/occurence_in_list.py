# Write a function that takes a list of strings and returns a dictionary
#  where the keys are the unique strings and the values are the counts of 
# their occurrences in the list.

def occurrences(list):
  
    dict = {}
    for string in list:
       
        if string in dict:
            dict[string] += 1
        else:
            dict[string] = 1  
            
    return dict

list = ["MAnjet", "ANjan", "Ritesh", "Mohan", "Anjali", "Manoj"]
final = occurrences(list)
print(final)
