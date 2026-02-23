#Q13. Sum and Average Calculator

def calculate_stats():
    print("*** Sum and Average Calculator ***")
    
    #inputs
    n = int(input("How many numbers do you want to enter? "))
    
    if n <= 0:
        print("Error: You must enter at least one number.")
        return
        
    numbers = [] #empty list
    
    #loop to take each number
    for i in range(1, n + 1):
        val = float(input(f"Enter number {i}: "))
        numbers.append(val)
        
    #calculate sum and average
    total_sum = sum(numbers)
    average = total_sum / n
    
    print("\nResults")
    print(f"Numbers entered: {numbers}")
    print(f"Total Sum: {total_sum}")
    print(f"Average: {average:.2f}")
        
calculate_stats()