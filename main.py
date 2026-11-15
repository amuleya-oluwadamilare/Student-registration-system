from student import Student, register_student, view_students, search_student, update_student, delete_student
from storage import save_students, load_students
from results import enter_scores, view_student_result
from reports import class_statistics
from reports import rank_students 

students = load_students()

while True:

    print("\n======================================")
    print("STUDENT RESULT MANAGEMENT SYSTEM")
    print("======================================")

    print("\n1. Register New Student")
    print("2. View All Students")
    print("3. Search for Student")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Enter Student Scores")
    print("7. View Student Results")
    print("8. Class Statistics")
    print("9. Student Ranking")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        register_student(students)
        save_students(students)

    elif choice == "2":
        view_students(students)
    
    elif choice == "3":
        search_student(students)

    elif choice == "4":
        update_student(students)
        save_students(students)

    elif choice == "5":
        delete_student(students)
        save_students(students)

    elif choice == "6":
        enter_scores(students)
        save_students(students)

    elif choice == "7":
        view_student_result(students) 

    elif choice == "8":
        class_statistics(students)   

    elif choice == "9":
        rank_students(students)

    elif choice == "10":
        print("Thank you for using the system!")
        break
    
    else:
        print("This feature is not available yet.")
    print("9. Student Ranking")
    print("10. Exit")
        