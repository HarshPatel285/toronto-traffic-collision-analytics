import pandas as pd


def collisions_by_hour(df: pd.DataFrame) -> pd.Series:
    """
    Calculate number of collisions by hour of day.
    """

    if "OCC_HOUR" not in df.columns:
        raise ValueError("Dataset must contain OCC_HOUR column")

    hourly_counts = df.groupby("OCC_HOUR").size()

    return hourly_counts.sort_index()


def collisions_by_weekday(df: pd.DataFrame) -> pd.Series:
    """
    Calculate number of collisions by weekday.
    """

    if "OCC_DOW" not in df.columns:
        raise ValueError("Dataset must contain OCC_DOW column")

    weekday_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    weekday_counts = df.groupby("OCC_DOW").size()

    return weekday_counts.reindex(weekday_order)

def peak_collision_hour(df: pd.DataFrame) -> int:
    """
    Identify hour with highest number of collisions.
    """

    hourly_counts = collisions_by_hour(df)

    return hourly_counts.idxmax()

def peak_collision_day(df: pd.DataFrame) -> str:
    """
    Identify weekday with highest number of collisions.
    """

    weekday_counts = collisions_by_weekday(df)

    return weekday_counts.idxmax()