# Q8: Leap Year Checker

def check_leap_year():
    print("Leap Year Checker")
    
    year = int(input("Enter a year: "))
    
    #a year is a leap year if it is divisible by and if it's a century, it should also be divisible by 400
    
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print(f"{year} is a leap year!")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year.")

check_leap_year()