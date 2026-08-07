# Student Grade Manager (CLI)

A command-line tool to manage student records — add students, view stats, search, and filter — backed by a real SQLite database.

This was my first full project (P1) in my self-study roadmap. It started as a pure Python CLI storing data in memory, then was rebuilt to persist data with SQLite as part of learning databases and SQL.

## Features

- Add a student (name + score)
- View all students
- Class stats (min / max / average score)
- Search for a student by name
- View only passing students (score > 50)
- Data persists between runs — closing the app doesn't lose anything

## Tech stack

- Python 3
- SQLite (via Python's built-in `sqlite3` module)

## How to run

```bash
python cli-app.py
```

The database file (`students.db`) is created automatically the first time you run it — no setup needed.

## Database schema

```sql
CREATE TABLE students (
    id    INTEGER PRIMARY KEY,
    name  TEXT NOT NULL,
    score INTEGER NOT NULL
);
```

## What I learned building this

- Difference between in-memory data (lists/dicts) and persistent storage
- Parameterized queries (`?` placeholders) to avoid SQL injection
- `fetchone()` vs `fetchall()`, and when each applies
- Using SQL aggregate functions (`MIN`, `MAX`, `AVG`) instead of computing stats manually in Python
- `NULL` in SQL becomes `None` in Python, and why that matters for edge cases like stats on an empty table
