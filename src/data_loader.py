import pandas as pd
import os


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load the traffic collision dataset from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the dataset file.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.

    Raises
    ------
    FileNotFoundError
        If dataset file does not exist.
    ValueError
        If dataset is empty.
    """

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file not found: {file_path}")

    # Load dataset
    df = pd.read_csv(file_path)

    # Validate dataset
    validate_dataset(df)

    return df


def validate_dataset(df: pd.DataFrame) -> None:
    """
    Validate that dataset contains valid rows and columns.
    """

    if df.empty:
        raise ValueError("Loaded dataset is empty.")

    if len(df.columns) == 0:
        raise ValueError("Dataset has no columns.")


def preview_dataset(df: pd.DataFrame, rows: int = 5) -> pd.DataFrame:
    """
    Return a preview of the dataset.

    Parameters
    ----------
    df : DataFrame
    rows : int

    Returns
    -------
    DataFrame
    """

    return df.head(rows)