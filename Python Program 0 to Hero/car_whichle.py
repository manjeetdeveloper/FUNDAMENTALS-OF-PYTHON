total_vehicles = 20
total_wheels = 104


# range use why :- range is a function it is use generate a sequence of numbers  
# like :- 0 to total_vehicals
# Totally meaning of range is :---- Value generating 

# IF ARE USE IN FOR LOOP ( FUNCTION ------range) :- to ye Possible  check krne ke liye use hot hia  

for cars in range(total_vehicles + 1):
    trucks = total_vehicles - cars

    
    if 4 * cars + 6 * trucks == total_wheels:
        print(f"{cars} cars and {trucks} trucks")
        break
else:
    print("Sorry! 🤷‍♂️🤷‍♂️🤷‍♂️")
