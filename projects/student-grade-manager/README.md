# Student Grade Manager (CLI)

A command-line tool to manage student records — add students, view stats, search, and filter — backed by a real SQLite database.

This was my first full project (P1) in my self-study roadmap. It went through three stages: a pure Python CLI storing data in memory, then rebuilt with SQLite for persistence, then refactored into a proper data layer / application layer split. It was later extended with file I/O and error handling — exporting records to a file and logging user actions.

## Project structure

- `db.py` — the data layer. Owns the database connection and every SQL query. Returns data, never prints anything.
- `main.py` — the application layer. Owns the menu, `input()`, every `print()`, and the file-based features (export + logging). Calls into `db.py`, never writes SQL directly.

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