import numpy as np

def is_valid_window(times: np.ndarray, index: int, window: int = 10, interval: float = 0.025) -> bool:
    """
    Check if a time window is valid based on the given interval.
    
    Args:
        times (np.ndarray): Array of time points.
        index (int): Index around which to check the window.
        window (int, optional): Size of the window. Defaults to 10.
        interval (float, optional): Maximum allowed interval. Defaults to 0.025.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    if index - window < 0 or index + window >= len(times):
        return False
    for i in range(index - window, index + window):
        if times[i + 1] - times[i] > interval:
            return False
    return True

