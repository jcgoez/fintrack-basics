---
description: Enforce Google Python Style Guide rules and consistent coding standards across Python files.
trigger: glob
globs: "**/*.py"
---

# Python Code Style Rules

When writing, editing, or reviewing Python code, strictly adhere to the following rules based on the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

## Core Philosophy

- **BE CONSISTENT**: Always match the style and conventions of the surrounding code.
- Prioritize consistency with existing project patterns when they are well-established.

---

## Language Rules

### 1. Imports
- Import packages and modules only; do not import individual classes or functions directly (exceptions: `typing` and `collections.abc`).
- Group imports into three sections separated by a blank line:
  1. Standard library imports
  2. Third-party library imports
  3. Application-specific imports
- Alphabetize imports within each section.
- Use absolute imports, never relative imports.
- Place one import per line.

```python
# YES
import os
import sys

import numpy as np
import tensorflow as tf

from myproject.backend import api_utils
from doctor.who import jodie

# NO
from sound_effects.utils import EffectsRegistry  # Do not import classes directly
from ..utils import helpers                     # Avoid relative imports
```

### 2. Exceptions
- Never use bare `except:` clauses or catch `Exception` without re-raising or logging appropriately.
- Handle specific exception types.

```python
# YES
try:
    result = risky_operation()
except ValueError as e:
    logging.error("Invalid value: %s", e)
    raise

# NO
try:
    result = risky_operation()
except:
    pass  # Suppresses all errors silently
```

### 3. Type Annotations
- Annotate all function and method signatures (parameters and return types).
- Use built-in generic types (`list[str]`, `dict[str, Any]`, `tuple[int, ...]`) rather than `typing.List`, `typing.Dict` (Python 3.9+).
- Use modern union syntax (`X | None`, `int | float`) instead of `Optional[X]` or `Union[X, Y]`.
- Always use `None` rather than `type(None)` or `NoneType`.
- Import symbols directly from `typing` or `collections.abc`: `from typing import Any`, `from collections.abc import Sequence, Mapping`.

```python
# YES
def fetch_data(url: str, timeout: int = 30) -> dict[str, Any]:
    """Fetches data from URL."""
    ...

def process_items(items: list[str]) -> None:
    """Processes a list of items."""
    ...
```

### 4. Default Argument Values
- **NEVER** use mutable objects (e.g., lists, dicts, set instances) as default parameter values.
- Use `None` as the default and initialize the mutable object inside the function body.

```python
# YES
def foo(a: int, b: list[int] | None = None) -> None:
    if b is None:
        b = []
    b.append(a)

# NO
def foo(a: int, b: list[int] = []) -> None:  # Mutable default is shared across calls
    b.append(a)
```

### 5. True/False Evaluations
- Use implicit false in boolean conditions for empty sequences, `None`, and zero.
- Never compare booleans explicitly to `True` or `False`.

```python
# YES
if not users:
if not some_dict:
if value:

# NO
if len(users) == 0:
if users == []:
if value == True:
```

### 6. Comprehensions & Generators
- Use list/dict/set comprehensions and generator expressions for simple cases.
- If a comprehension spans multiple lines or contains nested loops/conditions, refactor to standard `for` loops.

```python
# YES
result = [x for x in data if x > 0]
squares = (x**2 for x in range(10))

# NO
result = [
    x.strip().lower() for x in data
    if x and len(x) > 5 and not x.startswith('#')
    for y in x.split(',') if y
]  # Too complex; use regular loops
```

### 7. Lambda Functions
- Use lambdas strictly for one-line transformations (e.g., `key=` arguments).
- For multi-line logic or complex operations, define a named local or module-level function.

```python
# YES
sorted(data, key=lambda x: x.timestamp)
```

---

## Style & Formatting Rules

### 1. Line Length & Indentation
- Maximum line length: **80 characters** (exceptions: long import paths, URLs, unsplittable string literals).
- Indentation: **4 spaces** per indentation level. Tabs are prohibited.
- Hanging indents: Align wrapped elements vertically with the opening delimiter or use a 4-space hanging indent.

