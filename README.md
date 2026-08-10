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
- [x] OOP — classes, `__init__`, instance vs. class attributes (incl. attribute lookup/shadowing), inheritance (`super()`, overriding + extending a parent method). Composition deliberately scoped out — not needed for StudyMind. Applied to the `Car` example.
- [ ] Type hints (+ `typing` module: `List`, `Dict`, `Optional`, `Union`, etc.) — **in progress**
- [ ] Decorators (+ closures)
- [ ] Context managers
- [ ] JSON
- [ ] HTTP requests (+ Wikipedia search script using `requests`)
- [ ] asyncio & requests vs. aiohttp *(last standalone topic, right before FastAPI)*
- [ ] FastAPI *(official tutorial — learned hands-on while building StudyMind below, not a separate pre-read)*
- [ ] StudyMind — FastAPI + SQLite + LLM API *(capstone — final item, uses everything above; retry decorator catches standard exceptions, not a custom hierarchy)*

**Note:** Custom exception handling dropped as a dedicated Phase 1 topic — basic `try/except`/`OSError` handling is already covered (Python Part 2, Student Grade Manager). Foundational DSA (arrays, hash maps, linked lists, stacks/queues, trees, recursion) postponed out of Phase 1 entirely — moved to a bridge topic right before Phase 1.5's daily NeetCode/Grind75 grind starts, so it's learned right when it's needed instead of sitting unused.

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
- **2026-08-10** — Roadmap update: tied closures explicitly into the Decorators topic (a decorator is a closure that returns a wrapped function), added a small Wikipedia-search script (using `requests`) as the practice project right after HTTP requests, marked Unit testing as optional if the 6-week window runs tight, and added `asyncio` + `requests` vs. `aiohttp` as a topic right before FastAPI, since FastAPI is async-first.
- **2026-08-10** — OOP, first pass: built a `Car` class (`__init__`, instance attributes, a class attribute `office_costs`) and self-assessed it against the roadmap. Found inheritance and composition were missing, plus the instance-vs-class attribute distinction was never actually tested. Taught: attribute lookup order (instance shadows class, never overwrites it), inheritance (`super().__init__()`, overriding + extending a parent method), and composition (has-a vs. is-a) via standalone `Animal`/`Dog` and `Engine`/`Vehicle` examples.
- **2026-08-10** — Roadmap restructure: OOP scoped down to drop composition, keeping only inheritance — checked off. Foundational DSA pulled out of Phase 1 entirely, moved to a bridge topic immediately before Phase 1.5's daily grind starts, so it's taught right when needed rather than sitting unused for weeks. Custom exception handling dropped as a dedicated topic — basic `try/except`/`OSError` (already covered) is enough; StudyMind's retry decorator will catch standard exceptions instead of a custom hierarchy. New Phase 1 order: Git → Bash → OOP → Type hints → Decorators → Context managers → JSON → HTTP requests → asyncio → FastAPI → capstone. Starting Type hints today.
