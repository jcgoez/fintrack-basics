"""Tests for SQLite database persistence in FinTrack Nordic."""
import sqlite3
import pytest
from src.models import Holding, Portfolio
from src.database import init_db, save_portfolio, load_portfolio


@pytest.fixture
def test_db_path(tmp_path):
    """Provides a fresh isolated SQLite database path for each test."""
    db_file = tmp_path / "test_fintrack.db"
    init_db(str(db_file))
    return str(db_file)


def test_init_db_creates_table(test_db_path):
    """Verifies that holdings table schema is properly initialized."""
    with sqlite3.connect(test_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='holdings';")
        row = cursor.fetchone()
        assert row is not None, "holdings table was not created"


def test_save_portfolio_persists_data(test_db_path):
    """Task 3 Check: Ensures save_portfolio persists all holdings using parameterized queries."""
    h1 = Holding(symbol="NHH", shares=50.0, acquisition_price=100.0)
    h2 = Holding(symbol="EQNR", shares=10.0, acquisition_price=300.0)
    portfolio = Portfolio(owner="Lars Jaffke", holdings=[h1, h2])

    save_portfolio(portfolio, test_db_path)

    with sqlite3.connect(test_db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT symbol, shares, acquisition_price FROM holdings WHERE portfolio_owner = ? ORDER BY symbol",
            ("Lars Jaffke",)
        )
        rows = cursor.fetchall()

    assert len(rows) == 2
    assert rows[0] == ("EQNR", 10.0, 300.0)
    assert rows[1] == ("NHH", 50.0, 100.0)


def test_save_and_load_roundtrip(test_db_path):
    """Task 3 Extension Check: Save a portfolio and load it back as a full domain object."""
    h = Holding(symbol="FRO", shares=15.0, acquisition_price=250.0)
    original_portfolio = Portfolio(owner="Paloma de Lima", holdings=[h])

    save_portfolio(original_portfolio, test_db_path)
    loaded_portfolio = load_portfolio("Paloma de Lima", test_db_path)

    assert loaded_portfolio is not None
    assert loaded_portfolio.owner == "Paloma de Lima"
    assert len(loaded_portfolio.holdings) == 1
    assert loaded_portfolio.holdings[0].symbol == "FRO"
    assert loaded_portfolio.holdings[0].shares == 15.0
    assert loaded_portfolio.holdings[0].acquisition_price == 250.0
