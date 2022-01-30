# from scipy import stats
import pandas as pd

def remove_outliers(serie):
    """
    Remove outliers from a pandas series,
    based on quantiles.
    
    Args:
        serie: The pandas serie
    
    Returns:
        A pandas serie without outliers

    """
    q1 = serie.quantile(q=.25)
    q3 = serie.quantile(q=.75)
    iqr = stats.iqr(serie)
    upper_limit = q3 + (1.5*iqr)
    lower_limit = q1 - (1.5*iqr)
    
    sr = serie[(serie>lower_limit)&(serie<upper_limit)]


    return sr