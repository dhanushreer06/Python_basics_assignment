# Q10: Simple ATM Simulator

def run_atm():
    # Initial balance
    balance = 1000.0
    active = True

    print("*** Welcome to the ATM Simulator ***")

    while active:
        print("\n*** Main Menu ***")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            print(f"Current Balance: {balance:.2f}")

        elif choice == '2':
            try:
                deposit = float(input("Enter amount to deposit: "))
                if deposit > 0:
                    balance += deposit
                    print(f"Success! New balance: {balance:.2f}")
                else:
                    print("Error: Amount must be positive.")
            except ValueError:
                print("Error: Please enter a numeric value.")

        elif choice == '3':
            try:
                withdraw = float(input("Enter amount to withdraw: "))
                if withdraw > balance:
                    print("Transaction Failed: Insufficient funds.")
                elif withdraw <= 0:
                    print("Error: Amount must be positive.")
                else:
                    balance -= withdraw
                    print(f"Remaining balance: {balance:.2f}")
            except ValueError:
                print("Error: Please enter a numeric value.")

        elif choice == '4':
            print("Thank you for using our service. Goodbye!")
            active = False
        
        else:
            print("Invalid choice. Please pick a number between 1 and 4.")

run_atm()