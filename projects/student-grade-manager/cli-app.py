import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute('''
               create table if not exists students (
               id integer primary key,
               name text not null,
               score integer not null
               ) ''')

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
        cursor.execute('''
    insert into students (name, score)
    values (?, ?)
''', (name, score))
        conn.commit()
        print(f"Great, {name} was just added")

    elif choice == 2:
        cursor.execute('''select * from students''')
        for i, student in enumerate(cursor.fetchall()):
            print(f"{i + 1}, {student[1]}, {student[2]}", "\n \n \n")
    elif choice == 3:
        cursor.execute("""select min(score), max(score), avg(score) from students""")
        lowest, highest, avg = cursor.fetchone()
        if avg is not None:
            print("Highest : ", highest, " ; lowest : ", lowest, " ; average : ", avg, '\n \n \n')
        else:
            print("No students yet :( \n")
            
    elif choice == 4:
        searched_name = input("What is his name ? ")
        cursor.execute("""SELECT * FROM students WHERE name = ?""", (searched_name,))
        student = cursor.fetchone()
        if student is not None:
            print(f" There he is : , {student[1]}, {student[2]}", "\n \n \n")
        else : 
            print("Did not find the guy sadly \n")
    elif choice == 5:
       cursor.execute('''SELECT * FROM students WHERE score > 50''')
       passing_students = cursor.fetchall()
       for student in passing_students : 
        print(f"{student[1]}, score: {student[2]}")
    elif choice == 6:
        break
    else:
        print('invalid option')