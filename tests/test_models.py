"""Unit tests for FinTrack Nordic domain models."""
import pytest
from src.models import Holding, Portfolio


def test_holding_cost_basis():
    """Validates basic cost basis arithmetic."""
    holding = Holding(symbol="EQNR", shares=10.0, acquisition_price=300.0)
    assert holding.cost_basis == 3000.0


def test_holding_validation_positive_shares():
    """Task 2 Check: Ensure shares must be strictly positive (> 0)."""
    with pytest.raises(ValueError, match="(?i)shares"):
        Holding(symbol="DNB", shares=0.0, acquisition_price=200.0)

    with pytest.raises(ValueError, match="(?i)shares"):
        Holding(symbol="DNB", shares=-5.0, acquisition_price=200.0)


def test_holding_validation_positive_price():
    """Task 2 Check: Ensure acquisition price cannot be negative (< 0)."""
    with pytest.raises(ValueError, match="(?i)price"):
        Holding(symbol="YAR", shares=5.0, acquisition_price=-10.0)


def test_portfolio_total_cost():
    """Validates portfolio total cost aggregation across multiple holdings."""
    h1 = Holding(symbol="EQNR", shares=10.0, acquisition_price=300.0)
    h2 = Holding(symbol="DNB", shares=20.0, acquisition_price=200.0)
    portfolio = Portfolio(owner="Kari Nordmann", holdings=[h1, h2])

    assert portfolio.total_cost() == 7000.0


def test_portfolio_unrealized_pnl_gain():
    """Task 1 Check: Calculates unrealized capital gain or loss accurately."""
    h1 = Holding(symbol="EQNR", shares=10.0, acquisition_price=300.0)  # Cost: 3000
    h2 = Holding(symbol="DNB", shares=20.0, acquisition_price=200.0)   # Cost: 4000
    portfolio = Portfolio(owner="Ola Nordmann", holdings=[h1, h2])

    # Current market prices: EQNR up to 350, DNB down to 190
    market_prices = {"EQNR": 350.0, "DNB": 190.0}
    # Market value: (10*350) + (20*190) = 3500 + 3800 = 7300
    # Total cost: 7000 => PnL: +300
    assert portfolio.unrealized_pnl(market_prices) == pytest.approx(300.0)


def test_portfolio_unrealized_pnl_missing_ticker_raises_key_error():
    """Task 1 Check: Missing ticker in the price feed must raise a descriptive KeyError."""
    h1 = Holding(symbol="EQNR", shares=10.0, acquisition_price=300.0)
    portfolio = Portfolio(owner="Ola Nordmann", holdings=[h1])

    market_prices = {"DNB": 210.0}  # Missing EQNR
    with pytest.raises(KeyError, match="EQNR"):
        portfolio.unrealized_pnl(market_prices)
