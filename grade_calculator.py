#Q6. Grade Calculator

def calculate_grade():
    # Get student info
    name = input("Enter student name: ")
    
    # Get marks for 3 subjects
    sub1 = float(input("Enter marks for Subject 1: "))
    sub2 = float(input("Enter marks for Subject 2: "))
    sub3 = float(input("Enter marks for Subject 3: "))
    
    # Calculate the average
    average = (sub1 + sub2 + sub3) / 3
    
    # Check if marks are realistic
    if any(s < 0 or s > 100 for s in [sub1, sub2, sub3]):
        print("Error: Marks should be between 0 and 100.")
        return

    # Determine grade based on the average
    if average >= 90:
        grade = "A"
        msg = "Excellent."
    elif average >= 80:
        grade = "B"
        msg = "Well done."
    elif average >= 70:
        grade = "C"
        msg = "Good"
    elif average >= 60:
        grade = "D"
        msg = "You passed, but try to improve."
    else:
        grade = "F"
        msg = "Focus on studies."

    # Display result
    print(f"\n*** Grade Card ***")
    print(f"Average Score:{average:.2f}")
    print(f"Final Grade: {grade}")
    print(f"Feedback: {msg}")


marks =calculate_grade()