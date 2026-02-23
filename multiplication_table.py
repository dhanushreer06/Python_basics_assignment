#Q12. Multiplication Table Generator

def generate_table():
    
    #get the number for the table
    num = int(input("Enter the number: "))
    #ask how far the table should go 
    n = int(input("Enter the range: "))

    print(f"\n Multiplication Table for {num} ")
    
    #loop from 1 up to the limit
    for i in range(1, n + 1):
        result = num * i
        print(f"{num} x {i} = {result}")

generate_table()