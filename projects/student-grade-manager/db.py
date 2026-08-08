import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        create table if not exists students (
            id integer primary key,
            name text not null,
            score integer mot null
        )
    ''')
    conn.commit()

def add_student(name, score):
    cursor.execute('''insert into students (name, score) values (?, ?)''', (name, score))
    conn.commit()

def get_all_students():
    cursor.execute('''select * from students''')
    return cursor.fetchall()

def get_stats():
    cursor.execute("""select min(score), max(score), avg(score) from students""")
    return cursor.fetchone()

def find_student(name):
    cursor.execute("""select * from students where name = ?""", (name,))
    return cursor.fetchone()

def get_passing_students():
    cursor.execute('''select * from students where score > 50''')
    return cursor.fetchall()