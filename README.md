# A+ Vibes CGPA Calculator

## Overview

A+ Vibes is a Python-based CGPA calculator designed to help students track their academic progress, receive personalized feedback on each course, and motivate them to improve. The program collects course scores, calculates CGPA (including previous semester data), and provides actionable feedback for every course.

---

## Features

- **Course Data Collection:**  
  Collects course codes, test scores, exam scores, and credit units from the user.

- **CGPA Calculation:**  
  Calculates the current CGPA, optionally including previous semester CGPA and credits.

- **Personalized Feedback:**  
  Provides feedback for each course, indicating whether the student passed, areas for improvement, and motivational messages.

---

## How It Works

1. **User enters their name and semester.**
2. **User inputs course details for the current semester.**
3. **If in the second semester, user provides previous semester CGPA and credits.**
4. **The program calculates the CGPA and displays it.**
5. **Feedback is given for each course, including suggestions and encouragement.**

---

## Function Breakdown

### `collect_courses()`
- Prompts the user for the number of courses.
- For each course, collects:
  - Course code
  - Test score
  - Exam score
  - Credit unit
- Returns a list of dictionaries, each representing a course.

### `calculate_cgpa(grades, prev_cgpa=None, prev_credits=None)`
- Calculates grade points for each course based on total score.
- Computes total weighted grade points and credits.
- If previous CGPA and credits are provided, includes them in the calculation.
- Returns the CGPA rounded to 2 decimal places.

### `feedback(grades)`
- Analyzes each course’s score and grade point.
- Provides feedback for each course:
  - Congratulates for high scores.
  - Suggests improvement for lower scores.
  - Motivates the student to keep trying.

### `main()`
- Orchestrates the flow:
  - Collects user info.
  - Calls `collect_courses()`.
  - Calls `calculate_cgpa()`.
  - Calls `feedback()` and displays results.

---

## Team Collaboration Guide

### Suggested Team Structure

- **Team 1:** Course Data Collection (`collect_courses`)
- **Team 2:** CGPA Calculation (`calculate_cgpa`)
- **Team 3:** Feedback System (`feedback`)

### Universal Variable Names

- `grades`: List of course dictionaries (used throughout).
- `course`: Individual course dictionary (used in loops).
- `prev_cgpa`: Previous semester CGPA (float).
- `prev_credits`: Previous semester total credits (int).
- `total_score`: Sum of test and exam scores (float, per course).
- `grade_point`: Calculated grade point (float, per course).

### Integration Points

- **Data Format:**  
  All functions use the same `grades` list structure.
- **Interface Contracts:**  
  Each function expects and returns data in a documented format.
- **Testing:**  
  Teams should test their functions independently and together.

---

## Example Usage

```bash
$ python A+_vibes.py
Please Enter your Name: Joe
Hey, Joe welcome to A+ Forcaster
Enter number of courses: 3

Course 1:
  Course code: MTH101
  Test score (0-30): 20
  Exam score (0-70): 60
  Credit unit: 3

Course 2:
  Course code: PHY101
  Test score (0-30): 15
  Exam score (0-70): 50
  Credit unit: 2

Course 3:
  Course code: ENG101
  Test score (0-30): 10
  Exam score (0-70): 30
  Credit unit: 1

Enter previous CGPA (or leave blank): 4.2
Enter previous total credits (or leave blank): 18
Okay, Joe, Your Current CGPA: 4.11
Here is what we have to say: 
Congratulations! You got an A (5.0) in MTH101 - keep the A+ Vibes up!
Well done! You got a B (4.0) in PHY101 - you could still have gotten an A, you had 15 test score, that's why!
You got an E (1.0) in ENG101 - you have to go and read, don't give up!
```

---

## Best Practices

- **Use consistent variable names.**
- **Document all functions and expected data formats.**
- **Test each function independently and as part of the whole program.**
- **Collaborate using version control (e.g., Git).**
- **Review and integrate code as a team.**

---


## Authors

A+ Vibes Team
