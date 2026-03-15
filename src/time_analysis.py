import pandas as pd


def collisions_by_hour(df: pd.DataFrame) -> pd.Series:
    """
    Calculate number of collisions by hour of day.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.Series
        Hourly collision counts.
    """

    if "OCC_HOUR" not in df.columns:
        raise ValueError("Dataset must contain OCC_HOUR column")

    hourly_counts = df.groupby("OCC_HOUR").size()

    return hourly_counts.sort_index()


def collisions_by_weekday(df: pd.DataFrame) -> pd.Series:
    """
    Calculate number of collisions by weekday.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.Series
        Weekday collision counts.
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


def collisions_by_month(df: pd.DataFrame) -> pd.Series:
    """
    Calculate number of collisions by month.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.Series
        Monthly collision counts.
    """

    if "OCC_MONTH" not in df.columns:
        raise ValueError("Dataset must contain OCC_MONTH column")

    month_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    monthly_counts = df.groupby("OCC_MONTH").size()

    return monthly_counts.reindex(month_order)


def peak_collision_hour(df: pd.DataFrame) -> int:
    """
    Identify the hour with the highest number of collisions.
    """

    hourly_counts = collisions_by_hour(df)

    return hourly_counts.idxmax()


def peak_collision_day(df: pd.DataFrame) -> str:
    """
    Identify the weekday with the highest number of collisions.
    """

    weekday_counts = collisions_by_weekday(df)

    return weekday_counts.idxmax()


def monthly_collision_trend(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return monthly collision counts as a dataframe.
    Useful for dashboards.
    """

    monthly_counts = collisions_by_month(df)

    return monthly_counts.reset_index().rename(
        columns={
            "OCC_MONTH": "Month",
            0: "Collisions"
        }
    )