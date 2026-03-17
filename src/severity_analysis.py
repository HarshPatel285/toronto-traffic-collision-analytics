import pandas as pd

def fatal_collisions(df: pd.DataFrame) -> int:
    """
    Count fatal collisions.
    """

    if "FATALITIES" not in df.columns:
        raise ValueError("Dataset must contain FATALITIES column")

    return len(df[df["FATALITIES"] > 0])

def injury_collisions(df: pd.DataFrame) -> int:
    """
    Count injury collisions.
    """

    if "INJURY_COLLISIONS" not in df.columns:
        raise ValueError("Dataset must contain INJURY_COLLISIONS column")

    return len(df[df["INJURY_COLLISIONS"] == "YES"])