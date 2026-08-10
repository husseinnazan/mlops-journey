# 🐍 Python Part 2 — Notebook
> Dicts, Tuples & Sets · File I/O · try/except · *args & **kwargs

---

## 1. Dictionaries, Tuples & Sets

### Dictionaries — key/value pairs
```python
student = {"name": "Hussein", "age": 18, "city": "Nabatieh"}

print(student["name"])        # Hussein
print(student.get("age"))     # 18
print(student.get("grade", "N/A"))  # N/A (default if key missing)

student["age"] = 19           # update
student["email"] = "x@x.com"  # add new key
del student["city"]           # remove a key
```

### Looping Over Dicts
```python
for key in student:
    print(key)

for key, value in student.items():
    print(f"{key}: {value}")

for value in student.values():
    print(value)
```

### Dict Comprehension
```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Tuples — immutable, ordered
```python
point = (3, 4)
x, y = point          # unpacking
print(point[0])        # 3
# point[0] = 5         # ERROR — tuples can't be modified
```

### Sets — unique, unordered
```python
nums = {1, 2, 2, 3, 3, 3}
print(nums)             # {1, 2, 3} — duplicates gone

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)             # {2, 3} intersection
print(a | b)             # {1, 2, 3, 4} union
print(a - b)             # {1} difference
```

---

## 2. File I/O

### Reading — always use `with`
```python
with open("notes.txt", "r") as f:
    content = f.read()        # whole file as a string

with open("notes.txt", "r") as f:
    for line in f:             # memory-efficient, line by line
        print(line.strip())
```
`with` auto-closes the file even if an error happens mid-read — no manual `.close()` needed.

### Writing & Appending
```python
with open("output.txt", "w") as f:   # "w" WIPES the file first
    f.write("Hello\n")

with open("output.txt", "a") as f:   # "a" adds to the end
    f.write("Another line\n")
```

### Mode Cheat Sheet
```python
"r"   # read (file must exist)
"w"   # write (creates or wipes)
"a"   # append (creates or adds to end)
"r+"  # read and write
```

---

## 3. try/except

### Basic Pattern
```python
try:
    choice = int(input("Choose an option: "))
except ValueError:
    print("Not a valid input")
```

### Multiple Excepts
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
```

### else and finally
```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Not a number.")
else:
    print(f"You entered {num}, nice.")     # runs only if no exception
finally:
    print("Done trying.")                   # always runs
```

### File Errors Use OSError, Not ValueError
```python
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except OSError as e:
    print(f"Error was: {e}")
```

### Raising Your Own Errors
```python
def set_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    return age
```

---

## 4. *args and **kwargs

### `*args` — extra positional arguments as a tuple
```python
def add(*args):
    return sum(args)

print(add(1, 2, 3))   # 6
```

### `**kwargs` — extra keyword arguments as a dict
```python
def describe(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe(name="Hussein", age=18)
```

### Combined — order always: regular params → *args → **kwargs
```python
def profile(name, *hobbies, **details):
    print(name, hobbies, details)

profile("Hussein", "coding", "editing", city="Nabatieh", age=18)
```

### Why It Matters — the decorator skeleton (preview)
```python
def wrapper(*args, **kwargs):
    return original_function(*args, **kwargs)
```

---

## 🛠 Applied — Student Grade Manager CLI

These four topics weren't just drilled in isolation — they were applied directly to the real `db.py` / `main.py` project:

```python
def export_students_to_file(filename="backup.txt"):
    students = db.get_all_students()

    student_dict = {}
    for student in students:
        student_dict[student[1]] = student[2]

    try:
        with open(filename, 'w') as w:
            for name, score in student_dict.items():
                w.write(f"{name}: {score}\n")
    except OSError as e:
        print(f"Error was: {e}")


def log_action(action, *details, **meta):
    try:
        with open("activity_log.txt", 'a') as wr:
            wr.write(f"ACTION: {action} | details: {details} | meta: {meta}\n")
    except OSError as e:
        print(f"you have the following error : {e}")
```

This exercises all four topics at once: building a dict from raw DB tuples, writing/appending to files safely with `with`, catching real `OSError` failures instead of crashing, and using `*args`/`**kwargs` for a logging function flexible enough to describe any action.

---

## 🧪 Practice Exercises

**Exercise 1 — Dicts:**
Build a dictionary counting how many times each word appears in a sentence (split it, loop, count).

**Exercise 2 — File I/O:**
Write a function that reads a file line by line and returns a dict of `{line_number: line_content}`.

**Exercise 3 — try/except:**
Write a function that safely converts a list of strings to integers, skipping (not crashing on) any that fail, and returns the valid ones.

**Exercise 4 — *args/**kwargs:**
Write a function `order_summary(customer_name, *items, **details)` that prints the customer, lists items ordered, then prints any extra details like `discount=10`.

**Exercise 5 — Combined:**
Write a function `safe_export(data_dict, filename)` that tries to write a dict to a file (one `key: value` per line), catches `OSError`, and logs the outcome (success or failure) to a separate log file using `*args`/`**kwargs`.

---

*Write the code yourself first. Then show me and I'll critique it.* 💪