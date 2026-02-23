#Q2. Simple Calculator

def calculator():
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print(f"Sum: {num1 + num2}")
    print(f"Difference: {num1 - num2}")
    print(f"Product: {num1 * num2}")
    
    # Divided by Zero handling
    if num2 != 0:
        print(f"{num1 / num2}")
    else:
        print("Cannot divide by zero.")
            

calculator()