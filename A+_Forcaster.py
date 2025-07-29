def main():
    name = input("What is your name?: ") 
    print(f"Hello {name}.Welcome to A+ VIBES! 😀 ")
    print("Where you can confidently forecast your CGPA eventually making you an excellent student!🤩")
    print()
    collect_courses()
    
    prev_cgpa = float(input("Enter previous CGPA, if not leave blank!: ")) #Takes in input for previous CGPA 
    prev_credits = int(input("Enter previous credit unit, if not leave blank!: ")) #Takes in input for previous credit units
    print(f"{name}, your current CGPA is {calculate_cgpa(grades, prev_cgpa=None, prev_credits=None)}") #calls the function that would provide the CGPA
    print(f"Our honest review and suggestions are as follows: {feedback(grades)}") #Calls the function that would give feedback 
    
if __name__ == "__main__":
    main()  #calls the function that orchestrate the flow of the entire program 