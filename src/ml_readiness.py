import pandas as pd


def calculate_ml_readiness(df):

    score = 100

    # Missing Values
    missing_percent = (df.isna().sum().sum() / (df.shape[0] * df.shape[1])) * 100

    score -= min(missing_percent, 30)

    # Duplicate Rows
    duplicate_percent = (df.duplicated().sum() / len(df)) * 100

    score -= min(duplicate_percent, 20)

    # Constant Columns
    constant_columns = sum(df.nunique(dropna=False) == 1)

    score -= constant_columns * 5

    # Object Columns
    object_columns = len(df.select_dtypes(include="object").columns)

    score -= min(object_columns * 2, 20)

    score = max(0, round(score))

    return score