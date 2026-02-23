# Q5: Bill Splitter

def split_the_bill():
    
    print("**Bill Splitter***")

    # Get the inputs
    total_bill = float(input("Enter the total bill amount: "))
    tip_percentage = float(input("Enter tip percentage "))
    people_count = int(input("How many people are splitting the bill? "))

    # Calculating tip_amnt, final_total, amnt_per_person  
    tip_amnt = total_bill * (tip_percentage / 100)
    final_total = total_bill + tip_amnt
    amnt_per_person = final_total / people_count

    # Display results
    print(f"Total Bill (with tip): {final_total:.2f}")
    print(f"Each person should pay: {amnt_per_person:.2f}")

bill = split_the_bill()