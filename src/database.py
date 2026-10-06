"""SQLite persistence layer for FinTrack Nordic."""
import sqlite3
from typing import Optional
from src.models import Portfolio, Holding


def init_db(db_path: str = "fintrack.db") -> None:
    """Initializes the database schema if it does not already exist."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS holdings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                portfolio_owner TEXT NOT NULL,
                symbol TEXT NOT NULL,
                shares REAL NOT NULL,
                acquisition_price REAL NOT NULL
            );
        """)
        conn.commit()


def save_portfolio(portfolio: Portfolio, db_path: str = "fintrack.db") -> None:
    """
    Persists a Portfolio object and its holdings into the SQLite database.

    TODO (Task 3): Implement using parameterized SQL ('?' placeholders):
    1. Initialize the DB schema if not present.
    2. Remove existing records for this portfolio owner.
    3. Insert all current holdings using executemany with parameterized queries.
    """
    raise NotImplementedError("Task 3: Implement save_portfolio using parameterized SQL")


def load_portfolio(owner: str, db_path: str = "fintrack.db") -> Optional[Portfolio]:
    """
    Retrieves a Portfolio and its holdings by owner name.

    TODO (Task 3 extension):
    1. Query holdings where portfolio_owner = ?
    2. Convert retrieved rows into Holding objects.
    3. Return a Portfolio(owner=owner, holdings=[...]).
    """
    raise NotImplementedError("Task 3 extension: Implement load_portfolio")
