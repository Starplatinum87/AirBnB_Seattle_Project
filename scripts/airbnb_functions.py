import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

def probabilistic_nan_replacement(series):
    """Replace NaNs based on the probability distribution of values present in data
    Parameters
    ----------
    series: pandas series
        Series where NaNs must be replaced

    Returns
    -------
    new_series: pandas series
        Series with nan values replaced
    """

    # Create list of values for the probability distribution and probabilities associated with each one
    values = list(series.value_counts.index)
    probs = list(series.value_counts()/series.value_counts().sum())

    nan_values = np.random.choice(values, size=series.isna().sum(), p=probs)

    nan_replacements = pd.Series(nan_values, index=series.loc[series.isna()].index)
    new_series = pd.concat([series.loc[series.notna()], nan_replacements]).sort_index()

    return new_series

def adjusted_r2(x_train, y_pred, y_test):
    r2 = r2_score(y_pred, y_test)
    n = x_train.shape[0]
    k = x_train.shape[1]
    adj_r2 = 1 - (((1-r2) * (n - 1)) / (n - k -1))
    return adj_r2


def scale_data(X, y, num):
    """Standard scale numerical data and one-hot encode categorical data
    Parameters
    ----------
    X: DataFrame
        Feature set
    y: Series
        Target set
    num: list
        List of strings of numerical features
        
    Returns
    -------
    df_scaled: DataFrame
        DataFrame with scaled and encoded features
    """

    X_numerical = X[num]

    scaler = StandardScaler()
    X_numerical = scaler.fit_transform(X_numerical)

    X_numerical = pd.DataFrame(X_numerical, columns=num, index=X.index)

    df_scaled = pd.concat([y, X_numerical, X.drop(num, axis=1)], axis=1, ignore_index=False)

    return df_scaled