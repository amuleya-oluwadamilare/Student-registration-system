from datetime import datetime
def enter_scores(students):
    print("\n--- ENTER STUDENT SCORES ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student.student_id == student_id:

            subjects = ["Mathematics", "English", "Computer Science",
                        "Physics", "Chemistry"]

            student.scores = {}

            for subject in subjects:
                while True:
                    try:
                        score = float(input(f"Enter {subject} score: "))

                        if 0 <= score <= 100:
                            student.scores[subject] = score
                            break
                        else:
                            print("Score must be between 0 and 100.")

                    except ValueError:
                        print("Please enter a valid number.")

            print("\nScores entered successfully!")
            return

    print("Student not found!")


def calculate_result(student):
    if not student.scores:
        print("No scores available for this student.")
        return

    total = sum(student.scores.values())
    average = total / len(student.scores)

    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 45:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade = "F"

    print("\n========== STUDENT RESULT ==========")
    print("Name:", student.full_name)
    print("Student ID:", student.student_id)
    print("Report Date:", datetime.now().strftime("%d-%m-%Y %H:%M"))

    for subject, score in student.scores.items():
        print(f"{subject}: {score}")

    print("-----------------------------------")
    print("Total Score:", total)
    print("Average Score:", round(average, 2))
    print("Grade:", grade)
    print("===================================")


def view_student_result(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student.student_id == student_id:
            calculate_result(student)
            return

    print("Student not found!")