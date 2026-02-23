#Q19. Text Analysis

def text_analysis():
    
    #input a text
    text = input("Enter a sentence: ")
    
    #total chars (including spaces)
    total_chars = len(text)
    
    #total words
    words = text.split()
    total_words = len(words)
    
    #count vowels
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for ch in text:
        if ch in vowels:
            vowel_count += 1
    
    #display result
    print("\nText Analysis Result:")
    print("Total Characters:", total_chars)
    print("Total Words:", total_words)
    print("Total Vowels:", vowel_count)

text_analysis()