#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def shuffle_spike_data(spike_data: np.ndarray) -> np.ndarray:
    """
    Shuffle spike rate data.
    
    Args:
        spike_data (np.ndarray): Array of spike rate data.
    
    Returns:
        np.ndarray: Shuffled spike data.
    """
    shuffled_data = spike_data.copy()
    np.random.shuffle(shuffled_data)
    return shuffled_data

