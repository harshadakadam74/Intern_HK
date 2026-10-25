# Student Grade Calculator

## 1. Project Overview

The Student Grade Calculator is a beginner Python project that calculates a student's grade based on their marks. It displays the student's name, marks, grade, and an encouraging message.

The project demonstrates conditional statements, loops, functions, comparison operators, and error handling.

## 2. Objectives

- Understand if, elif, and else statements.
- Practice comparison operators.
- Learn while loops and input validation.
- Create and use functions.
- Handle invalid input using try-except.
- Develop a simple grade calculation application.

## 3. Technologies Used

- Python 3
- Visual Studio Code
- Git and GitHub

No external packages are required.

## 4. Grading Logic

| Marks | Grade |
|---|---|
| 90–100 | A |
| 80–89.99 | B |
| 70–79.99 | C |
| 60–69.99 | D |
| 0–59.99 | F |

The program checks the marks using if-elif-else statements. The first matching condition determines the grade.

## 5. Functions Used

- `get_student_name()`: Accepts a non-empty student name.
- `get_marks()`: Accepts valid marks between 0 and 100.
- `calculate_grade(marks)`: Calculates the grade and returns an encouraging message.
- `display_result()`: Displays the student's result.
- `main()`: Controls the execution of the program.

## 6. Setup Instructions

1. Install Python 3 from https://www.python.org/downloads/.
2. Install Visual Studio Code from https://code.visualstudio.com/.
3. Create a folder named `student-grade-calculator`.
4. Create `grade_calculator.py` and paste the project code.
5. Open the folder in VS Code.
6. Open the integrated terminal.
7. Run `python grade_calculator.py`.
8. Enter the student's name and marks when prompted.

On Windows, `py grade_calculator.py` can also be used.

## 7. Project Structure

- `grade_calculator.py`: Main application.
- `README.md`: Project documentation.
- `test_cases.txt`: Test cases and expected results.
- `screenshots/`: Screenshots showing program execution and testing.

## 8. Testing

The application should be tested with marks from each grade range, boundary values such as 0 and 100, invalid marks outside the permitted range, non-numeric input, and an empty name.

Record the actual outcome of each test before submitting.

## 9. What I Learned

I learned how to use conditional statements to make decisions, comparison operators to compare values, while loops to repeat input requests, functions to organize code, and try-except blocks to handle invalid input.

This project improved my understanding of Python programming logic and input validation.

## 10. Conclusion

The Student Grade Calculator demonstrates how Python can be used to solve a simple real-world problem. It provides a foundation for more advanced topics, including lists of student records, file handling, and object-oriented programming.

