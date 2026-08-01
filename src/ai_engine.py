import pandas as pd


def generate_recommendations(df):

    recommendations = []

    # Missing Values
    missing = df.isna().sum()

    for col in missing.index:

        if missing[col] > 0:

            percent = round(
                (missing[col] / len(df)) * 100,
                2
            )

            if percent < 10:

                recommendations.append(
                    f"🟢 {col}: Fill missing values."
                )

            elif percent < 40:

                recommendations.append(
                    f"🟡 {col}: Median/Mode imputation recommended."
                )

            else:

                recommendations.append(
                    f"🔴 {col}: High missing values ({percent}%). Consider dropping."
                )

    # Duplicate Rows
    duplicate_rows = df.duplicated().sum()

    if duplicate_rows > 0:

        recommendations.append(
            f"🔁 Remove {duplicate_rows} duplicate rows."
        )

    # Numeric Columns
    numeric = df.select_dtypes(include="number")

    for col in numeric.columns:

        q1 = numeric[col].quantile(.25)

        q3 = numeric[col].quantile(.75)

        iqr = q3 - q1

        outliers = numeric[
            (numeric[col] < q1 - 1.5 * iqr)
            |
            (numeric[col] > q3 + 1.5 * iqr)
        ]

        if len(outliers) > 0:

            recommendations.append(
                f"📈 {col}: {len(outliers)} outliers detected."
            )

    if len(recommendations) == 0:

        recommendations.append(
            "✅ Dataset looks healthy."
        )

    return recommendations