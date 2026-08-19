age = int(input("Enter your age: "))
income = float(input("Enter your annual family income (in rupees): "))

if age >= 25 and income < 300000:
    print("Congratulations! You qualify for the specialized education scholarship.")
else:
    print("Sorry, you do not qualify for the scholarship.")

    if age < 25:
        print("Reason: You must be at least 25 years old.")

    if income >= 300000:
        print("Reason: Annual family income must be below ₹3,00,000.")
