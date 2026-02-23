#Q1. Personal Biocard

def display_biocard():
    #take input (user details)
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    hobby = input("Enter your favorite hobby: ")

    print("\n*** PERSONAL BIO CARD ***")
    print("___________________________")
    print(f"NAME:  {name}")
    print(f"AGE:   {age}")
    print(f"HOBBY: {hobby}")
    print("___________________________")
display_biocard()