year = int(input("Enter year: \n"))

if (year % 4 == 0 and year % 100 != 0): 

    # yaha ham 100 se divide esliye kiye hai ki centurey ko check krne ke liye 

    # koi v year jo 4 se divisible ho wo leap year hota hai 
    # ur jo 100 se divisible ho wo nahi hota hai 
    
    print(f"{year} is a leap year.")


else:
    print(f"{year} is not a leap year.")
