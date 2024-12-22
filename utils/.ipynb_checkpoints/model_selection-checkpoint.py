import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from typing import List

def find_best_alpha(X_train: np.ndarray, y_train: np.ndarray, alpha_values: List[float]) -> float:
    """
    Perform grid search to find the best alpha for Ridge regression.
    
    Args:
        X_train (np.ndarray): Training feature matrix.
        y_train (np.ndarray): Training target vector.
        alpha_values (List[float]): List of alpha values to test.
    
    Returns:
        float: Best alpha value.
    """
    ridge = Ridge(fit_intercept=True)
    param_grid = {'alpha': alpha_values}
    grid_search = GridSearchCV(ridge, param_grid, cv=5, scoring='r2')
    grid_search.fit(X_train, y_train)
    return grid_search.best_params_['alpha']

