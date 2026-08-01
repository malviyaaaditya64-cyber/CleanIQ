import pandas as pd


def detect_column_types(df):

    report = []

    for column in df.columns:

        dtype = str(df[column].dtype)

        suggestion = "OK"

        col = column.lower()

        if "date" in col or "dob" in col or "time" in col:
            suggestion = "📅 Convert to Datetime"

        elif "email" in col:
            suggestion = "📧 Validate Email Format"

        elif "phone" in col or "mobile" in col:
            suggestion = "📱 Validate Phone Numbers"

        elif "id" in col:
            suggestion = "🆔 Primary Key Candidate"

        elif dtype == "object":

            unique_ratio = df[column].nunique() / len(df)

            if unique_ratio < 0.05:
                suggestion = "🏷 Convert to Category"

        report.append(
            {
                "Column": column,
                "Current Type": dtype,
                "Suggestion": suggestion
            }
        )

    return pd.DataFrame(report)