import sqlite3
from typing import List, Optional, Tuple


class Student:
    def __init__(self, id: int, name: str, score: int):
        self.id: int = id
        self.name: str = name
        self.score: int = score


class StudentDB:
    def __init__(self, db_path: str = "students.db"):
        self.db_path: str = db_path
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)
        self.cursor: sqlite3.Cursor = self.conn.cursor()

    def create_table(self) -> None:
        self.cursor.execute('''
            create table if not exists students (
                id integer primary key,
                name text not null,
                score integer not null
            )
        ''')
        self.conn.commit()

    def add_student(self, name: str, score: int) -> None:
        self.cursor.execute(
            '''insert into students (name, score) values (?, ?)''',
            (name, score)
        )
        self.conn.commit()

    def get_all_students(self) -> List[Student]:
        self.cursor.execute('''select * from students''')
        rows = self.cursor.fetchall()
        return [Student(row[0], row[1], row[2]) for row in rows]

    def get_stats(self) -> Tuple[Optional[int], Optional[int], Optional[float]]:
        self.cursor.execute("""select min(score), max(score), avg(score) from students""")
        return self.cursor.fetchone()

    def find_student(self, name: str) -> Optional[Student]:
        self.cursor.execute("""select * from students where name = ?""", (name,))
        row = self.cursor.fetchone()
        if row is None:
            return None
        return Student(row[0], row[1], row[2])

    def get_passing_students(self) -> List[Student]:
        self.cursor.execute('''select * from students where score > 50''')
        rows = self.cursor.fetchall()
        return [Student(row[0], row[1], row[2]) for row in rows]