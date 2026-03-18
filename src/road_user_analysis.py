import pandas as pd

def pedestrian_collisions(df: pd.DataFrame) -> int:
    """
    Count collisions involving pedestrians.
    """
    if "PEDESTRIAN" not in df.columns:
        raise ValueError("Dataset must contain PEDESTRIAN column")

    return len(df[df["PEDESTRIAN"] == "YES"])


def motorcycle_collisions(df: pd.DataFrame) -> int:
    """
    Count collisions involving motorcycles.
    """
    if "MOTORCYCLE" not in df.columns:
        raise ValueError("Dataset must contain MOTORCYCLE column")

    return len(df[df["MOTORCYCLE"] == "YES"])


def bicycle_collisions(df: pd.DataFrame) -> int:
    """
    Count collisions involving bicycles.
    """
    if "BICYCLE" not in df.columns:
        raise ValueError("Dataset must contain BICYCLE column")

    return len(df[df["BICYCLE"] == "YES"])


def automobile_collisions(df: pd.DataFrame) -> int:
    """
    Count collisions involving automobiles.
    """
    if "AUTOMOBILE" not in df.columns:
        raise ValueError("Dataset must contain AUTOMOBILE column")

    return len(df[df["AUTOMOBILE"] == "YES"])