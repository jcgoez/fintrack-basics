"""Domain models for FinTrack Nordic portfolio monitoring."""
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Holding:
    """Represents a single stock or asset position."""
    symbol: str
    shares: float
    acquisition_price: float

    # TODO (Task 2): Use Antigravity inline command (Ctrl+I) to add input validation:
    # 1. shares must be > 0 (raise ValueError)
    # 2. acquisition_price must be >= 0 (raise ValueError)
    # 3. symbol should be converted to uppercase

    @property
    def cost_basis(self) -> float:
        """Total invested capital for this holding."""
        return self.shares * self.acquisition_price


@dataclass
class Portfolio:
    """Represents an investor portfolio containing multiple holdings."""
    owner: str
    holdings: List[Holding] = field(default_factory=list)

    def total_cost(self) -> float:
        """Total acquisition cost across all holdings in the portfolio."""
        return sum(h.cost_basis for h in self.holdings)

    def unrealized_pnl(self, current_market_prices: Dict[str, float]) -> float:
        """
        Calculates total unrealized profit or loss (Market Value - Cost Basis).

        TODO (Task 1): Use Antigravity /plan in the sidebar agent to implement this:
        1. Iterate through holdings and calculate total market value.
        2. If any holding symbol is missing from current_market_prices, raise KeyError.
        3. Return total_market_value - self.total_cost().
        """
        raise NotImplementedError("Task 1: Implement unrealized_pnl using Antigravity /plan")
