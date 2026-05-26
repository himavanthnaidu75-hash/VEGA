import math

class RiskManager:
    def __init__(self, total_capital, max_risk_per_trade=0.01, kelly_fraction=0.5):
        self.total_capital = total_capital
        self.max_risk_per_trade = max_risk_per_trade
        self.kelly_fraction = kelly_fraction
        self.win_rate = 0.45  # Estimated starting win rate
        self.risk_reward = 2.0

    def calculate_position_size(self, entry_price, stop_loss):
        """
        Calculate size based on Kelly Criterion and Fixed Fractional.
        """
        risk_per_share = abs(entry_price - stop_loss)
        if risk_per_share == 0: return 0

        # Kelly: f* = (p(r+1) - 1) / r
        # where p is win rate, r is win/loss ratio
        kelly_f = (self.win_rate * (self.risk_reward + 1) - 1) / self.risk_reward
        kelly_f = max(0, min(kelly_f, 0.2)) * self.kelly_fraction # Cap Kelly

        # Fixed Fractional risk
        max_loss_allowed = self.total_capital * self.max_risk_per_trade

        size_ff = max_loss_allowed / risk_per_share
        size_kelly = (self.total_capital * kelly_f) / entry_price

        # Return the more conservative size
        return math.floor(min(size_ff, size_kelly))

    def validate_trade(self, entry, stop, target):
        """Check R:R filter."""
        risk = abs(entry - stop)
        reward = abs(target - entry)
        if risk == 0: return False
        return (reward / risk) >= self.risk_reward
