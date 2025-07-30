def collect_courses():
    courses = []
    no_of_courses = int(input("How many courses do you offer?: "))
    print()
    num = 0
    for num in range (no_of_courses):
        print(f"Course {num + 1}: ")
        course_code = input(" Enter Course Code: ")
        exam_score = float(input(" Enter Exam Score(0-70): "))
        credit_unit = int(input(" What's the credit unit for the course? "))
        test_score = float(input(" Enter Test score(0-30): "))
        courses.append({ "Course Code":course_code,  "Exam score":exam_score,  "Test score":test_score,  "Credit unit": credit_unit})
        print()
    return courses


def main():
    name = input("What is your name?: ") 
    print(f"Hello {name}.Welcome to A+ VIBES! 😀 ")
    print("Where you can confidently forecast your CGPA eventually making you an excellent student!🤩")
    print()
    collect_courses()
    grades = collect_courses()
    
    prev_cgpa = float(input("Enter previous CGPA, if not leave blank!: ")) #Takes in input for previous CGPA 
    prev_credits = int(input("Enter previous credit unit, if not leave blank!: ")) #Takes in input for previous credit units
    print(f"{name}, your current CGPA is {calculate_cgpa(grades, prev_cgpa=None, prev_credits=None)}") #calls the function that would provide the CGPA
    print(f"Our honest review and suggestions are as follows: {feedback(grades)}") #Calls the function that would give feedback 
    
if __name__ == "__main__":
    main()  #calls the function that orchestrate the flow of the entire program 