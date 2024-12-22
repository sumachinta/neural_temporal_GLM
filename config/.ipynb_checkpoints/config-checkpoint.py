from typing import List

class Config:
    """Configuration class to store analysis parameters."""
    def __init__(self, lags: int, n_shuffles: int, alpha_values: List[int], test_size: float, time_bin: float):
        self.lags = lags
        self.n_shuffles = n_shuffles
        self.alpha_values = alpha_values
        self.test_size = test_size
        self.time_bin = time_bin

# Configuration setup
config = Config(
    lags=10, # How many time bins to take around the current 't'
    n_shuffles=1000, # Number of shuffles to get shuffled R2
    alpha_values=[700, 1000, 1200, 1500, 2000, 5000, 10000], # Hyper paramtere tuning
    test_size=0.2,  # Fraction of data used for testing
    time_bin =.02 # Duration of each bin in seconds
)

