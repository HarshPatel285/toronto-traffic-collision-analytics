import pandas as pd

def fatal_collisions(df: pd.DataFrame) -> int:
    """
    Count fatal collisions.
    """

    if "FATALITIES" not in df.columns:
        raise ValueError("Dataset must contain FATALITIES column")

    return len(df[df["FATALITIES"] > 0])