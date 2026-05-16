# Python PPT Prompts — Oxirgi 24 soat (Tuple, List, Args, Kwargs, Zip, Lambda, Enumerate, Map, Filter)

---

## Slide 1 — List vs Tuple: Asosiy Farq

```
Create a professional PowerPoint slide titled "List vs Tuple — What's the difference?".

Show a side-by-side comparison table with two columns:

LEFT COLUMN (LIST — blue theme):
Header: LIST  [ ]
- Mutable (o'zgartiriladi)
- Square brackets: [ ]
- Example: fruits = ["apple", "lemon", "kiwi", "banana"]
- fruits[2] = "melon"  ← allowed ✅

RIGHT COLUMN (TUPLE — orange theme):
Header: TUPLE  ( )
- Immutable (o'zgartirilmaydi)
- Parentheses: ( )
- Example: animals = ("dog", "cat", "fish", "lion")
- animals[0] = "bird"  ← NOT allowed ❌

Below the table, show an animated diagram:
- List box with arrows showing items being swapped/replaced
- Tuple box with a LOCK icon — items are frozen

Bottom note: "Use TUPLE when data should never change. Use LIST when data changes over time."

Style: dark background, monospace code font, clear icons.
```

---

## Slide 2 — List Indexing & Slicing

```
Create a PowerPoint slide titled "List Indexing & Slicing".

Show this list visually as numbered boxes:
fruits = ["apple", "orange", "lemon", "kiwi"]
Index:      0         1         2        3
Negative:  -4        -3        -2       -1

Then show 4 operations with animated arrows pointing to the result:

1. a = fruits[0]       → "apple"         (single item)
2. b = fruits[0:2]     → ["apple","orange"]  (0 included, 2 excluded — half-open interval)
3. c = fruits[::3]     → ["apple","kiwi"]    (every 3rd item)
4. d = fruits[::-1]    → ["kiwi","lemon","orange","apple"]  (reverse)

For each operation draw an arrow from the list boxes to the result box.
Highlight the [start:stop:step] format at the bottom.

Add a note: "0:2 means index 0 is INCLUDED, index 2 is EXCLUDED — yarim interval"

Style: colorful index boxes, animation per operation.
```

---

## Slide 3 — List Methods

```
Create a PowerPoint slide titled "List Methods — How they mutate the list".

Show starting list: letters = ["a", "d", "b"]

Then show a STEP-BY-STEP animation of each operation changing the list:

Step 1: letters.append("c")    → ["a", "d", "b", "c"]     ← adds to END
Step 2: letters.insert(0, "z") → ["z", "a", "d", "b", "c"] ← adds to FRONT at index 0
Step 3: letters.pop(size)      → removes "c" from END, list = ["z","a","d","b"]
Step 4: letters.pop(0)         → removes "z" from FRONT, list = ["a","d","b"]

Then show second set with animals = ["dog","cat","capybara","fish","lion"]:
Step 5: animals.remove("lion")  → removes by VALUE (not index)
Step 6: del animals[2:4]        → removes slice from index 2 to 3 (capybara, fish)
Step 7: animals.index("cat")    → returns position number: 0
Step 8: animals.clear()         → []  (empty list)

Show a summary table at the bottom:
Method     | Action           | Returns
append()   | add to end       | None
insert()   | add at index     | None
pop()      | remove by index  | removed item
remove()   | remove by value  | None
index()    | find position    | index number
clear()    | empty the list   | None

Style: each step animates the list boxes changing color/disappearing/appearing.
```

---

## Slide 4 — List Sort Methods

```
Create a PowerPoint slide titled "Sorting Lists — sort() vs sorted()".

Show two scenarios:

SCENARIO 1 — sort() MUTATES original:
numbers = [2, 20, 12, 8, 57]
numbers.sort()          → [2, 8, 12, 20, 57]   ← original CHANGED
numbers.sort(reverse=True) → [57, 20, 12, 8, 2] ← original CHANGED again

Draw arrow showing original list being destroyed and replaced.

SCENARIO 2 — sorted() KEEPS original:
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
numbs     → [2, 20, 12, 100]   ← UNCHANGED ✅
new_numbs → [2, 12, 20, 100]   ← NEW sorted list ✅

Draw two separate boxes showing both lists exist at the same time.

Comparison table at bottom:
         | Changes original? | Returns new list?
sort()   |       YES ❌      |       NO
sorted() |       NO ✅       |       YES ✅

Style: red highlight for mutation, green for immutable behavior.
```

