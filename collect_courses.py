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
        courses.append({ "Course Code":course_code, "Exam score(0-70)":exam_score, "Test score(0-30)":test_score, "Credit unit": credit_unit})
        print()
    return courses
#grades = courses
