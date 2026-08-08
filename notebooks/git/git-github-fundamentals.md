# 🌱 Git & GitHub — Notebook

> init/add/commit · branching · merging · conflicts · stash · revert · rebase · push/fetch/pull · pull requests

This is the tool you'll touch every single day from here on — every phase, every project, every commit to `mlops-journey`. You already have real scar tissue with it (your divergent-branch merge conflict, the pathspec error), so a lot of this should click into "oh, *that's* what was happening" rather than feeling brand new.

---

## 1. The three-stage model

Git tracks changes through three areas:

```
Working Directory  →  Staging Area  →  Local Repository  →  Remote (GitHub)
   (edit files)         (git add)        (git commit)          (git push)
```

You edit freely in the working directory. `git add` marks a file "ready to be saved." `git commit` actually saves it permanently to your local history. `git push` sends that history to GitHub.

```bash
git status          # shows what's modified, staged, or untracked — your constant check-in command
git add file.py      # stage one file
git add .            # stage everything in and below the current directory
git add -A           # stage everything in the ENTIRE repo, regardless of where you are
git commit -m "message"   # save staged changes permanently, with a message
```

**`git add .` vs `git add -A`** — the distinction that trips people up: `.` only stages what's in your current folder downward; `-A` stages the whole repo including deletions elsewhere. In your `mlops-journey` repo, running `git add .` from inside `notebooks/python/` would miss changes in `notebooks/sql/`.

---

## 2. Undoing things — three different tools, three different jobs

This is the part people get wrong most, because the commands sound similar but do very different things:

| Command | What it does | When to use |
|---|---|---|
| `git restore file.py` | Reverts an **uncommitted** file back to its last commit | "I messed up this edit, throw it away" |
| `git reset` | Unstages files (moves them back to working directory) | "I `git add`ed too early" |
| `git reset --hard` | Unstages **and** discards uncommitted changes entirely | Nuclear option — use carefully |
| `git revert <commit-id>` | Creates a **new commit** that undoes an old one, keeping history intact | Undoing something already pushed/shared |

The key distinction: `reset` rewrites history (dangerous once pushed and shared), `revert` adds to history (safe, always). If you've already pushed a bad commit that a cousin or teammate might have pulled, `revert` — never `reset` — is the correct tool.

```python
# db.py — imagine you just broke this file experimenting
def get_connection():
    return sqlite3.connect("grades.db")  # accidentally deleted the return

# Not yet staged? →
git restore db.py

# Already staged with `git add`? →
git restore --staged db.py
git restore db.py
```

---

## 3. Branching — your own experiment space

A branch is an independent line of work. `main` stays stable; you branch off it to try things without risking what already works.

```bash
git branch                 # list branches, * marks current one
git branch feature-x       # create a new branch
git checkout feature-x     # switch to it
git checkout -b feature-x  # create AND switch in one command — the one you'll actually use daily
```

New branches start as an exact copy of whatever branch you were on. Nothing you commit on `feature-x` touches `main` until you merge it.

```bash
# Real scenario in your repo: adding a new notebook without risking main
git checkout -b add-git-notebook
# ... create the file, git add, git commit ...
git checkout main
git merge add-git-notebook
```

---

## 4. Merge conflicts — what's actually happening

A conflict happens when the *same lines* of the *same file* were changed differently on two branches Git is trying to combine. Git can't guess which version is "right," so it stops and marks the file:

```python
def calculate_average(grades: list[float]) -> float:
<<<<<<< HEAD
    return sum(grades) / len(grades)
=======
    return round(sum(grades) / len(grades), 2)
>>>>>>> feature-branch
```

Everything between `<<<<<<< HEAD` and `=======` is your current branch's version. Everything between `=======` and `>>>>>>> feature-branch` is the incoming branch's version. You manually pick, edit, or combine — then delete the markers entirely, `git add` the file, and commit.

This is exactly what you hit with your divergent branches earlier — now you have the mental model for *why* it happened, not just how you fixed it.

---

## 5. Stash — pausing work without committing it

Git won't let you switch branches with uncommitted changes that would get overwritten. `git stash` sets those changes aside temporarily so you can switch cleanly.

```bash
git stash          # save uncommitted work, clean working directory
git checkout other-branch   # now this works even mid-edit
# ... do whatever you needed to do ...
git checkout original-branch
git stash pop       # bring your stashed work back AND remove it from the stash list
git stash apply     # bring it back but KEEP it in the stash list too (for reuse)
git stash list       # see everything currently stashed
```

`pop` = restore and delete from stash. `apply` = restore and keep a copy in stash. That's the one distinction to remember.

---

## 6. Push, fetch, pull

```bash
git push origin main    # send your local commits to GitHub
git fetch               # download remote changes, but DON'T merge them into your files yet
git pull                # fetch + merge in one step — the one you'll use most often
```

`fetch` alone is useful when you want to see what changed remotely before deciding whether to merge it in. `pull` is the everyday command.

---

## 7. Rebase — cleaner history, use with care

Instead of merging (which creates an extra "merge commit"), rebase replays your branch's commits on top of the latest version of another branch — resulting in a straight, linear history.

```bash
git checkout feature-branch
git rebase main   # feature-branch's commits now sit on top of main's latest commits
```

**Rule to actually follow:** only rebase branches that are yours alone and haven't been pushed/shared yet. Rebasing rewrites commit IDs — if someone else already pulled the old version, their history and yours will no longer match, and things break. For your solo work on `mlops-journey` right now, rebase is completely safe to use.

---

## 8. Pull requests (PRs)

A PR is a request to merge one branch into another, with a review step in between — even solo, this is worth practicing since it's how virtually all real engineering teams work.

Flow: push your branch → open a PR on GitHub (base: `main`, compare: `your-branch`) → review the diff → merge.

```bash
git checkout -b notebook-git
# ... work, commit ...
git push origin notebook-git
# then open the PR on github.com/husseinnazan/mlops-journey
```

---

## Practice Exercises

No solutions included — write the commands yourself, run them for real in `mlops-journey`, and bring back what you did.

1. **Branch and merge, cleanly.** In `mlops-journey`, create a new branch called `notebook-git`. Add this notebook file to it inside a new `notebooks/git/` folder. Commit it, switch back to `main`, and merge `notebook-git` in.

2. **Cause and resolve a real conflict.** Create a second branch from `main`. On `main`, edit one line of your repo's `README.md`. On the second branch, edit that *same line* differently. Try to merge the second branch into `main` and resolve the conflict that results — for real, not hypothetically.

3. **Stash mid-work.** Start editing any file in `db.py` or `main.py` from your Student Grade Manager project without committing. Without discarding the edit, stash it, switch to a different branch, switch back, and pop your stash to confirm your edit is still there.

4. **Revert a real commit.** Make a small, clearly-labeled commit to any notebook file (e.g. add a throwaway line). Then use `git revert` — not `reset` — to undo it, and confirm with `git log --oneline` that both the original commit and the revert commit are visible in history.

5. **Rebase and open a real PR.** Create a new branch, make at least two separate commits on it (not one — two), then rebase it onto the latest `main`. Push the branch to GitHub and actually open a pull request comparing it against `main`. Don't merge it yet — just get it open and review the diff GitHub shows you.

Write the code yourself first. Then show me and I'll critique it. 💪
