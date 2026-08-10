# mlops-journey
Learning log and projects on my path to MLOps engineering.

# MLOps Journey

Learning log for my path to MLOps engineering.

**Goal:** Backend/cloud engineer first, MLOps engineer after.

**Started:** August 2026

## Phase 1 — Backend foundations

- [x] Python fundamentals — syntax, functions (`notebooks/python/`)
- [x] SQL & relational databases (`notebooks/sql/`)
- [x] Git & GitHub (`notebooks/git/`)
- [x] Bash (`notebooks/bash/`)
- [x] Python Part 2 — dicts/tuples/sets, file I/O, try/except, *args/**kwargs (`notebooks/python/`)
- [ ] SQL window functions
- [ ] OOP
- [ ] Type hints
- [ ] Foundational DSA
- [ ] Error handling (custom exceptions)
- [ ] Context managers
- [ ] Decorators
- [ ] JSON
- [ ] HTTP requests
- [ ] Unit testing
- [ ] StudyMind — FastAPI + SQLite + LLM API (capstone)

## Projects

- [Student Grade Manager (CLI)](projects/student-grade-manager) — CLI app with SQLite persistence. First project (P1), originally in-memory, rebuilt with a real database. Extended with file export and activity logging while learning file I/O and error handling.
- [Bash Todo App (CLI)](projects/bash-todo-app) — `add` / `list` / `remove` todo list in pure Bash, backed by SQLite at `~/.config/todo-app/db.sqlite`. Built to learn `case` branching and calling `sqlite3` from a shell script.

## Log
- **2026-08-06** — Set up environment (Git, VS Code, Python). Started SQL.
- **2026-08-06** — Learned SQL/relational databases (SELECT, joins, aggregates, subqueries, PK/FK, many-to-many junction tables) via DBeaver. Added `notebooks/sql/`.
- **2026-08-07** — Converted Student Grade Manager CLI from in-memory storage to SQLite. All 5 menu options now backed by real queries (INSERT, SELECT, aggregates, WHERE filtering).
- **2026-08-08** — Refactored Student Grade Manager into db.py (data layer, returns data) and main.py (application layer, handles input/display). Kept the original cli-app.py for comparison.
- **2026-08-08** — Watched Git & GitHub crash course (branching, merging, conflicts, stash, revert, rebase, PRs). Added `notebooks/git/git-github-fundamentals.md`.
- **2026-08-09** — First contact with Bash: script files, variables, positional arguments (`$1`), `if`/`else` with `-z`/`-d` tests, `for` loops over lists and globs, exit codes (`$?`, `&&`, `||`, `exit`), redirection (`>`, `>>`), and pipes (`|`). Added `notebooks/bash/bash-fundamentals.md`.
- **2026-08-09** — Built a Bash Todo App from scratch: `case`-based command routing (`add`/`list`/`remove`), a SQLite table created via `sqlite3` calls from the script, and safe variable quoting (`'$2'` inside an `INSERT` vs bare `$2` in a numeric `WHERE`). Added `projects/bash-todo-app`.
- **2026-08-10** — Python Part 2: dictionaries, tuples, sets, file I/O (`with open`, read/write/append modes), `try/except` (multiple excepts, `else`/`finally`, raising custom errors, `OSError` for file failures), and `*args`/`**kwargs`. Applied all four directly to the Student Grade Manager CLI — added `export_students_to_file()` and `log_action()` to `main.py`. Added `notebooks/python/python-part-2.md`.