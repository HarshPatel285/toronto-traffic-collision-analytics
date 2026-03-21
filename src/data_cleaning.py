import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert column names to uppercase and remove spaces.
    """
    df.columns = df.columns.str.upper().str.replace(" ", "_")
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    """
    return df.drop_duplicates()


def remove_invalid_coordinates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows with invalid map coordinates.
    """
    if "LAT_WGS84" in df.columns and "LONG_WGS84" in df.columns:

        df = df[(df["LAT_WGS84"] != 0) & (df["LONG_WGS84"] != 0)]

    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in dataset.
    """

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Fill missing categorical values
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].fillna("Unknown")

    return df


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:

    df = standardize_column_names(df)

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    df = remove_invalid_coordinates(df)

    return df