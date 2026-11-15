import json
import os
from student import Student

DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "data",
    "students.json"
)


def save_students(students):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    student_data = []

    for student in students:
        student_data.append({
            "student_id": student.student_id,
            "full_name": student.full_name,
            "class_form": student.class_form,
            "gender": student.gender,
            "date_of_birth": student.date_of_birth,
            "scores": student.scores

        })

    with open(DATA_FILE, "w") as file:
        json.dump(student_data, file, indent=4)


def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            student_data = json.load(file)

        return [Student(**data) for data in student_data]

    except (json.JSONDecodeError, TypeError):
        return []