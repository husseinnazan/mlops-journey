from typing import Dict
from db import StudentDB

db = StudentDB()


def export_students_to_file(filename: str = "backup.txt") -> None:
    students = db.get_all_students()

    student_dict: Dict[str, int] = {}
    for student in students:
        student_dict[student.name] = student.score

    try:
        with open(filename, 'w') as w:
            for name, score in student_dict.items():
                w.write(f"{name}: {score}\n")
    except OSError as e:
        print(f"Error was: {e}")


def log_action(action: str, *details, **meta) -> None:
    try:
        with open("activity_log.txt", 'a') as wr:
            wr.write(f"ACTION: {action} | details: {details} | meta: {meta}\n")
    except OSError as e:
        print(f"you have the following error : {e}")


db.create_table()
print("Hello student ! Select one of the folowing : \n")

while True:
    print("1. Add student\n2. View all students\n3. Class stats\n4. Search for a student\n5. View passing students only\n6. Export to file\n7. Quit\n")
    try:
        choice = int(input("Choose an option : "))
    except ValueError:
        print("Not a valid input")
        continue

    if choice == 1:
        name = input("Please enter the student's name : ")
        score = int(input("Please enter the student's score : "))
        db.add_student(name, score)
        print(f"Great, {name} was just added")
        log_action("add_student", name, score, source="menu")

    elif choice == 2:
        for i, student in enumerate(db.get_all_students()):
            print(f"{i + 1}, {student.name}, {student.score}", "\n \n \n")

    elif choice == 3:
        lowest, highest, avg = db.get_stats()
        if avg is not None:
            print("Highest : ", highest, " ; lowest : ", lowest, " ; average : ", avg, '\n \n \n')
        else:
            print("No students yet :( \n")

    elif choice == 4:
        searched_name = input("What is his name ? ")
        student = db.find_student(searched_name)
        if student is not None:
            print(f"There he is : {student.name}, {student.score}", "\n \n \n")
        else:
            print("Did not find the guy sadly \n")
        log_action("search", searched_name)

    elif choice == 5:
        for student in db.get_passing_students():
            print(f"{student.name}, score: {student.score}")

    elif choice == 6:
        export_students_to_file()
        print("Exported to backup.txt")

    elif choice == 7:
        break

    else:
        print('invalid option')