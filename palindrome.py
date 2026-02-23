#Q17. Palindrome Checker

def check_palindrome():
    
    #input a string
    s = input("Enter a word or number: ")
    
    reversed_string = ""
    
    #reverse the string
    for ch in s:
        reversed_string = ch + reversed_string
    
    if s == reversed_string:
        print(s, "is a palindrome.")
    else:
        print(s, "is not a palindrome.")

check_palindrome()