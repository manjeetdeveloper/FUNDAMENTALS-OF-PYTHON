# def animals_count(heads, legs):  
#     chickens = (4 * heads - legs) // 2
#     rabbits = heads - chickens

#     return chickens, rabbits

# #  By Question 
# heads, legs = 35, 94
# chickens, rabbits = animals_count(heads, legs)
# print(f"Chickens: {chickens}, Rabbits: {rabbits}")


# heads, legs = 23, 70
# chickens, rabbits = animals_count(heads, legs)

# print(f"Chickens: {chickens}, Rabbits: {rabbits}")


# heads, legs = 25, 67
# chickens, rabbits = animals_count(heads, legs)
# print(f"Chickens: {chickens}, Rabbits: {rabbits}")

# heads, legs = 20, 70
# chickens, rabbits = animals_count(heads, legs)
# print(f"Chickens: {chickens}, Rabbits: {rabbits}")



#  if else condition 

heads, legs = 35, 94

if legs % 2 == 0 and 2 * heads <= legs <= 4 * heads: 

    chickens = (4 * heads - legs) // 2
    rabbits = heads - chickens
    result = (chickens, rabbits)
else:
    result = "Enter right Input"

if type(result) == [rabbits , chickens]:
    # if type(result) == tupples

    chickens, rabbits = result
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")
else:
    print(result)
