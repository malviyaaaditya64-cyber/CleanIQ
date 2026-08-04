import pandas as pd


def answer_question(df, question):

    q = question.lower()

    if "rows" in q:
        return f"The dataset contains {len(df):,} rows."

    elif "columns" in q:
        return f"The dataset contains {len(df.columns)} columns."

    elif "missing" in q:
        return f"Missing values: {int(df.isna().sum().sum())}"

    elif "duplicate" in q:
        return f"Duplicate rows: {int(df.duplicated().sum())}"

    elif "memory" in q:
        memory = round(
            df.memory_usage(deep=True).sum()/1024/1024,
            2
        )
        return f"Memory Usage: {memory} MB"

    elif "numeric" in q:
        n = len(df.select_dtypes(include="number").columns)
        return f"Numeric Columns: {n}"

    elif "categorical" in q:
        c = len(df.select_dtypes(include="object").columns)
        return f"Categorical Columns: {c}"

    elif "quality" in q:
        return "Please open the Data Quality tab for the complete quality report."

    else:

     suggestions = []

    if df.isna().sum().sum() > 0:
        suggestions.append(
            f"• Remove {int(df.isna().sum().sum())} missing values."
        )

    if df.duplicated().sum() > 0:
        suggestions.append(
            f"• Remove {int(df.duplicated().sum())} duplicate rows."
        )

    if len(df.select_dtypes(include="object").columns) > 0:
        suggestions.append(
            "• Encode categorical columns before Machine Learning."
        )

    suggestions.append(
        "• Scale numeric features before model training."
    )

    suggestions.append(
        "• Check outliers before building models."
    )

    return (
        "I couldn't understand your question.\n\n"
        "Here are some recommendations for your dataset:\n\n"
        + "\n".join(suggestions)
    )