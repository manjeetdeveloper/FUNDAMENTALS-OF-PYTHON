print("Sale! Sale! Sale!")
print("1. Mobile with Powerbank")
print("2. Only Mobile")
print("3. You are Not Interested")
choice = input("Enter Your Choice: ")

if choice == '1' or choice == '2':
    mobilePrice = float(input("Enter mobile amount: "))

    if choice == '1':
        powerbankPrice = float(input("Enter PowerBank amount: "))
        total = mobilePrice + powerbankPrice
        discount = total * 0.25
        print("You Will Get a 25% Discount. You have to pay: ", total - discount)

        
    elif choice == '2':
        discount = mobilePrice * 0.05
        print("You Will Get a 5% Discount. You have to pay: ", mobilePrice - discount)
else:
    print("I am Not Interested in This Sale!")
