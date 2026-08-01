import pandas as pd


def auto_fix_dataset(
    df,
    remove_duplicates=True,
    fill_missing=True,
    trim_spaces=True,
    standardize_text=True,
    optimize_types=True,
    remove_empty=True
):

    cleaned_df = df.copy()

    report = []

    # ----------------------------------
    # Remove Duplicate Rows
    # ----------------------------------

    if remove_duplicates:

        duplicate_count = cleaned_df.duplicated().sum()

        if duplicate_count > 0:

            cleaned_df = cleaned_df.drop_duplicates()

            report.append(
                f"✅ Removed {duplicate_count} duplicate rows."
            )

    # ----------------------------------
    # Remove Empty Rows
    # ----------------------------------

    if remove_empty:

        empty_rows = cleaned_df.isna().all(axis=1).sum()

        if empty_rows > 0:

            cleaned_df = cleaned_df.dropna(how="all")

            report.append(
                f"✅ Removed {empty_rows} empty rows."
            )

    # ----------------------------------
    # Remove Empty Columns
    # ----------------------------------

    if remove_empty:

        empty_columns = cleaned_df.columns[
            cleaned_df.isna().all()
        ]

        if len(empty_columns) > 0:

            cleaned_df = cleaned_df.drop(
                columns=empty_columns
            )

            report.append(
                f"✅ Removed {len(empty_columns)} empty columns."
            )

    # ----------------------------------
    # Trim Spaces
    # ----------------------------------

    if trim_spaces:

        object_columns = cleaned_df.select_dtypes(
            include="object"
        ).columns

        for col in object_columns:

            cleaned_df[col] = (
                cleaned_df[col]
                .astype(str)
                .str.strip()
            )

        report.append(
            "✅ Trimmed extra spaces."
        )

    # ----------------------------------
    # Fill Missing Values
    # ----------------------------------

    if fill_missing:

        for col in cleaned_df.columns:

            if cleaned_df[col].dtype == "object":

                mode = cleaned_df[col].mode()

                if not mode.empty:

                    cleaned_df[col] = cleaned_df[col].fillna(
                        mode[0]
                    )

            else:

                cleaned_df[col] = cleaned_df[col].fillna(
                    cleaned_df[col].median()
                )

        report.append(
            "✅ Filled missing values."
        )

    # ----------------------------------
    # Standardize Text
    # ----------------------------------

    if standardize_text:

        object_columns = cleaned_df.select_dtypes(
            include="object"
        ).columns

        for col in object_columns:

            cleaned_df[col] = (
                cleaned_df[col]
                .astype(str)
                .str.title()
            )

        report.append(
            "✅ Standardized text."
        )

    # ----------------------------------
    # Optimize Data Types
    # ----------------------------------

    if optimize_types:

        for col in cleaned_df.select_dtypes(include="integer").columns:

            cleaned_df[col] = pd.to_numeric(
                cleaned_df[col],
                downcast="integer"
            )

        for col in cleaned_df.select_dtypes(include="float").columns:

            cleaned_df[col] = pd.to_numeric(
                cleaned_df[col],
                downcast="float"
            )

        report.append(
            "✅ Optimized numeric data types."
        )

    return cleaned_df, report