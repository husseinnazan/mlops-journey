import db

db.create_table()
print("Hello student ! Select one of the folowing : \n")

while True:
    print("1. Add student\n2. View all students\n3. Class stats\n4. Search for a student\n5. View passing students only\n6. Quit\n")
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
    elif choice == 2:
        for i, student in enumerate(db.get_all_students()):
            print(f"{i + 1}, {student[1]}, {student[2]}", "\n \n \n")
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
            print(f"There he is : {student[1]}, {student[2]}", "\n \n \n")
        else:
            print("Did not find the guy sadly \n")
    elif choice == 5:
        for student in db.get_passing_students():
            print(f"{student[1]}, score: {student[2]}")
    elif choice == 6:
        break
    else:
        print('invalid option')