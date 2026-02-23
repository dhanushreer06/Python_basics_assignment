#Q11. Number Pattern Printer

def print_pattern():
    print("*** Number Pattern Printer ***")
    
    #input rows
    rows = int(input("Enter the number of rows: "))
    
    if rows <= 0:
        print("Please enter a positive number.")
        return
    
    #outer loop
    for i in range(1, rows + 1):
        #inner loop to print numbers in the row
        for j in range(1, i + 1):
            print(j, end=" ")
        
        #move to next line
        print()
            
print_pattern()