# Python PPT Prompts

## Slide 1 — Python Builtins

```
Create a PowerPoint slide titled "Python Built-in Tools".
Show 3 categories in separate colored boxes with icons:
- TYPES: int, float, str, list, dict (blue box)
- FUNCTIONS: print(), len(), input(), type() (green box)
- CONSTANTS: True, False, None (orange box)
Add an animated arrow showing: "dir(__builtins__) → shows ALL built-in tools list"
Style: dark background, monospace font for code.
```

---

## Slide 2 — Primitive Types

```
Create a PowerPoint slide titled "Python Primitive Data Types".
Show a comparison table with 3 rows: Number, String, Boolean.
For each row show: Type name | Example value | Useful methods.
- Number: 100 | bit_count(), numerator
- String: "AI Python Fullstack" | upper(), title(), replace()
- Boolean: True / False | bool(), isnumeric()
Add an animated diagram showing variable as a "reference label" pointing to a value in memory (not a storage box like Java).
```

---

## Slide 3 — Truthy vs Falsy

```
Create a PowerPoint slide titled "Truthy vs Falsy Values".
Left side (red): FALSY values list — False, 0, "", None
Right side (green): TRUTHY values list — True, 100, -100, "MIT"
In the middle show the "or" operator logic as a flowchart animation:
- Start from left → check each value → if falsy skip → if truthy STOP and return it.
Show example: "" or False or 0 or None or 0 → returns 0 (last falsy)
Bottom note: bool(0) = False, bool("MIT") = True
```

---

## Slide 4 — Functions: Define vs Call

```
Create a PowerPoint slide titled "Functions: Define vs Call".
Show two panels side by side with animation:
Left panel (building icon): DEFINE — "def greet(name):" code block
Right panel (play button icon): CALL — "greet('Matt')" code block
Animate an arrow from CALL → DEFINE → executes → returns result.
Add a note: "Function = reusable block of code. Python uses indentation instead of { } like Java."
```

---

## Slide 5 — Parameters vs Arguments & Default Values

```
Create a PowerPoint slide titled "Parameters vs Arguments".
Top section: show "def give_greet(name, age=30)"
Highlight "name" and "age=30" as PARAMETERS with labels.
Arrow pointing down to: give_greet("Jack") → "Jack" labeled as ARGUMENT.
Show that age=30 is DEFAULT — used when not provided.
Animation: first call with both args, second call with only name → default age fills in automatically.
Show result: "Hi Jack, you are 30 years old!"
```

---

## Slide 6 — Scope

```
Create a PowerPoint slide titled "Scope in Python".
Draw two nested boxes:
- Outer big box labeled "GLOBAL scope" containing: b = 100
- Inner smaller box labeled "LOCAL scope (inside function)" containing: a, b, c variables
Animate: when calculate(5, 50) is called, local b=50 overrides global b=100 inside the function.
Add priority rule at bottom: "Local scope has higher priority than Global scope."
```

---

## Slide 7 — Objects & OOP

```
Create a PowerPoint slide titled "Everything is an Object in Python".
Center: Python logo
Radiating outward with animated lines: str object, int object, bool object, module object, array object
Each node shows: type('Hello') → <class 'str'>
Bottom section: OOP 4 Pillars as 4 colored columns — Encapsulation, Abstraction, Inheritance, Polymorphism.
```

---

## Slide 8 — Class Blueprint

```
Create a PowerPoint slide titled "Class = Blueprint for Objects".
Left side: Blueprint/template labeled "class Person" showing: name, age (state) + introduce(), say_age() (methods)
Right side: 3 separate boxes labeled person1 (Matt,25), person2 (John,30), person3 (Jack,35)
Animate arrow from blueprint → each object being "created" (instantiated).
Show __init__ as the constructor that runs automatically on creation.
```

---

## Slide 9 — Ordinary vs Static Properties

```
Create a PowerPoint slide titled "Ordinary vs Static (Class) Properties".
Two columns with different colors:
Left (ORDINARY/INSTANCE): accessed via object — person1.name → belongs to that object only
Right (STATIC/CLASS): accessed via class — Person.message → shared by ALL objects
Animate: change static property → all objects see the change. Change ordinary → only that object changes.
Show @classmethod decorator highlighted in code.
```

---

## Slide 10 — Magic/Dunder Methods

```
Create a PowerPoint slide titled "Special (Dunder) Methods".
Show a table with 2 columns: Method name | When it triggers automatically
__new__ → before object is created
__init__ → when object is created
__str__ → when print(object) is called
__call__ → when object() is called like a function
__len__ → when len(object) is called
__eq__ → when object == other is used
Animate each row appearing with a real code example from the Car class (Ferrari, Lamborghini).
```

---

## Slide 11 — Iterable Objects

```
Create a PowerPoint slide titled "Iterable Objects in Python".
Center: "for loop" icon
Radiating outward: list, tuple, set, dict, string, range, map, filter — each as a colored badge.
Animate "MIT" string being iterated: M → I → T appearing one by one.
Show range(3) → 0, 1, 2 as a number line animation.
Bottom: "If you can use for loop on it → it is ITERABLE"
```

---

## Slide 12 — Dictionary

```
Create a PowerPoint slide titled "Dictionary (like JSON object)".
Show a visual key→value map:
"name" → "Matt"
"age" → 25
"single" → True
Animate 3 ways to access: dict["key"], dict.get("key"), dict.get("key", default)
Show difference: dict["missing"] → KeyError crash (red X), dict.get("missing") → None (green check).
Show del keyword removing a key with animation.
```

---

## Slide 13 — Error Handling

```
Create a PowerPoint slide titled "Error Handling: try / except / else / finally".
Show a flowchart animation:
try block → runs first
  ↓ error? → except block (catches error, shows message)
  ↓ no error? → else block (success message)
  ↓ always → finally block (always runs, cleanup)
Use traffic light colors: try=yellow, except=red, else=green, finally=blue.
Show real example: accessing car_dict.speed → AttributeError caught.
```
