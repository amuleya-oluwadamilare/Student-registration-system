def class_statistics(students):
    print("\n========== CLASS STATISTICS ==========")

    if not students:
        print("No students registered.")
        return

    averages = []

    for student in students:
        if student.scores:
            average = sum(student.scores.values()) / len(student.scores)
            averages.append((student.full_name, average))

    print("Total Registered Students:", len(students))

    if not averages:
        print("No examination results available yet.")
        return

    class_average = sum(avg for name, avg in averages) / len(averages)

    highest = max(averages, key=lambda item: item[1])
    lowest = min(averages, key=lambda item: item[1])

    passed = sum(1 for name, avg in averages if avg >= 40)
    failed = len(averages) - passed

    print("Class Average:", round(class_average, 2))
    print("Highest Average:", highest[0], round(highest[1], 2))
    print("Lowest Average:", lowest[0], round(lowest[1], 2))
    print("Students Passed:", passed)
    print("Students Failed:", failed)

    print("======================================")

def rank_students(students):
    print("\n========== STUDENT RANKING ==========")

    ranked_students = []

    for student in students:
        if student.scores:
            average = sum(student.scores.values()) / len(student.scores)
            ranked_students.append((student, average))

    if not ranked_students:
        print("No student results available.")
        return

    ranked_students.sort(key=lambda item: item[1], reverse=True)

    for position, (student, average) in enumerate(ranked_students, start=1):
        print(f"{position}. {student.full_name} | "
              f"ID: {student.student_id} | "
              f"Average: {average:.2f}")

    print("=====================================")