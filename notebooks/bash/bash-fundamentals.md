# 🐚 Bash — Notebook

> scripts · variables · arguments · conditionals · loops · exit codes · redirection · pipes

Everything below was written and run at the terminal on August 9, 2026. This is not a Bash mastery notebook — it's the working subset needed to *read* a Dockerfile, a GitHub Actions step, and an AWS startup script in Phase 2 without guessing.

---

## 1. A script is a file full of commands

```bash
echo 'echo "hello from a script"' > test.sh
bash test.sh
# Output: hello from a script
```

That's the whole idea. `test.sh` is an ordinary text file containing one line. `bash test.sh` says *read this file and run every line inside it*.

Anything typed at the prompt can go in a script, and anything in a script can be typed at the prompt. There is no separate "script language" — it's the same shell either way.

---

## 2. Variables

```bash
name="Hussein"
echo "hello $name"
# Output: hello Hussein
```

No `let`, no `var`, no type declaration. A name and a value.

Two rules that bite:

**No spaces around `=`.**

```bash
name="Hussein"      # correct
name = "Hussein"    # ERROR — bash tries to run a command called `name`
```

**The `$` comes first when reading it back.**

```bash
echo "$name"        # → Hussein
echo "name$"        # → name$   (literal text, no expansion)
```

Getting this backwards produced `hello 1$` instead of `hello Hussein` — bash saw `1$` as ordinary characters and stored that as the value.

Variables expand inside **double** quotes but not single:

```bash
echo "hello $name"   # → hello Hussein
echo 'hello $name'   # → hello $name
```

---

## 3. Arguments — input from outside the script

```bash
name="$1"
echo "hello $name"
```

```bash
bash test.sh Hussein    # → hello Hussein
bash test.sh Azan       # → hello Azan
```

`$1` is whatever was typed after the script name. `$2` is the second thing, `$3` the third. Bash fills them in automatically — you never declare them.

Same script, different input each run. That's the point of scripts.

---

## 4. Conditionals

```bash
name="$1"

if [[ -z "$name" ]]; then
    echo "you didn't give me a name"
else
    echo "hello $name"
fi
```

```bash
bash test.sh Hussein    # → hello Hussein
bash test.sh            # → you didn't give me a name
```

Structure notes:

- The `;` before `then` is required
- `fi` closes the block — it's `if` spelled backwards, the same job a closing brace does elsewhere
- `[[ ]]` is where the test goes, with spaces inside the brackets

The single-letter tests used most often:

```bash
[[ -z "$x" ]]      # string is empty
[[ -n "$x" ]]      # string is NOT empty
[[ -d "$x" ]]      # is a directory
[[ -f "$x" ]]      # is a regular file
[[ -e "$x" ]]      # exists (either kind)
```

---

## 5. Loops

Over a hand-written list:

```bash
for topic in git bash sql oop; do
    echo "Phase 1 topic: $topic"
done
# Output: Phase 1 topic: git
#         Phase 1 topic: bash
#         Phase 1 topic: sql
#         Phase 1 topic: oop
```

`do` opens the block, `done` closes it — the same role `then`/`fi` play for `if`. The variable name (`topic`) is your choice; it just has to match the `$topic` used inside.

Over files, which is the version that matters:

```bash
for file in *.sh; do
    echo "Found script: $file"
done
# Output: Found script: loop.sh
#         Found script: test.sh
```

`*.sh` is not a list anyone typed. Bash expands it into every matching filename *before* the loop starts, then runs the block once per file. `*` alone means everything in the directory.

Loop plus conditional — the skeleton behind most practical Bash:

```bash
for file in *; do
    if [[ -d "$file" ]]; then
        echo "$file is a directory"
    else
        echo "$file is a file"
    fi
done
```

*For each thing matching this pattern, test it, act accordingly.* Backup scripts, deploy scripts, cleanup scripts — all variations on those six lines.

---

## 6. Exit codes

Every command finishes with a hidden number. `$?` holds the most recent one.

```bash
ls ~
echo $?              # → 0

ls /nonexistent
echo $?              # → 2
```

**`0` means success.** Anything non-zero means failure. Note the inversion from Python, where 0 is falsy — here, read it as "zero errors occurred."

Different programs use different failure numbers (`ls` returns 2 for a missing path, 1 for lesser problems). Only the zero / non-zero distinction matters.

That number is what `&&` and `||` check:

```bash
mkdir testdir && cd testdir       # cd runs ONLY if mkdir returned 0
ls /nonexistent || echo "failed"  # echo runs ONLY if ls did NOT return 0
```

This is why Dockerfiles chain with `&&` everywhere — it stops a broken step from letting the next one run against a wrong state.

Scripts set their own number with `exit`:

```bash
if [[ -z "$1" ]]; then
    echo "no argument given"
    exit 1
fi
echo "got: $1"
exit 0
```

`exit 1` stops the script immediately and reports failure. A non-zero exit from a test step is exactly how GitHub Actions decides a build is broken.

---

## 7. Redirection

```bash
ls ~ > files.txt      # send output INTO a file, overwriting it
cat files.txt         # → the directory listing

echo "one more" >> files.txt   # APPEND instead
tail -3 files.txt              # → ... / سيسول / one more
```

`>` overwrites. `>>` appends. Confusing them is how files get destroyed.

A detail worth remembering: running `ls ~ > files.txt` produces a listing that **contains `files.txt` itself**. The shell creates the (empty) file first, then runs `ls` — so the file already exists by the time `ls` looks around.

---

## 8. Pipes

```bash
ls ~ | wc -l              # → 29
```

`|` connects one command's output directly to the next command's input, with no file in between. `ls` produces a list; `wc -l` counts lines.

Chain as many as needed:

```bash
ls ~ | grep "s" | wc -l   # → 18
```

Read left to right as a pipeline: list everything → keep only lines containing "s" → count what's left.

This is the Unix idea in one character. Small programs that each do one thing, composed into something bigger. Reading logs in Phase 2 is this exact pattern:

```bash
cat app.log | grep "ERROR" | wc -l
```

---

## Practice Exercises

Write these yourself. **No solutions are provided in this notebook.**

1. **`greet.sh`** — Take a name as `$1` and a greeting word as `$2`, and print them together (`bash greet.sh Hussein hey` → `hey Hussein`). If either is missing, print a usage message instead.

2. **`count-type.sh`** — Loop over everything in the current directory and print only the directories, skipping files. Then print a final line with how many there were. (You'll need a counter variable that starts at 0 before the loop and increments inside it — bash does arithmetic with `$(( ))`, as in `n=$((n + 1))`.)

3. **`check-repo.sh`** — Check whether a `notebooks` directory exists in the current directory. If it does, print how many `.md` files are inside it. If it doesn't, print an error and `exit 1`. Verify it works by running it both inside and outside your `mlops-journey` repo.

4. **`backup.sh`** — Take a directory name as `$1`. If it exists, copy it to `<name>-backup` and confirm success. If it doesn't exist, exit with a non-zero code and a clear message. Use `&&` at least once. Test it on a throwaway directory first, not on real work.

5. **`log-summary.sh`** — The combinatory one. Take a filename as `$1`. Verify the file exists before doing anything. Then print: the total number of lines, the number of lines containing the word `ERROR`, and the last 5 lines of the file. Build the first two using pipes. Make a fake log file with `echo` and `>>` to test against.

Write the code yourself first. Then show me and I'll critique it. 💪
