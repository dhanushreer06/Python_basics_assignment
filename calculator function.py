#Q18. Basic Calculator Project

def calculator():

    while True:
        # Show the options
        print("\n Available Operations ")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        # Get user choice
        choice = input("\nChoose an option (1-5): ")

        if choice == '5':
            break

        if choice in ['1', '2', '3', '4']:
            #input values
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the operation based on choice made
            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                #division by zero error
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: You cannot divide by zero!")

# Run the function
calculator()