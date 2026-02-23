#Q9. Ticket Pricing System

def get_ticket_price():
    print(" *** Ticket Booking *** ")
    
    #standard price for a ticket
    base_price = 10.0
    
    age = int(input("Enter your age: "))
    
    if age < 0:
        print("Age cannot be negative!")
        return

    # Pricing logic
    if age < 5:
        #free for toddlers
        price = 0.0
        print("Ticket is free for children under 5.")
    elif age <= 12:
        #child discount
        price = base_price * 0.5
        print(f"Child ticket (5-12): 50% discount applied.")
    elif age >= 60:
        #senior discount
        price = base_price * 0.7
        print(f"Senior ticket (60+): 30% discount applied.")
    else:
        #standard price
        price = base_price
        print("Standard adult ticket price applies.")

    print(f"\nFinal Ticket Price: {price:.2f}")

get_ticket_price()