# mlops-journey
Learning log and projects on my path to MLOps engineering.

# MLOps Journey

Learning log for my path to MLOps engineering.

**Goal:** Backend/cloud engineer first, MLOps engineer after.

**Started:** August 2026

## Current focus
- [x] SQL fundamentals
- [ ] Linux & Bash
- [x] Git
- [ ] FastAPI + SQLite backend
- [ ] Docker
- [ ] Deploy something live

## Projects

- [Student Grade Manager (CLI)](projects/student-grade-manager) — CLI app with SQLite persistence. First project (P1), originally in-memory, rebuilt with a real database.

## Log
- **2026-08-06** — Set up environment (Git, VS Code, Python). Started SQL.
- **2026-08-06** — Learned SQL/relational databases (SELECT, joins, aggregates, subqueries, PK/FK, many-to-many junction tables) via DBeaver.
- **2026-08-07** — Converted Student Grade Manager CLI from in-memory storage to SQLite. All 5 menu options now backed by real queries (INSERT, SELECT, aggregates, WHERE filtering).
- **2026-08-08** — Refactored Student Grade Manager into db.py (data layer, returns data) and main.py (application layer, handles input/display). Kept the original cli-app.py for comparison.
- **2026-08-08** — Watched Git & GitHub crash course (branching, merging, conflicts, stash, revert, rebase, PRs). Added `notebooks/git/git-github-fundamentals.md`.