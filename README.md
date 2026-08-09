# mlops-journey
Learning log and projects on my path to MLOps engineering.

# MLOps Journey

Learning log for my path to MLOps engineering.

**Goal:** Backend/cloud engineer first, MLOps engineer after.

**Started:** August 2026

## Phase 1 — Backend foundations

- [x] Git & GitHub
- [ ] Bash
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

- [Student Grade Manager (CLI)](projects/student-grade-manager) — CLI app with SQLite persistence. First project (P1), originally in-memory, rebuilt with a real database.

## Log
- **2026-08-06** — Set up environment (Git, VS Code, Python). Started SQL.
- **2026-08-06** — Learned SQL/relational databases (SELECT, joins, aggregates, subqueries, PK/FK, many-to-many junction tables) via DBeaver.
- **2026-08-07** — Converted Student Grade Manager CLI from in-memory storage to SQLite. All 5 menu options now backed by real queries (INSERT, SELECT, aggregates, WHERE filtering).
- **2026-08-08** — Refactored Student Grade Manager into db.py (data layer, returns data) and main.py (application layer, handles input/display). Kept the original cli-app.py for comparison.
- **2026-08-08** — Watched Git & GitHub crash course (branching, merging, conflicts, stash, revert, rebase, PRs). Added `notebooks/git/git-github-fundamentals.md`.
- **2026-08-09** — First contact with Bash scripting, written and run at the terminal: script files, variables, positional arguments (`$1`), `if`/`else` with `-z`/`-d` tests, `for` loops over lists and globs, exit codes (`$?`, `&&`, `||`, `exit`), redirection (`>`, `>>`), and pipes (`|`). Barely scratched the surface — enough to read a shell command, not to write real scripts yet. Added `notebooks/bash/bash-fundamentals.md`.