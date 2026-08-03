"""
Dataset Profile Service (Optimized)

Creates a compact dataset profile for LLM analysis.
"""

import pandas as pd


class DatasetProfileService:

    @staticmethod
    def build(df: pd.DataFrame) -> str:

        profile = []

        # ==================================================
        # Dataset Overview
        # ==================================================

        profile.append("========== DATASET OVERVIEW ==========")

        profile.append(f"Rows: {len(df)}")
        profile.append(f"Columns: {len(df.columns)}")

        memory = df.memory_usage(deep=True).sum() / 1024 / 1024

        profile.append(f"Memory Usage: {memory:.2f} MB")

        profile.append("")

        # ==================================================
        # Column Types
        # ==================================================

        numerical = df.select_dtypes(include="number")
        categorical = df.select_dtypes(include=["object", "category"])
        datetime = df.select_dtypes(include=["datetime"])
        boolean = df.select_dtypes(include=["bool"])

        profile.append("========== COLUMN SUMMARY ==========")

        profile.append(f"Numerical Columns : {len(numerical.columns)}")
        profile.append(f"Categorical Columns : {len(categorical.columns)}")
        profile.append(f"Datetime Columns : {len(datetime.columns)}")
        profile.append(f"Boolean Columns : {len(boolean.columns)}")

        profile.append("")

        # ==================================================
        # Missing Values
        # ==================================================

        profile.append("========== MISSING VALUES ==========")

        missing = df.isnull().sum()

        has_missing = False

        for col, value in missing.items():

            if value > 0:

                profile.append(f"{col}: {value}")

                has_missing = True

        if not has_missing:

            profile.append("No missing values found.")

        profile.append("")

        # ==================================================
        # Numerical Summary
        # ==================================================

        if not numerical.empty:

            profile.append("========== NUMERICAL FEATURES ==========")

            for col in numerical.columns:

                profile.append(f"\n{col}")

                profile.append(f"Mean : {numerical[col].mean():.2f}")
                profile.append(f"Median : {numerical[col].median():.2f}")
                profile.append(f"Min : {numerical[col].min():.2f}")
                profile.append(f"Max : {numerical[col].max():.2f}")
                profile.append(f"Std : {numerical[col].std():.2f}")

        # ==================================================
        # Categorical Summary
        # ==================================================

        if not categorical.empty:

            profile.append("")
            profile.append("========== CATEGORICAL FEATURES ==========")

            for col in categorical.columns:

                profile.append(f"\n{col}")

                profile.append(
                    f"Unique Values : {categorical[col].nunique()}"
                )

                mode = categorical[col].mode()

                if not mode.empty:

                    profile.append(f"Most Frequent : {mode.iloc[0]}")

        # ==================================================
        # Sample Data
        # ==================================================

        profile.append("")
        profile.append("========== SAMPLE DATA ==========")

        profile.append(
            df.head(3).to_string(index=False)
        )

        return "\n".join(profile)