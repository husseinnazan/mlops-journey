# 🐍 Python Part 1 — Notebook
> Syntax · Functions · Loops · Conditionals · Lists

---

## 1. Syntax & Basics

Python is clean. No semicolons, no curly braces. Indentation is everything.

```python
# This is a comment

name = "Hussein"
age = 18
is_student = True

print(name)       # Hussein
print(age)        # 18
print(is_student) # True
```

### Data Types
```python
x = 10          # int
y = 3.14        # float
name = "harara" # string
active = True   # boolean
nothing = None  # null/empty
```

### Basic Operations
```python
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...
print(10 // 3)  # 3  (floor division)
print(10 % 3)   # 1  (remainder)
print(10 ** 3)  # 1000 (power)
```

### String Operations
```python
first = "Hussein"
last = "Harara"

full = first + " " + last     # concatenation
print(full)                    # Hussein Harara
print(len(full))               # 14
print(full.upper())            # HUSSEIN HARARA
print(full.lower())            # hussein harara
print(full.replace("Hussein", "H"))  # H Harara

# f-strings (use these, they're clean)
age = 18
print(f"My name is {first} and I am {age} years old.")
```

### User Input
```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

---

## 2. Conditionals

```python
age = 18

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```

### Comparison Operators
```python
x = 10
print(x == 10)  # True  (equal)
print(x != 5)   # True  (not equal)
print(x > 5)    # True
print(x < 5)    # False
print(x >= 10)  # True
print(x <= 9)   # False
```

### Logical Operators
```python
age = 18
has_id = True

if age >= 18 and has_id:
    print("Access granted.")

if age < 13 or age > 60:
    print("Special discount.")

if not has_id:
    print("No ID, no entry.")
```

### Nested Conditions
```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

---

## 3. Loops

### While Loop
```python
count = 0

while count < 5:
    print(count)
    count += 1

# Output: 0 1 2 3 4
```

### For Loop
```python
for i in range(5):
    print(i)

# Output: 0 1 2 3 4

for i in range(1, 6):
    print(i)

# Output: 1 2 3 4 5

for i in range(0, 10, 2):
    print(i)

# Output: 0 2 4 6 8
```

### Loop Controls
```python
# break — stop the loop
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0 1 2 3 4

# continue — skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output: 1 3 5 7 9
```

### Looping Over a String
```python
name = "Hussein"

for letter in name:
    print(letter)
```

---

## 4. Functions

```python
def greet():
    print("Hello!")

greet()  # Hello!
```

### Parameters & Arguments
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Hussein")  # Hello, Hussein!
```

### Return Values
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

### Default Parameters
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Hussein")           # Hello, Hussein!
greet("Hussein", "Salut")  # Salut, Hussein!
```

### Multiple Return Values
```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(low)   # 1
print(high)  # 9
```

---

## 5. Lists

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple
print(fruits[-1])  # cherry (last item)
print(len(fruits)) # 3
```

### Modifying Lists
```python
fruits = ["apple", "banana", "cherry"]

fruits.append("mango")       # add to end
fruits.insert(1, "orange")   # add at index
fruits.remove("banana")      # remove by value
fruits.pop()                 # remove last item
fruits.pop(0)                # remove at index

print(fruits)
```

### Looping Over Lists
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

### List Slicing
```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])   # [1, 2, 3]
print(numbers[:3])    # [0, 1, 2]
print(numbers[3:])    # [3, 4, 5]
print(numbers[::-1])  # [5, 4, 3, 2, 1] (reversed)
```

### Useful List Methods
```python
numbers = [3, 1, 4, 1, 5, 9]

numbers.sort()           # sort ascending
numbers.sort(reverse=True) # sort descending
numbers.reverse()        # flip the list
print(sum(numbers))      # sum of all
print(min(numbers))      # smallest
print(max(numbers))      # largest
print(numbers.count(1))  # how many times 1 appears
```

### List Comprehension (powerful shortcut)
```python
# Normal way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

# List comprehension way (cleaner)
squares = [i ** 2 for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

---

## 🧪 Practice Exercises

**Exercise 1 — Conditionals:**
Write a program that asks the user for a number and prints whether it's positive, negative, or zero.

**Exercise 2 — Loops:**
Print all numbers from 1 to 100 that are divisible by 3 or 5.

**Exercise 3 — Functions:**
Write a function `total(numbers)` that takes a list and returns the sum of all numbers without using `sum()`.

**Exercise 4 — Lists:**
Create a list of 5 of your favorite things. Sort them alphabetically and print them with their index number.

**Exercise 5 — Combined:**
Write a program that asks the user to enter names one by one (until they type "done"), stores them in a list, then prints the list sorted alphabetically.

---

*Write the code yourself first. Then show me and I'll critique it.* 💪
