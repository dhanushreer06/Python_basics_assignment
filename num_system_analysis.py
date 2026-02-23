#Q20. Number System Analysis

def number_system():
    
    #input a number
    num = int(input("Enter a decimal number: "))
    
    #convering numbers in to diff format
    print("Binary:", format(num, 'b'))
    print("Octal:", format(num, 'o'))
    print("Hexadecimal:", format(num, 'x'))

number_system()