```python
# Aligned with opening delimiter
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Hanging indent (4 spaces)
foo = long_function_name(
    var_one, var_two, var_three,
    var_four
)
```

### 2. Blank Lines
- 2 blank lines between top-level functions and class definitions.
- 1 blank line between method definitions inside a class.
- Use single blank lines inside function bodies sparingly to separate logical sections.

### 3. Naming Conventions

| Identifier Type | Convention | Example |
|---|---|---|
| Packages & Modules | `lower_with_under` | `game_logic.py` |
| Classes | `CapWords` | `TicTacToeBoard` |
| Functions & Methods | `lower_with_under()` | `check_winner()` |
| Constants | `CAPS_WITH_UNDER` | `MAX_RETRIES` |
| Variables | `lower_with_under` | `player_turn` |
| Internal/Private | `_leading_underscore` | `_internal_state` |

- Never use dashes (`-`) in module names or identifiers.
- Single-letter variables should only be used for iteration counters (`i`, `j`, `k`) or coordinate keys (`x`, `y`).
- Reserve `__double_leading_and_trailing__` names for Python special attributes and dunder methods.

### 4. Comments & Google-Style Docstrings
- All public modules, classes, functions, and methods MUST have docstrings adhering to the **Google Docstring format**.
- Docstring sections should include `Args:`, `Returns:`, and `Raises:` when applicable.

```python
def fetch_smalltable_rows(
    table_handle: smalltable.Table,
    keys: Sequence[bytes | str],
    require_all_keys: bool = False,
) -> Mapping[bytes, tuple[str, ...]]:
    """Fetches rows from a Smalltable.

    Args:
        table_handle: An open smalltable.Table instance.
        keys: A sequence of strings representing the key of each table
            row to fetch. String keys will be UTF-8 encoded.
        require_all_keys: If True, raise ValueError if any key is missing.

    Returns:
        A dict mapping keys to the corresponding table row data fetched.
        Each row is represented as a tuple of strings.

    Raises:
        IOError: An error occurred accessing the smalltable.
        ValueError: A key is missing and require_all_keys is True.
    """
    ...
```

- Comments must be complete sentences with proper punctuation.
- Inline comments must be separated by at least 2 spaces from code and used sparingly.

### 5. Strings & Logging
- Use **f-strings** for string interpolation and display formatting.
- For `logging` statements, use `%` formatting to enable lazy evaluation.

```python
# String formatting
formatted_str = f"Player {player_name}: score={score}"

# Logging
logging.info("Player %s scored %d points", player_name, score)
```

### 6. Resources & Context Managers
- Always use `with` statements (context managers) when managing files, sockets, locks, or database connections.

```python
with open("data.txt", mode="r", encoding="utf-8") as f:
    data = f.read()
```

### 7. Script Entry Points
- Every executable Python script must use a `main()` function guarded by `if __name__ == "__main__":`.

```python
def main() -> None:
    ...

if __name__ == "__main__":
    main()
```

### 8. Function Length
- Keep functions concise, single-purpose, and cohesive.
- Functions exceeding ~40 lines should be evaluated for refactoring into smaller helpers.

---

## Type System Best Practices

- **Generics**: Explicitly parameterize generic collections (e.g., `list[int]`, not bare `list`).
- **Forward References**: Use string quotes for forward references if `from __future__ import annotations` is not active.
- **Type Aliases**: Use `TypeAlias` for complex types (`ConnectionOptions: TypeAlias = dict[str, str]`).
- **TypeVars**: Use descriptive names or `_T` for generic TypeVars (`_T = TypeVar("_T")`).

---

## Quality & Linting
- All Python code must be lint-clean with `pylint` and adhere to formatting standards.
- Suppress lint warnings only with inline comments explaining the rationale (e.g., `# pylint: disable=...`).