---

## Slide 5 — Lambda Function

```
Create a PowerPoint slide titled "Lambda — Anonymous Function".

Show the transformation from regular function to lambda:

REGULAR FUNCTION:
def calculate(x, y):
    return x * y
result = calculate(3, 5)  → 15

LAMBDA (same thing, one line):
def calculate(x, y): return x * y
result = calculate(3, 5)  → 15

Show an animated arrow collapsing the regular function into one line.

Then show the REAL POWER — lambda inside sort():

people = [
  ("Robert", 20),
  ("Steve", 19),
  ("Joseph", 25),
  ("Michael", 30),
  ("Ali", 40)
]

people.sort()
→ sorts alphabetically by NAME (default)
Result: [("Ali",40), ("Joseph",25), ("Michael",30), ("Robert",20), ("Steve",19)]

people.sort(key=lambda person: person[1])
→ sorts by AGE (index 1)
Result: [("Steve",19), ("Robert",20), ("Joseph",25), ("Michael",30), ("Ali",40)]

Show an animated diagram: each tuple box has index[0]=name and index[1]=age.
Arrow from lambda pointing to index[1] (age) showing "this is the sort key".

Formula box: lambda [parameter] : [return expression]
```

---

## Slide 6 — Unpacking Arguments

```
Create a PowerPoint slide titled "Unpacking — Splitting a list into variables".

Show the list first:
groups = ["MIT", "Flexy", "DEVEX", "Mg"]

Then show unpacking with * (star):
(x, y, *z) = groups

Draw animated arrows:
"MIT"   → x  (first item)
"Flexy" → y  (second item)
"DEVEX" + "Mg" → z  (REST — becomes a list: ["DEVEX","Mg"])

Show result boxes:
x = "MIT"
y = "Flexy"
z = ["DEVEX", "Mg"]   ← z is always a LIST

Add a note: "* collects ALL remaining items into a list. It can be placed anywhere."

Show more examples below:
(*a, last) = groups     → a=["MIT","Flexy","DEVEX"], last="Mg"
(first, *mid, last) = groups → first="MIT", mid=["Flexy","DEVEX"], last="Mg"

Style: color-code each variable with its own color, animated arrows from list to variables.
```

---

## Slide 7 — *args (Tuple Arguments)

```
Create a PowerPoint slide titled "*args — Accept Any Number of Arguments (Tuple)".

Show the function definition:
def calculate(*args):
    total = 1
    for x in args:
        total *= x
    return total

Then show 3 different CALLS and trace the value flow:

CALL 1: calculate(1, 7, 2, 3)
         ↓
args = (1, 7, 2, 3)   ← becomes a TUPLE
type(args) → <class 'tuple'>
Loop: total = 1 → 1×1=1 → 1×7=7 → 7×2=14 → 14×3=42
Result: 42

CALL 2: calculate(0, 2, 300)
args = (0, 2, 300)
Loop: 1 → 0 → 0 → 0
Result: 0

CALL 3: calculate(5, 7)
args = (5, 7)
Loop: 1 → 5 → 35
Result: 35

Draw a funnel diagram: multiple values go INTO the function → packaged into ONE tuple inside.

Key rule box: "*args always creates a TUPLE inside the function."
```

---

## Slide 8 — **kwargs (Dictionary Arguments)

```
Create a PowerPoint slide titled "**kwargs — Accept Named Arguments (Dictionary)".

Show the function definition:
def introduce(**kwargs):
    print(type(kwargs))
    print(f"Hi I am {kwargs['name']} and I am {kwargs['age']} years old")

Then show 2 CALLS and trace value flow:

CALL 1: introduce(name="Justin", age=28)
         ↓
kwargs = {"name": "Justin", "age": 28}   ← becomes a DICT
type(kwargs) → <class 'dict'>
kwargs['name'] → "Justin"
kwargs['age']  → 28
Output: "Hi I am Justin and I am 28 years old"

CALL 2: introduce(name="Matt", age=25, single=True)
         ↓
kwargs = {"name": "Matt", "age": 25, "single": True}   ← extra key added!
Output: "Hi I am Matt and I am 25 years old"

Draw a funnel diagram: key=value pairs go IN → packaged into ONE dictionary inside.

Comparison box:
*args   → positional → TUPLE  → accessed by index: args[0]
**kwargs → named     → DICT   → accessed by key: kwargs['name']

Style: show dictionary key→value boxes animated assembling inside the function.
```

