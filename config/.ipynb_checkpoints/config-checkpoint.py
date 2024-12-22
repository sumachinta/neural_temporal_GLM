from typing import List

class Config:
    """Configuration class to store analysis parameters."""
    def __init__(self, lags: int, n_shuffles: int, alpha_values: List[int]):
        self.lags = lags
        self.n_shuffles = n_shuffles
        self.alpha_values = alpha_values

# Configuration setup
config = Config(
    lags=10,
    n_shuffles=1000,
    alpha_values=[700, 1000, 1200, 1500, 2000, 5000, 10000]
)

