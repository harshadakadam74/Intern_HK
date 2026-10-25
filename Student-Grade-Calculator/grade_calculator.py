
# Project: Student Grade Calculator
# Week 2 - Python Basics
# Description: Calculate a student's grade from their marks.


def get_student_name():
    """Ask for a non-empty student name."""
    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name

        print("Name cannot be empty. Please try again.")


def get_marks():
    """Accept marks between 0 and 100."""
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Invalid marks! Enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def calculate_grade(marks):
    """Return the grade and encouraging message."""
    if marks >= 90:
        return "A", "Excellent! Outstanding work!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good job! Keep improving!"
    elif marks >= 60:
        return "D", "You passed! Keep practicing!"
    else:
        return "F", "Don't give up! Learn and try again!"


def display_result(name, marks, grade, message):
    """Display the student's result."""
    print("\n" + "=" * 40)
    print(f"RESULT FOR {name.upper()}")
    print("=" * 40)
    print(f"Student Name: {name}")
    print(f"Marks: {marks:g}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")
    print("=" * 40)


def main():
    print("=" * 40)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 40)

    name = get_student_name()
    marks = get_marks()

    grade, message = calculate_grade(marks)

    display_result(name, marks, grade, message)


if __name__ == "__main__":
    main()