---

## Slide 9 — *args + **kwargs Combined

```
Create a PowerPoint slide titled "*args + **kwargs — Combined in One Function".

Show the function:
def greeting(*args, **kwargs):
    print("*args > ", args)
    print("**kwargs >", kwargs)

Then show the CALL with traced value flow:
greeting(
    "hi", True, 10,          ← positional → goes to *args
    name="Matt", age=20      ← named      → goes to **kwargs
)

Draw a SPLIT DIAGRAM:
Input values → function → SPLIT into two containers:
LEFT:  args   = ("hi", True, 10)     ← TUPLE
RIGHT: kwargs = {"name":"Matt","age":20} ← DICT

Show the rule visually:
RULE: Positional args ALWAYS come before keyword args in the call.
greeting("hi", True, 10, name="Matt", age=20)  ✅
greeting(name="Matt", "hi", True, 10)          ❌ SyntaxError

Style: two different colored containers (tuple=blue, dict=orange), animated splitting.
```

---

## Slide 10 — zip()

```
Create a PowerPoint slide titled "zip() — Combine Two Lists Together".

Show two tuples:
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

Draw them as two parallel rows of boxes:
tuple1: [1] [2] [3] [4]
tuple2: [a] [b] [c]

Then animate zip() connecting them with vertical lines:
zipped = zip(tuple1, tuple2)
↓
zipped object → lazy (not computed yet)
result = list(zipped)
↓
[(1,'a'), (2,'b'), (3,'c')]   ← index 4 dropped! (shorter list wins)

Show the PAIRING animation: 1↔a, 2↔b, 3↔c, then 4 has no pair → dropped.

Key notes:
- zip() returns a zip OBJECT (lazy) — must convert to list() to see values
- Result length = length of the SHORTER list
- Each pair becomes a TUPLE

Style: zipper graphic animation showing the two lists being "zipped" together.
```

---

## Slide 11 — enumerate()

```
Create a PowerPoint slide titled "enumerate() — Get Index AND Value Together".

Show the problem without enumerate:
animals = ["dog", "cat"]
for element in enumerate(animals):
    print(element)
Output:
(0, 'dog')   ← returns tuples
(1, 'cat')

Then show the BETTER way with unpacking:
for (index, value) in enumerate(animals):
    print(f"index: {index}, value: {value}")
Output:
index: 0, value: dog
index: 1, value: cat

Draw a diagram showing enumerate() WRAPPING the list:
Original list:   ["dog",    "cat"]
After enumerate: [(0,"dog"), (1,"cat")]  ← adds counter automatically

Show the dictionary equivalent using .items():
car_obj = dict(brand="Ferrari", year=2025)
for (key, value) in car_obj.items():
    ...
→ same pattern: unpack (key, value) pairs

Comparison table:
enumerate(list)    → (index, value) pairs
dict.items()       → (key, value) pairs
zip(list1, list2)  → (item1, item2) pairs

Style: index counter animating +1 for each item.
```

---

## Slide 12 — map()

```
Create a PowerPoint slide titled "map() — Transform Every Item in a List".

Show the data:
cars = [("Ferrari",78), ("Tayota",87), ("Audi",116), ("BMW",109), ("Pagani",33)]

Show MANUAL way (for loop):
new_cars = []
for car in cars:
    new_cars.append(car[0])
→ new_cars = ["Ferrari", "Tayota", "Audi", "BMW", "Pagani"]

Show MAP way:
result_map = map(lambda car: car[0], cars)
→ result_map = <map object>  ← LAZY — not computed yet!
new_cars = list(result_map)
→ ["Ferrari", "Tayota", "Audi", "BMW", "Pagani"]

Draw a CONVEYOR BELT diagram:
Input:  [("Ferrari",78), ("Tayota",87), ...]
          ↓ lambda car: car[0]  (takes only index 0)
Output: ["Ferrari",    "Tayota",    ...]

Show each tuple going through the lambda "machine" and coming out as just the name.

Key notes:
- map() returns a map OBJECT (lazy) — must use list() to get results
- Lambda defines the TRANSFORMATION rule
- Original list is NOT changed

Style: factory/conveyor belt visual with input and output boxes.
```

