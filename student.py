class Student:
        
    def __init__(self, student_id, full_name, class_form, gender, date_of_birth, scores=None):
        self.student_id = student_id
        self.full_name = full_name
        self.class_form = class_form
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.scores = scores if scores is not None else {}

    def display_info(self):
        print("\nStudent Information")
        print("---------------------------")
        print("Student ID:", self.student_id)
        print("Full Name:", self.full_name)
        print("Class:", self.class_form)
        print("Gender:", self.gender)
        print("Date of Birth:", self.date_of_birth)

def register_student(students):
 
    print("\n--- REGISTER NEW STUDENT ---")

    while True:
        student_id = input("Enter Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            continue

        break

    while True:
        full_name = input("Enter Full Name: ").strip()

        if not full_name:
            print("Student name cannot be empty.")
        else:
            break
        class_form = input("Enter Class/Form: ")
        gender = input("Enter Gender: ")
        date_of_birth = input("Enter Date of Birth: ")

        new_student = Student(
            student_id,
            full_name,
            class_form,
            gender,
            date_of_birth
        )

        students.append(new_student)

        print("\nStudent registered successfully!")

def view_students(students):
      print("\n--- REGISTERED STUDENTS ---")
      
      if not students:
            print("No students registered yet.")
            return
      
      for student in students:
            student.display_info()

def search_student(students):

    print("\n--- SEARCH FOR STUDENT ---")

    search_id = input("Enter Student ID or Name: ")

    for student in students:

        if (student.student_id.lower() == search_id.lower()
                or search_id.lower() in student.full_name.lower()):

            student.display_info()
            return

    print("Student not found!")

def update_student(students):

    print("\n--- UPDATE STUDENT INFORMATION ---")

    student_id = input("Enter Student ID: ")

    for student in students:

        if student.student_id == student_id:

            print("\nEnter new information.")

            student.full_name = input("New Full Name: ")
            student.class_form = input("New Class: ")
            student.gender = input("New Gender: ")
            student.date_of_birth = input("New Date of Birth: ")

            print("\nStudent information updated successfully!")
            return

    print("Student not found!")

def delete_student(students):

    print("\n--- DELETE STUDENT ---")

    student_id = input("Enter Student ID to delete: ")

    for student in students:

        if student.student_id == student_id:

            students.remove(student)

            print("\nStudent deleted successfully!")
            return

    print("Student not found!")
