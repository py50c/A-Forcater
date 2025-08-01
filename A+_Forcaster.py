def collect_courses():
    courses = []
    no_of_courses = int(input("How many courses do you offer?: "))
    print()
    num = 0
    for num in range (no_of_courses):
        print(f"Course {num + 1}: ")
        course_code = input(" Enter Course Code: ")
        exam_score = float(input(" Enter Exam Score(0-70): "))
        test_score = float(input(" Enter Test score(0-30): "))
        credit_unit = int(input(" What's the credit unit for the course? "))
        courses.append({ "Course code":course_code,  "Exam score":exam_score,  "Test score":test_score,  "Credit unit": credit_unit})
        print()
    return courses

def feedback(grades):
    """this function analyzes each course's score and grade point, and provides 
    feedback, congratulates for good scores and suggests improvement for low scores,
    and motivates the student to keep trying."""
    feedback_msg = []
    course_feedback = []
    for course in grades:
        total_score = course['Test score'] + course['Exam score']
        Test_score = course['Test score']
        Exam_score = course['Exam score']
        Course_code = course['Course code']
        if total_score >= 70:
            course_feedback.append(f"Congratulations! You absolutely crushed {Course_code} with an A.")
            print(' ')
            course_feedback.append("You're basically a genius, scientists should study your big, beautiful brain")
        elif total_score >= 60:
            course_feedback.append(f"Whoa, you had a B in {Course_code}. You were so close to an A,")
            course_feedback.append('you could almost taste it ')
            if Test_score == 15 and Exam_score == 45:
                course_feedback.append(f'Be careful though, you almost missed it with a test score of {Test_score}.')
                course_feedback.append(f"and an exam score of {Exam_score}. Let's make them both sparkle next time")
            elif 5 <= Test_score <= 15 and Exam_score == 55:
                course_feedback.append(f"you flopped your test a bit with a test score of {Test_score}. Let's focus more next time")
                course_feedback.append(f"your exam score of {Exam_score} basically did all the magic")
            elif Test_score <= 4 and Exam_score >= 60:
                course_feedback.append(f"You seem to have had a little issue with a test score of {Test_score} and an exam score of {Exam_score}")
                print(" ")
                course_feedback.append("Let's make sure to prepare better next time")
                course_feedback.append("or rather still pray for this miracle to reoccur") 
            elif 30 <= Exam_score <= 35 and 25 >= Test_score <= 30:
                course_feedback.append(f"Not gonna lie, you flopped your exam real bad with an exam score of {Exam_score}")
                course_feedback.append(f"Your test score of {Test_score} did a good job")
                print(" ")
                course_feedback.append("Let's put more effort next time, okay?")
        elif total_score >= 50:
            course_feedback.append(f"Whoa, you snagged a C in {Course_code}! Not every superhero wears a cape,")
            course_feedback.append('but you certainly conquered this course, trust me')
            if Test_score == 15 and Exam_score == 35:
                course_feedback.append(f'Both your test score of {Test_score} and exam score of {Exam_score}')
                course_feedback.append("were taking it easy.")
                print(" ")
                course_feedback.append("Let's power them up in the next round")
            elif 6<= Test_score <= 15 and Exam_score == 44:
                course_feedback.append(f"you flopped your test real bad with a test score of {Test_score}. Let's focus more next time")
                course_feedback.append(f"your exam score of {Exam_score} basically did all the magic")
                print(" ")
                course_feedback.append("Although you didn't do well in your exams either, a little more effort can do the magic")
                course_feedback.append("You can always still make it to the top. Keep pushing")
            elif Test_score <= 6 and Exam_score >= 50:
                course_feedback.append(f"With a test score of {Test_score} and an exam score of {Exam_score}, I'm guessing you could do better, and work on your tests too")
                print(" ")
                course_feedback.append("Let's make sure to prepare better next time") 
            elif 20 <=Exam_score <= 29 and 25 >= Test_score <= 30:
                course_feedback.append("Not gonna lie, you flopped your exam real bad. Let's put more effort next time, okay?")
                course_feedback.append("Consistency remains the key")
        elif total_score >= 45:
            course_feedback.append(f"Well, almost bagged a C in {Course_code}! Seems like you barely made it under,")
            course_feedback.append(f"with a test and exam score of {Test_score} and, {Exam_score}")
            print(' ')
            course_feedback.append("Don't give up, a D grade means you're close.")
            course_feedback.append("Focus on your weaknesses and bounce back stronger")
            if Test_score == 15 and Exam_score == 30:
                course_feedback.append(f'Both your test score of {Test_score} and exam score of {Exam_score}')
                course_feedback.append("were on a coffee break. It's time to get them back in action  ")
            elif Test_score == range(6,15) and Exam_score == 39:
                course_feedback.append(f"So, your test score of {Test_score} was taking a leisurely stroll, and ")
                course_feedback.append(f"your exam score of {Exam_score} was sprinting")
                course_feedback.append("maybe give your tests a little sprint training")
                course_feedback.append("Every setback is always an oppurtunity for growth")
                course_feedback.append("You can always still make it to the top")
            elif Test_score <= 6 and Exam_score >= 45:
                course_feedback.append(f"You were definitely off track with a test score of {Test_score} and your exam score of {Exam_score} literally bailed you.")
                course_feedback.append("You can do better")
                print(' ')
                course_feedback.append("Let's make sure to prepare better next time") 
            elif Exam_score == range(15,19) and 25 >= Test_score <= 30:
                course_feedback.append(f"Your exam had its own plans with an exam score of {Exam_score} while your test was on fire with a test score of {Test_score}.")
                course_feedback.append("Let's get both of them on the same page next time")
        elif total_score >=40:
            course_feedback.append(f"So, you had an E in {Course_code}.Well gotta say, atleast it's not an F.")
            course_feedback.append("You're doing better than you think! An E grade shows you're meeting expectations")
            course_feedback.append("Keep building on your strengths")
            course_feedback.append("Consider this a learning curve with a slight incline")
            if Test_score == 15 and Exam_score == 25:
                course_feedback.append(f'Both your test score of {Test_score} and exam score of {Exam_score}')
                course_feedback.append("seem to have a bit of a stage fright syndrome.") 
                course_feedback.append("Let's make them superstars")
            elif Test_score == range(6,15) and Exam_score == 39:
                course_feedback.append(f"So, your test score of {Test_score} was likely taking the day off, compared to")
                course_feedback.append(f"your exam score of {Exam_score}")
                course_feedback.append("Or maybe they were speaking a ddifferent language")
                course_feedback.append("Remember, it's progress over perfection")
                course_feedback.append("Keep movinng forward and you'll achieve your goals")
            elif Test_score <= 6 and Exam_score >= 39:
                course_feedback.append(f"Your test score of {Test_score} was definitely off track and your exam score of {Exam_score} was no better. You can do better")
                print(" ")
                course_feedback.append("Let's make sure to prepare better and aim higher") 
            elif Exam_score == range(10,14) and 25 >= Test_score <= 30:
                course_feedback.append(f"With an exam score of {Exam_score}, I'm guessing you were on vacation during your exams cause honestly your test score of {Test_score} did all the magic here.")
                print(' ')
                course_feedback.append("Let's get both of them on the same page next time. Okay?")
        else:
            course_feedback.append(f"Unfortunately you have an F in {Course_code}. Don't fret, think of this as a practice round")
            course_feedback.append("It's okay to stumble")
            course_feedback.append("Let's reaccess and come back stronger")
            if Test_score == 15 and Exam_score == 24:
                course_feedback.append(f'Both your test score of {Test_score} and exam score of {Exam_score}')
                course_feedback.append("seem to have played a little hide-and-seek.") 
                print(' ')
                course_feedback.append("Let's make sure to find them next time")
            elif Test_score == range(6,15) and Exam_score == 33:
                course_feedback.append(f"So, with your test score of {Test_score} and exam score of {Exam_score},")
                course_feedback.append("I think we need to have a serious prep talk")
                print(' ')
                course_feedback.append("Let's push much more harder. You're almost there")
            elif Test_score <= 6 and Exam_score == 39:
                course_feedback.append(f"Your test score of {Test_score} is practically invisible. You can do better")
                print(' ')
                course_feedback.append("Let's aim higher. More grace to your elbow") 
            elif Exam_score == range(0,9) and Test_score >=25 or Test_score <= 30:
                course_feedback.append(f"Your exam score of {Exam_score} basically ghosted you while your test score of {Test_score} tried its best")
                print(' ')
                course_feedback.append("Time to get both parts of your brain in the game. Na you promise your mama first class. Orhh")

        feedback_msg.append("".join(course_feedback))
    return feedback_msg

def main():
    name = input("What is your name?: ") 
    print(f"Hello {name}.Welcome to A+ VIBES! 😀 ")
    print("Where you can confidently forecast your CGPA eventually making you an excellent student!🤩")
    print()
    grades = collect_courses()
    
    prev_cgpa = input("Enter previous CGPA, if not leave blank!: ") #Takes in input for previous CGPA 
    prev_credits = input("Enter previous credit unit, if not leave blank!: ") #Takes in input for previous credit units
    #sprint(f"{name}, your current CGPA is {calculate_cgpa(grades, prev_cgpa=None, prev_credits=None)}") #calls the function that would provide the CGPA
    print(f"Our honest review and suggestions are as follows: {feedback(grades)}") #Calls the function that would give feedback 
    
if __name__ == "__main__":
    main()  #calls the function that orchestrate the flow of the entire program 