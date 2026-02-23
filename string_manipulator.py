#Q3. String Manipulator

def manipulate_string():
    #taking input
    s = input("Enter a string: ")

    
    #converting string to uppercase and lowercase
    print(f"Uppercase: {s.upper()}")
    print(f"Lowercase: {s.lower()}")
    
    #reversing the string by using slicing
    reversed_string = s[::-1]
    print(f"Reversed string:  {reversed_string}")
    
    #finding length
    print(f"Length of string is :    {len(s)}")

s = manipulate_string()