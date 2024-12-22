#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from typing import Tuple


def fit_and_evaluate(
    X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, y_test: np.ndarray, alpha: float
) -> Tuple[float, float, float, np.ndarray, np.ndarray]:
    """
    Fit Ridge regression with the best alpha and evaluate performance.
    
    Args:
        X_train (np.ndarray): Training feature matrix.
        y_train (np.ndarray): Training target vector.
        X_test (np.ndarray): Testing feature matrix.
        y_test (np.ndarray): Testing target vector.
        alpha (float): Regularization parameter for Ridge regression.
    
    Returns:
        Tuple[float, float, float, np.ndarray, np.ndarray]: MSE, R-squared, intercept, coefficients, and predicted values.
    """
    best_ridge = Ridge(alpha=alpha, fit_intercept=True)
    best_ridge.fit(X_train, y_train)
    
    y_pred = best_ridge.predict(X_test)
    mse_value = mean_squared_error(y_test, y_pred)
    r2_value = r2_score(y_test, y_pred)
    coefficients = best_ridge.coef_
    intercept = best_ridge.intercept_
    
    return mse_value, r2_value, intercept, coefficients, y_pred

