# Bash Todo App

A single-file command-line todo list, written in Bash, backed by SQLite.

Built as a hands-on project for the Bash topic in [mlops-journey](../../) — the goal wasn't the app itself, it was learning `case` branching, `sqlite3` from the shell, and safe variable quoting by building something real instead of doing isolated exercises.

## Usage

```bash
todo add "buy milk"     # add a new task
todo list                # show all tasks
todo remove 2            # remove the task with that id
```

## How it works

- Tasks are stored in a real SQLite database at `~/.config/todo-app/db.sqlite`, created automatically on first run.
- `$1` selects the command (`add` / `list` / `remove`) via a `case` statement; `$2` carries the task text or id.
- Each command shells out to `sqlite3` with a plain SQL string — there's no ORM or library involved, just the same `sqlite3 "$DB_PATH" "..."` pattern for every operation.

## Setup

```bash
chmod +x bash-todo-app.sh
```

Optionally add it to your `PATH` as `todo` so it can be run from anywhere:

```bash
sudo ln -s "$(pwd)/bash-todo-app.sh" /usr/local/bin/todo
```

## Notes / known limitations

- **Ids are never reused.** `AUTOINCREMENT` guarantees a deleted task's id never gets assigned to a new one, so `list` can show gaps (e.g. `2, 4, 5`) after a removal. This is intentional — see the commit history / journey log for the reasoning.
- **No edit command.** Only add, list, and remove exist for now.
- **Task text with a single quote will break the insert.** e.g. `todo add "dad's car"` — the SQL string isn't escaped. Known issue, not yet fixed.

## Built while learning

- `case` statements for multi-way branching
- Calling `sqlite3` from a shell script
- Quoting rules: why `'$2'` needs quotes in an `INSERT` but `$2` doesn't in a numeric `WHERE`
- `mkdir -p` for idempotent directory setup