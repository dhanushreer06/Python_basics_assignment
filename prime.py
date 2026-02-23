#Q15. Simple Prime Number Checker

def check_prime():

    #input a number
    num = int(input("Enter a number: "))
    
    if num < 2:
        print("Not a prime number.")
        return

    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return

    print(f"{num} is a prime number!")

check_prime()