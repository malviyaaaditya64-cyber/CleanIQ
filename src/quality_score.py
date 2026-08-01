def calculate_quality_score(df):

    total_cells = df.shape[0] * df.shape[1]

    if total_cells == 0:
        return 0

    missing = df.isna().sum().sum()

    duplicates = df.duplicated().sum()

    missing_penalty = (missing / total_cells) * 100

    duplicate_penalty = (duplicates / len(df)) * 100 if len(df) else 0

    score = 100 - (missing_penalty + duplicate_penalty)

    score = max(0, min(100, round(score, 2)))

    return score