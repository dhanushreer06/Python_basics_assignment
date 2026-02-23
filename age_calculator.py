#Q4. Age Calculator

def calculate_age():
    # lets use current year = 2026
    current_year = 2026
    
    #take input for birth year
    name = input("Enter your name: ")
    birth_year = int(input("Enter your birth year: "))
    
    #find the age
    age = current_year - birth_year
    
    #handling impossible birth year error
    if birth_year > current_year:
        print("Error: Birth year cannot be in the future.")
    else:
        print(f"{name}, you are {age} years old.")
            
calculate_age()