---

## Slide 13 — filter()

```
Create a PowerPoint slide titled "filter() — Keep Only Items That Pass the Test".

Show the data:
cars = [("Ferrari",78), ("Tayota",87), ("Audi",116), ("BMW",109), ("Pagani",33)]

Show FILTER operation:
result_filter = filter(lambda car: car[1] > 80, cars)
list(result_filter)

Draw a SIEVE/FILTER diagram:
Each car tuple goes through a test gate: car[1] > 80?

("Ferrari", 78)  → 78 > 80? NO  ❌ → DROPPED
("Tayota",  87)  → 87 > 80? YES ✅ → KEPT
("Audi",   116)  → 116 > 80? YES ✅ → KEPT
("BMW",    109)  → 109 > 80? YES ✅ → KEPT
("Pagani",  33)  → 33 > 80? NO  ❌ → DROPPED

Result: [("Tayota",87), ("Audi",116), ("BMW",109)]

Show map() vs filter() comparison:
map()    → TRANSFORMS every item (changes shape)
filter() → SELECTS items (keeps or drops — no change to item itself)

Key notes:
- filter() returns a filter OBJECT (lazy) — must use list()
- Lambda must return True or False
- Original list is NOT changed

Style: sieve/strainer visual with green items passing through, red items blocked.
```

---

## Slide 14 — map() vs filter() vs for loop — Full Comparison

```
Create a PowerPoint slide titled "Three Ways to Process a List — Comparison".

Use this data for all three:
cars = [("Ferrari",78), ("Tayota",87), ("Audi",116), ("BMW",109), ("Pagani",33)]

Show three columns side by side:

COLUMN 1 — FOR LOOP:
new_cars = []
for car in cars:
    new_cars.append(car[0])
→ ["Ferrari","Tayota","Audi","BMW","Pagani"]
Label: "Traditional — verbose but clear"

COLUMN 2 — MAP:
new_cars = list(map(lambda car: car[0], cars))
→ ["Ferrari","Tayota","Audi","BMW","Pagani"]
Label: "Transforms ALL items — concise"

COLUMN 3 — FILTER:
fast = list(filter(lambda car: car[1] > 80, cars))
→ [("Tayota",87),("Audi",116),("BMW",109)]
Label: "Selects SOME items — removes others"

Bottom comparison table:
           | Changes items? | Keeps all items? | Returns
for loop   |     YES        |    depends       | nothing (you append manually)
map()      |     YES        |    YES (all)     | map object → list()
filter()   |     NO         |    NO (some)     | filter object → list()

Style: three parallel columns with colored borders, arrows showing input → output.
```

---

## Slide 15 — Value Flow Master Chart (Barcha mavzular birlashgan)

```
Create a PowerPoint slide titled "How Values Flow Through Python Functions".

Draw one large flow diagram connecting ALL topics from today:

START: Raw data
cars = [("Ferrari",78), ("Tayota",87), ("Audi",116), ("BMW",109), ("Pagani",33)]

BRANCH 1 → enumerate():
for (index, value) in enumerate(cars):
→ Adds index counter: (0,("Ferrari",78)), (1,("Tayota",87))...

BRANCH 2 → map():
map(lambda car: car[0], cars)
→ Extracts names: ["Ferrari","Tayota","Audi","BMW","Pagani"]

BRANCH 3 → filter():
filter(lambda car: car[1] > 80, cars)
→ Keeps fast cars: [("Tayota",87),("Audi",116),("BMW",109)]

BRANCH 4 → sort with lambda:
cars.sort(key=lambda car: car[1])
→ Sorts by speed: [("Pagani",33),("Ferrari",78),("Tayota",87),("BMW",109),("Audi",116)]

Show all 4 branches coming from the same original list.
Each branch has a different colored path.
At the end of each branch, show the final output box.

Add note: "All these tools process the SAME list differently. Original list stays unchanged (except sort)."

Style: tree/flowchart diagram, each branch a different color, animated path tracing.
```

---

*Har bir promptni alohida Claude suhbatiga tashlang. Eng yaxshi natija uchun bitta prompt = bitta suhbat.*
