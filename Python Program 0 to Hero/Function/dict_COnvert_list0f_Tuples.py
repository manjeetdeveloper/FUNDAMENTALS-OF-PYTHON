# Create a function that converts a dictionary into a list of tuples.
#  Each tuple should contain a key-value pair from the dictionary.


dict = {'Name': 'Anjan', 'Age': 21,'City':'Bihar'}

def convert(dict):
    return list(dict.items())

final = convert(dict)
print(final)