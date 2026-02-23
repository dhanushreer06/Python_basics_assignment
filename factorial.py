#Q14. Factorial Calculator

def factorial(n):
    #base Case
    if n == 0 or n == 1:
        return 1
    #recursive Case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a non-negative integer: "))

result = factorial(num)
print(f"The factorial of {num} is: {result}")
            
