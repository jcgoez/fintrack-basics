# TECH5: Hands-On Exercise — FinTrack Nordic

Welcome to the hands-on exercise for **TECH5: Programming and Application Design** at NHH.

In this exercise, you will work in **pairs** to act as **Software Architects**: using Google Antigravity to model an investment portfolio, persist it to SQLite, and write automated tests.

---

## 👥 Pair Programming Workflow

To prepare for **Module 3's Collaborative Project**, you will complete this lab in pairs:

| Role | Primary Responsibilities | Key Antigravity Tools |
| :--- | :--- | :--- |
| **Architect** | Formulates problem requirements, specifies edge cases, writes prompts | Sidebar Agent (`Ctrl+L`), `/plan`, `@`-mentions |
| **Driver** | Operates editor, navigates shortcuts, inspects diffs, runs tests | `Tab` autocomplete, `Ctrl+I` inline, terminal (`pytest`) |

> 🔄 **Role-Swap Checkpoint (Minute 65 / Halfway mark):**  
> After completing Tasks 1 & 2, the Driver and Architect **switch seats and roles** for Tasks 3 & 4. Commit your midway progress using Git co-authorship!

---

## 🚀 Quick Start

1. **Open this project folder in Antigravity.**
2. **Open a terminal** and set up your virtual environment:
   ```bash
   python -m venv .venv
   # Windows PowerShell:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate

   pip install -r requirements.txt
   ```
3. **Run the baseline test suite:**
   ```bash
   pytest
   ```
   *(You should see **3 passed, 6 failed**. As you complete each task with Antigravity, the tests will turn green one by one!)*

---

## 📂 Project Structure

```text
.
├── .agents/
│   └── rules           # Antigravity project rules ("Explain-Before-Accept" policy)
├── src/
│   ├── models.py       # Domain models (Holding, Portfolio)
│   └── database.py     # SQLite persistence layer
├── tests/
│   ├── test_models.py  # Unit tests for domain logic (Task 1 & 2)
│   └── test_db.py      # Tests for database storage (Task 3)
├── requirements.txt    # Project dependencies (pytest)
└── README.md
```

---

## 🎯 Lab Milestones

### Phase 1: The Blueprint (Architect = Student A, Driver = Student B)

#### Task 1: Unrealized P&L via Planning Mode
1. **Architect:** In Sidebar Chat (<kbd>Ctrl+L</kbd> / <kbd>Cmd+L</kbd>), prompt with `/plan`:
   > *"Add an `unrealized_pnl(market_prices: dict[str, float])` method to `Portfolio` in `@src/models.py`. Raise a `KeyError` if any held symbol is missing from market_prices. Return total market value minus total cost."*
2. **Driver:** Review the architectural plan. If correct, approve execution.
3. Inspect the proposed diff in `src/models.py`, accept the change, and run:
   ```bash
   pytest tests/test_models.py -k pnl
   ```

#### Task 2: Input Validation with Inline Command (<kbd>Ctrl+I</kbd>)
1. **Driver:** Highlight the `Holding` class in `src/models.py`.
2. Press <kbd>Ctrl+I</kbd> (or <kbd>Cmd+I</kbd>) and prompt:
   > *"Add input validation: ensure shares > 0 and acquisition_price >= 0, raising ValueError with clear messages."*
3. **Explain-Before-Accept Check:** Ensure Antigravity explains *how* dataclass validation works in Python before accepting the diff.
4. Run tests:
   ```bash
   pytest tests/test_models.py
   ```
   *(All 6 model tests should now pass!)*

---

### 🔄 Role-Swap Checkpoint (Minute 65)
Switch seats! **Student B is now the Architect; Student A is now the Driver.**

Commit your Phase 1 milestone with Git co-authorship:
```bash
git checkout -b feature/fintrack-solution
git add src/models.py
git commit -m "feat(models): implement unrealized PnL and holding validation

Co-authored-by: Partner Name <partner@nhh.no>"
```

---

### Phase 2: The Memory & Process (Architect = Student B, Driver = Student A)

#### Task 3: SQLite Persistence Layer
1. **Architect:** In `src/database.py`, prompt the Sidebar Agent:
   > *"Implement `save_portfolio(portfolio, db_path)` and `load_portfolio(owner, db_path)` using parameterized SQL ('?' placeholders). Connect models from `@src/models.py`."*
2. **Driver:** Review diffs. Verify that **NO** string formatting (`f"..."`) is used inside SQL queries.
3. Run database tests:
   ```bash
   pytest tests/test_db.py
   ```

#### Task 4: Terminal Error Diagnostics & Final Verification
1. Intentionally introduce a typo into a column name in `src/database.py` and run `pytest`.
2. Notice the `sqlite3.OperationalError` in the terminal.
3. Prompt Antigravity:
   > *"Diagnose the error in `@terminal` and repair `@src/database.py`."*
4. Run the full test suite to reach **9 passed, 0 failed**:
   ```bash
   pytest
   ```
5. Commit and push your final solution:
   ```bash
   git add src/ database.py
   git commit -m "feat(db): complete SQLite persistence layer with parameterized queries"
   git push origin feature/fintrack-solution
   ```

---

## 📜 The "Explain-Before-Accept" Policy (.agents/rules)

This project contains `.agents/rules` which instructs Antigravity to explain the architectural pattern before generating code. 

**Why this matters:**
The 4-hour school exam in TECH5 tests **your** conceptual understanding in VS Code. Always make sure you can answer:
1. *Why is `@property` used instead of a standard method for `cost_basis`?*
2. *Why are parameterized queries (`?`) mandatory when persisting business data?*
3. *What happens if a ticker symbol is missing from an external price dictionary?*
