# Student Grade Manager (CLI)

A command-line tool to manage student records — add students, view stats, search, and filter — backed by a real SQLite database, with a typed, object-oriented data layer.

This was my first full project (P1) in my self-study roadmap. It's evolved through several distinct versions rather than being written once — see [Version History](#version-history) below for how it actually got here.

## Project structure

- `db.py` — the data layer. A `StudentDB` class owns the database connection, cursor, and every SQL query as methods. A `Student` class represents a row as an object (`.id`, `.name`, `.score`) instead of a raw tuple. Returns data, never prints anything.
- `main.py` — the application layer. Owns the menu, `input()`, every `print()`, and the file-based features (export + logging). Creates one `StudentDB` instance and calls its methods, never writes SQL directly.

## Features

- Add a student (name + score)
- View all students
- Class stats (min / max / average score)
- Search for a student by name
- View only passing students (score > 50)
- Data persists between runs — closing the app doesn't lose anything
- **Export all students to a text file** (`backup.txt`) — added while learning file I/O
- **Activity logging** — every add/search action is appended to `activity_log.txt`, added while learning `try/except` and `*args`/`**kwargs`

## Tech stack

- Python 3
- SQLite (via Python's built-in `sqlite3` module)
- Type hints (`typing` module: `List`, `Optional`, `Tuple`) throughout `db.py` and `main.py`
- OOP data layer (`StudentDB`, `Student`) with inheritance concepts applied elsewhere in the roadmap, composition/inheritance not needed in this particular project

## How to run

```bash
python main.py
```

The database file (`students.db`) is created automatically the first time you run it — no setup needed.

## Database schema

```sql
create table students (
    id    integer primary key,
    name  text not null,
    score integer not null
);
```

## Version History

**v0.1 — In-memory prototype**
Pure Python, no persistence — data lived in lists/dicts and vanished on exit. First working version of the menu loop and core operations (add, view, stats, search, filter).

**v0.2 — SQLite persistence**
Rebuilt on a real `students.db` file via Python's `sqlite3` module. All five menu options moved from in-memory logic to real SQL queries (`INSERT`, `SELECT`, aggregate functions, `WHERE` filtering). Data now survives between runs.

**v0.3 — Layered architecture**
Split the single file into `db.py` (data layer — owns the connection, cursor, and all SQL; returns data, never prints) and `main.py` (application layer — owns the menu, `input()`, `print()`). Resolved a real git merge conflict along the way, from two divergent histories of the same file.

**v0.4 — File I/O and error handling**
Added `export_students_to_file()` (writes all students to `backup.txt`) and `log_action()` (appends every add/search to `activity_log.txt` using `*args`/`**kwargs` for flexible action details). Introduced `try/except OSError` around file operations instead of letting the program crash on a bad write/read.

**v0.5 — OOP + type hints refactor (current)**
`db.py`'s free functions rebuilt as a `StudentDB` class — connection and cursor become `self.conn`/`self.cursor`, created once in `__init__` instead of living as module-level globals threaded through every function call. A new `Student` class replaces raw tuple access (`student[1]`, `student[2]`) with named attributes (`student.name`, `student.score`) everywhere in `main.py`. Every method and function across both files fully type-hinted:
- `get_all_students()` / `get_passing_students()` → `List[Student]`
- `find_student()` → `Optional[Student]` — the real-world case for `Optional`: genuinely returns `None` when no match is found, not just a formality
- `get_stats()` → `Tuple[Optional[int], Optional[int], Optional[float]]` — the row itself is always returned by `fetchone()` on an aggregate query, but individual values inside it can be `None` on an empty table

## What I learned building this

- Difference between in-memory data (lists/dicts) and persistent storage
- Parameterized queries (`?` placeholders) to avoid SQL injection
- `fetchone()` vs `fetchall()`, and when each applies
- Using SQL aggregate functions (`MIN`, `MAX`, `AVG`) instead of computing stats manually in Python
- `NULL` in SQL becomes `None` in Python, and why that matters for edge cases like stats on an empty table
- Separating data logic from application logic — `db.py` returns data, `main.py` decides how to display it
- Resolving a real git merge conflict — two divergent histories of the same file, reconciled by hand
- Reading and writing files safely with `with open(...)`, and why it's preferred over manual `open()`/`close()`
- Handling file errors with `try/except OSError` instead of letting the program crash
- Using `*args` and `**kwargs` to build a flexible logging function that accepts any action's details
- Wrapping a database connection in a class (`StudentDB`) so `conn`/`cursor` live in one place instead of being re-passed to every function — the same shape real ORM/framework code (SQLAlchemy, FastAPI dependency injection) uses later
- Replacing raw tuple indexing with a proper object (`Student`) — `student.name` instead of `student[1]`, and why that matters for readability once a schema has more than two or three columns
- Applying `Optional` to a function that has a genuine "might return nothing" case (`find_student`), rather than as an abstract exercise