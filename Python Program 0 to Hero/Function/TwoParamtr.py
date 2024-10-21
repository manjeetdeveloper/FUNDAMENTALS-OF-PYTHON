#Taking two Parameters and one as a defult argument and return this value 

def numbers(a, b=5):
    return a + b    




result1 = numbers(10)        
result2 = numbers(10, 6)  # yaha pe b ka value b=5 nahi ho rhi hai b=6 ho ja rhi hai   

print(f"Result: {result1}")
print(f"Result: {result2}")

