# Antigravity Rules for TECH5: Programming and Application Design (NHH)

## 1. Pedagogical Policy: "Explain-Before-Accept"
- Always explain the "why" before proposing code changes. When introducing or modifying Python patterns (e.g., `@property`, `@dataclass`, `field(default_factory=...)`, `sqlite3` context managers, exception handling), provide a concise 2-sentence explanation of:
  1. The software engineering principle / design pattern being applied.
  2. How this pattern prevents runtime bugs or ensures business data integrity.
- Write code that teaches students concepts relevant to the 4-hour closed-book school exam.

## 2. Code Quality & Standards
- Adhere strictly to PEP 8 style standards.
- Use explicit Python type hints on all function signatures and dataclass attributes (e.g., `dict[str, float]`, `list[Holding]`).
- Write descriptive docstrings for all classes and public methods explaining arguments, return types, and potential raised exceptions.

## 3. Database & SQL Security
- NEVER use string formatting (`f"..."` or `+`) to construct SQL queries.
- ALWAYS use parameterized queries with `?` placeholders to enforce SQL injection defense.
- Always manage database connections using context managers (`with sqlite3.connect(...) as conn:`).
