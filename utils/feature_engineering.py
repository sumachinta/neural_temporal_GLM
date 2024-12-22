#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import Tuple, List

def create_lagged_features(
    data: pd.DataFrame, lags: int, time_bins: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Create lagged features for a given dataset.
    
    Args:
        data (pd.DataFrame): Data containing run_data, stpt_data, amp_data, and spike_data.
        lags (int): Number of lags to consider.
        time_bins (np.ndarray): Array of time bins.
    
    Returns:
        Tuple[np.ndarray, np.ndarray]: Arrays X (features) and y (target).
    """
    X_list: List[np.ndarray] = []
    y_list: List[float] = []
    
    for i in range(lags, len(data) - lags):
        if is_valid_window(time_bins, i, lags):
            X_list.append(np.concatenate([
                data['run_data'].values[i - lags:i + lags + 1],
                data['stpt_data'].values[i - lags:i + lags + 1],
                data['amp_data'].values[i - lags:i + lags + 1]
            ]))
            y_list.append(data['spike_data'].values[i])
    
    X = np.array(X_list)
    y = np.array(y_list)
    return X, y


def standardize_features(X: np.ndarray) -> Tuple[np.ndarray, StandardScaler]:
    """
    Standardize features using StandardScaler.
    
    Args:
        X (np.ndarray): Feature matrix.
    
    Returns:
        Tuple[np.ndarray, StandardScaler]: Scaled features and the scaler object.
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler


def adjust_coefficients(
    beta_0: float, beta: np.ndarray, scaler: StandardScaler
) -> Tuple[float, np.ndarray]:
    """
    Adjust coefficients and intercept after standardization.
    
    Args:
        beta_0 (float): Intercept from the model fitted on standardized features.
        beta (np.ndarray): Coefficients from the model fitted on standardized features.
        scaler (StandardScaler): Scaler object used to standardize features.
    
    Returns:
        Tuple[float, np.ndarray]: Adjusted intercept and coefficients.
    """
    mu = scaler.mean_
    sigma = scaler.scale_
    gamma = beta / sigma
    gamma_0 = beta_0 - np.sum((beta * mu) / sigma)
    return gamma_0, gamma

